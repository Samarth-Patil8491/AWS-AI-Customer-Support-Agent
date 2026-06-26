async function sendMessage() {

    const input = document.getElementById("message");
    const message = input.value.trim();

    if (message === "") return;

    const chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `
        <div class="user-message">
            <strong>You</strong><br>
            ${message}
        </div>
    `;

    input.value = "";

    chatBox.innerHTML += `
        <div class="bot-message" id="typing">
            🤖 Typing...
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type":"application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        document.getElementById("typing").remove();

        chatBox.innerHTML += `
            <div class="bot-message">
                <strong>AI Agent</strong><br>
                ${data.reply}
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;
    }
    catch(error){

        document.getElementById("typing").remove();

        chatBox.innerHTML += `
            <div class="bot-message">
                Server Error. Please try again.
            </div>
        `;
    }
}

document.getElementById("message").addEventListener(
    "keypress",
    function(event){
        if(event.key==="Enter"){
            sendMessage();
        }
    }
);