const chat = document.getElementById("chat");
const input = document.getElementById("message-input");
const sendButton = document.getElementById("send-btn");

sendButton.addEventListener("click", sendMessage);

input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});

function sendMessage() {

    const text = input.value.trim();

    if (text === "") {
        return;
    }

    addUserMessage(text);

    input.value = "";

    scrollToBottom();

    // Aquí llamaremos a nuestro agente
    //fakeAgentResponse(text);

    // En el futuro será:
     sendToAgent(text);

}

function addUserMessage(text) {

    const message = document.createElement("div");
    message.className = "message user";

    message.innerHTML = `
        <div class="bubble">
            ${escapeHtml(text)}
        </div>
    `;

    chat.appendChild(message);

}

function addAgentMessage(text) {

    const message = document.createElement("div");
    message.className = "message agent";

    message.innerHTML = `
        <img src="images/robot.svg" class="bubble-avatar">

        <div class="bubble">
            ${escapeHtml(text)}
        </div>
    `;

    chat.appendChild(message);

    scrollToBottom();

}

function scrollToBottom() {

    chat.scrollTop = chat.scrollHeight;

}

function escapeHtml(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;

}

function fakeAgentResponse(message) {

    setTimeout(() => {

        addAgentMessage("He recibido tu mensaje: \"" + message + "\"");

    }, 500);

}


async function sendToAgent(message) {

    const response = await fetch("/api/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })

    });

    const data = await response.json();

    addAgentMessage(data.response);

}

