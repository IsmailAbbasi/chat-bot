const send_btn = document.getElementById("send-btn");
const input_box = document.getElementById("chat-input");
const chat_area = document.querySelector(".chat-main");
const bot_typing = document.querySelector(".bot-typing");

send_btn.addEventListener('click', send_message)
input_box.addEventListener('keypress', function(e){
    if (e.key=='Enter'){
        send_message();
    }
})

function send_message(event){
    const message = input_box.value;

    if (message == ''){
      return;
    }

    const user_message_html = `<div class='chat-message message-user'>${message}</div>`;
    chat_area.innerHTML += user_message_html;
    chat_area.scrollTop = chat_area.scrollHeight;
    input_box.value = '';
    chat_area.innerHTML += `<div class="bot-typing" >
    <lord-icon
        src="https://cdn.lordicon.com/dxjqoygy.json"
        trigger="loop"
        style="width:40px;height:40px">
    </lord-icon>
    <i style="opacity:0.7;position:relative;top:2px;font-size:13px;">&nbsp;Ultron is typing...</i>
</div>`;

    if (message == 'clear all'){
      clear_messages();
      return;
    }
    fetch('/send-msg/', {
        method: 'POST', // or 'PUT'
        body: JSON.stringify({"message":message}),
      })
      .then(response => response.json())
      .then(data => {
        document.querySelectorAll(".bot-typing").forEach(el => el.remove());
        const bot_message_html = `<div class='chat-message message-bot'>${data.response}</div>`;
        chat_area.innerHTML += bot_message_html;
        chat_area.scrollTop = chat_area.scrollHeight;
        if (data.response_type == 'open_link'){
          window.open(data.action);
        }
        console.log('Success:', data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
}

function clear_messages(){
  chat_area.innerHTML = '';
}