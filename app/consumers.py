from django.conf import settings
from django.contrib.auth.models import User

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer


@database_sync_to_async
def get_user(_id):
    return list(User.objects.filter(id=_id).values('username', 'first_name', 'email', 'id', 'useraddinfo__avatar'))[0]

@database_sync_to_async
def set_user_online_status(_id, status):
    user = User.objects.get(id=_id)
    user.useraddinfo.status = status
    user.save()

@database_sync_to_async
def get_user_status(_id):
    return User.objects.get(id=_id).useraddinfo.status

class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print(f"connected : {self.scope['user'].username}")
        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            # when user had logged in it will create an group with its user id, so that if we want to 
            # send any meesage you can just specify group id this way we can use single chat/multi chat application
            # Eg: Multi chat: 'chaosMonkeys' when user has connected to websocket, all can post message by mentioning this group_name 
            # single chat : 'user_id' when user needs to chat he needs to specify user_id  
            group_name = str(self.scope["user"].id)
            await self.channel_layer.group_add(group_name, self.channel_name) 
            await self.accept()
            await set_user_online_status(self.scope["user"].id, 'online')
            
    async def disconnect(self, code):
        print(f'Disconnected {code}')
        await set_user_online_status(self.scope["user"].id, 'offline')

    async def receive_json(self, content):
        print(f"Recived input {content}")
        """
        user = User.objects.get(id=channel_id).values('username', 'first_name', 'email')  # Error
        # here sysnc methods wont work when you want to contact database, so if you need to connect db ref below await get_user methods
        """
        if content['command'] == 'message':
            channel_id = content['receiver'] # here we are passing user id
            chat_params = {
                   "type": "chat.join", # here it represents which function to call, chat_join `.` represents `_` and this parameter is must
                   "data": {
                      "command"  : content['command'],
                      "message"  : content['message'],
                      "sender"   : await get_user(self.scope["user"].id),
                      "receiver" : await get_user(int(channel_id))
                   } 
            }
        elif content['command'] == 'user_status':
           channel_id = str(self.scope["user"].id)
           chat_params = {
                   "type": "chat.join",
                   "data": {
                      "comamnd"  : content['command'],
                      "message"  : await get_user_status(int(content['receiver'])),
                      "sender"   : await get_user(self.scope["user"].id),
                      "receiver" : await get_user(int(content['receiver']))
                   } 
           }
        await self.channel_layer.group_send(channel_id, chat_params)
           
        
    async def chat_join(self, event):
        await self.send_json(event['data'])
