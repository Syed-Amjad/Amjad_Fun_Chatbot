function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input: userInput }),
    })
        .then(response => response.json())
        .then(data => {
            const chatDisplay = document.getElementById("chat-display");
            chatDisplay.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
            chatDisplay.innerHTML += `<p><strong>Bot:</strong> ${data.text}</p>`;

            const audio = document.getElementById("response-audio");
            audio.src = data.audio;
            audio.hidden = false;
            audio.play();
        });
}
