const send_btn = document.getElementById("send-btn");
const input_box = document.getElementById("chat-input");
const chat_area = document.querySelector(".chat-main");

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
    input_box.value = '';

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
        const bot_message_html = `<div class='chat-message message-bot'>${data.response}</div>`;
        chat_area.innerHTML += bot_message_html;
        console.log('Success:', data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
}

function clear_messages(){
  chat_area.innerHTML = '';
}