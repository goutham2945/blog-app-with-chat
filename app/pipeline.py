import requests 
from django.conf import settings

images_path = settings.IMAGES_PATH

def get_avatar(backend, strategy, details, response,
        user=None, *args, **kwargs):
    url = None
    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
    if backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal','')
    if backend.name == 'google-oauth2':
        url = response.get('picture', '')
    if backend.name == 'github':
       url =  response.get('avatar_url','')
    if url:
        img_data = requests.get(url).content
        img_name = '%s.png'%(user.id)
        with open(images_path + '/' + img_name, 'wb') as f:
            f.write(img_data)
            user.useraddinfo.avatar = img_name
            user.save()
