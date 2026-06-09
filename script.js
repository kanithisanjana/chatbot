const API_URL = "http://127.0.0.1:8000";

async function sendMessage() {

    let inputBox =
    document.getElementById("user-input");

    let message =
    inputBox.value.trim();

    if(message===""){
        return;
    }

    let chatBox =
    document.getElementById("chat-box");

    chatBox.innerHTML +=
    `<div class="user">${message}</div>`;

    inputBox.value="";

    const response =
    await fetch(`${API_URL}/chat`,{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:message
        })

    });

    const data = await response.json();

    chatBox.innerHTML +=
    `<div class="bot">${data.bot_response}</div>`;

    chatBox.scrollTop =
    chatBox.scrollHeight;
}