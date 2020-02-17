$DOM = $(document)
$DOM.ready(function(){

        var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
        var ws_path = ws_scheme + '://' + window.location.host + "/chat/stream/";
        console.log("Connecting to " + ws_path);
        var socket = new ReconnectingWebSocket(ws_path);

        function create_socket_conn() {
            user_id = $(this).attr('user_id')
            user_name = $(this).attr('user_name')
            user_avatar = $(this).attr('user_avatar')
            var add_agent = `<div class="agent_div">
                                      <div class="col-md-2">
                                           <img alt="noimage" src="${user_avatar}"></img>
                                      </div>
                                      <div class="col-md-12" style="padding-left:1.7rem;">
                                           <span>${user_name}</span></br>
                                           <span style="font-size:0.8rem;color:grey" class="status offline">Offline</span>
                                      </div>
                         </div>`
            $('.row.agent').empty().append(add_agent)
            $('.user_messages').empty()
            sel_user = $('input[type="radio"][name="optradio"]')
            sender = $('.user_profile').attr('user_id')
            params = {
                "command":"user_status",
                "message":"user_status",
                "sender": sender,
                "receiver": $('input[type="radio"][name="optradio"]:checked').attr('user_id'),
            } 
            socket.send(JSON.stringify(params));
        }

        function getChatFormattedMsg (img, msg) {
              return `<div class="row col-md-12">
                              <div class="col-md-1">
                                  <img alt="noimage" src="${img}"></img>
                              </div>
                              <div class="col-md-11">
                                   ${msg}
                              </div>
                       </div>`
        }

        function submit_chat_msg(e){
            msg  = $('#ip_chat_msg').val()
            sel_user = $('input[type="radio"][name="optradio"]')
            if(!msg.length) return
            if(!sel_user.is(':checked')) return
            sender = $('.user_profile').attr('user_id')
            usr_img = $('.user_profile').attr('user_avatar')            
            chat_html = getChatFormattedMsg(usr_img, msg)
            $('.user_messages').append(chat_html)
            $('#ip_chat_msg').val('')
            params = {
                "command":"message",
                "sender": sender,
                "receiver": sel_user.first().attr('user_id'),
                "message": msg
            } 
            socket.send(JSON.stringify(params));
        }

        function handleChatMsg (data) {
            user_id = data['sender']['id']
            $(`input[type="radio"][name="optradio"][user_id="${user_id}"]`).click()
            user_img = `/static/images/${data['sender']['useraddinfo__avatar']}`
            chat_html = getChatFormattedMsg(user_img, data['message'])
            $('.user_messages').append(chat_html)
            
        }

        function handleUserStatus (data){
            console.log('i modified status')
            $('.status').removeClass('offline').removeClass('online')
            $('.status').addClass(data['message'])
            $('.status').html(data['message'])
        }

        document.querySelector('#ip_chat_msg').onkeyup = function(e) {
          if (e.keyCode === 13) {  // enter, return
             $('#ip_chat_send').click();
          }
        };

        socket.onopen = function () {
            console.log("Connected to chat socket");
        };
        socket.onclose = function () {
            console.log("Disconnected from chat socket");
        };

        socket.onmessage = function (message) {
              data = JSON.parse(message.data)
              console.log("Got websocket message " + data);
              if(data.command == 'message'){
                  handleChatMsg(data)
              }else if(data.comamnd == 'user_status'){
                  handleUserStatus(data)
              }
        }
        function bindEvents() {
            $DOM.on('change', 'input[type="radio"][name="optradio"]', create_socket_conn)
                .on('click', '#ip_chat_send', submit_chat_msg)
        }

        bindEvents();

})
