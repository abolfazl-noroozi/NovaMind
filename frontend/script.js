
const sendButton = document.getElementById("send");
const questionInput = document.getElementById("question");
const messages = document.getElementById("messages");

function addMessage(text, sender) {
    const message = document.createElement("p");
    message.textContent = `${sender}: ${text}`;
    message.style.marginBottom = "12px";
    messages.appendChild(message);
}

async function sendMessage() {
    const question = questionInput.value.trim();

    if (!question) return;

    addMessage(question, "You");
    questionInput.value = "";

    try {
        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();
        addMessage(data.answer, "NovaMind");

    } catch (error) {
        addMessage(
            "Could not connect to the server. Please try again.",
            "NovaMind"
        );
    }
}

sendButton.addEventListener("click", sendMessage);

questionInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        sendMessage();
    }
});
