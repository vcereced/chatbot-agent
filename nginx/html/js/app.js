const chat = document.getElementById("chat");
const input = document.getElementById("message-input");
const sendButton = document.getElementById("send-btn");

let conversationId = null;

let currentPlaceholder = null;

const socket = new WebSocket(
    `ws://${window.location.host}/ws`
);

socket.onopen = () => {

    console.log("WebSocket conectado");

};

socket.onmessage = (event) => {

    const data = JSON.parse(event.data);

    console.log(data);

    switch (data.type) {

        case "started":

            updateAgentPlaceholder(
                currentPlaceholder,
                data.message,
            );

            break;

        case "status":

            updateAgentPlaceholder(
                currentPlaceholder,
                data.message,
            );

            break;

        case "finished":

            conversationId = data.conversation_id;

            finishAgentPlaceholder(
                currentPlaceholder,
                data.message,
            );

            currentPlaceholder = null;

            break;

        case "error":

            finishAgentPlaceholder(
                currentPlaceholder,
                data.message,
            );

            currentPlaceholder = null;

            break;

    }

};


socket.onclose = (event) => {
    console.log("CLOSE", event.code, event.reason);
};

socket.onerror = (event) => {
    console.log("ERROR", event);
};

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

    currentPlaceholder = createAgentPlaceholder();

    socket.send(JSON.stringify({

        type: "message",

        conversation_id: conversationId,

        message: text,

    }));

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

    scrollToBottom();

}

function createAgentPlaceholder() {

    const message = document.createElement("div");

    message.className = "message agent";

    message.innerHTML = `
        <img src="images/robot.svg" class="bubble-avatar">

        <div class="bubble status">
            Pensando...
        </div>
    `;

    chat.appendChild(message);

    scrollToBottom();

    return message;

}

function updateAgentPlaceholder(message, text) {

    if (!message) {
        return;
    }

    message.querySelector(".bubble").textContent = text;

    scrollToBottom();

}

function finishAgentPlaceholder(message, text) {

    if (!message) {
        return;
    }

    const bubble = message.querySelector(".bubble");

    bubble.classList.remove("status");

    bubble.textContent = text;

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