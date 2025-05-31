document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chatbot-form');
    const userInput = document.getElementById('user-input');
    const chatHistory = document.getElementById('chat-history');

    // Listen for form submission
    chatForm.addEventListener('submit', function(e) {
        e.preventDefault(); // Prevent form from reloading the page

        // Get user input and clear the input field
        const message = userInput.value.trim();
        if (!message) return;

        // Display user's message
        chatHistory.innerHTML += `<div class="user-msg"><strong>You:</strong> ${message}</div>`;

        // Send message to Flask backend
        fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: message })
        })
        // Handle the response from the backend
        .then(response => response.json())
        .then(data => {
            // Display AI's response
            chatHistory.innerHTML += `<div class="ai-msg"><strong>ExeOheDus:</strong> ${data.response}</div>`;
            chatHistory.scrollTop = chatHistory.scrollHeight;
        })
        .catch(error => {
            chatHistory.innerHTML += `<div class="error-msg">Error: ${error}</div>`;
        });

        userInput.value = '';
    });
});