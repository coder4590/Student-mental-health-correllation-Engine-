// ============================================================
// MINDGUARD — AI Chatbot Handler
// ============================================================

const API_BASE = '';
const chatMessages = document.getElementById('chatMessages');
const chatInput = document.getElementById('chatInput');
const sendBtn = document.getElementById('sendBtn');
const typingIndicator = document.getElementById('typingIndicator');
const suggestedPrompts = document.getElementById('suggestedPrompts');

// ---------- Send Message ----------
async function sendMessage() {
    const message = chatInput.value.trim();
    if (!message) return;

    // Hide suggested prompts after first message
    if (suggestedPrompts) suggestedPrompts.style.display = 'none';

    // Add user message
    addMessage(message, 'user');
    chatInput.value = '';
    sendBtn.disabled = true;

    // Show typing indicator
    typingIndicator.style.display = 'block';
    scrollToBottom();

    try {
        const response = await fetch(`${API_BASE}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) throw new Error('Server error');

        const data = await response.json();

        // Hide typing, add bot response
        typingIndicator.style.display = 'none';
        addMessage(data.response, 'bot');

    } catch (error) {
        typingIndicator.style.display = 'none';
        addMessage("I'm having trouble connecting right now. Please try again in a moment. If you're in crisis, please call Kaan Pete Roi at 01779554391.", 'bot');
    } finally {
        sendBtn.disabled = false;
        chatInput.focus();
    }
}

// ---------- Add Message to Chat ----------
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;

    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.textContent = sender === 'bot' ? '🧠' : '👤';

    const content = document.createElement('div');
    content.className = 'message-content';

    const bubble = document.createElement('div');
    bubble.className = 'message-bubble';

    // Handle multi-line bot responses
    if (sender === 'bot') {
        const paragraphs = text.split('\n\n');
        paragraphs.forEach(para => {
            if (para.trim()) {
                const p = document.createElement('p');
                p.innerHTML = para.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
                bubble.appendChild(p);
            }
        });
    } else {
        const p = document.createElement('p');
        p.textContent = text;
        bubble.appendChild(p);
    }

    const time = document.createElement('div');
    time.className = 'message-time';
    time.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

    content.appendChild(bubble);
    content.appendChild(time);
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(content);
    chatMessages.appendChild(messageDiv);

    scrollToBottom();
}

// ---------- Send Suggested Prompt ----------
function sendPrompt(text) {
    chatInput.value = text;
    sendMessage();
}

// ---------- Handle Enter Key ----------
function handleKeyPress(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
}

// ---------- Clear Chat ----------
function clearChat() {
    chatMessages.innerHTML = '';
    if (suggestedPrompts) suggestedPrompts.style.display = 'flex';
    
    // Restore welcome message
    const welcomeDiv = document.createElement('div');
    welcomeDiv.className = 'message bot-message';
    welcomeDiv.innerHTML = `
        <div class="message-avatar">🧠</div>
        <div class="message-content">
            <div class="message-bubble">
                <p>Hi there 👋 I'm your MindGuard AI Companion. I'm here to listen, support, and help you navigate whatever you're going through.</p>
                <p><strong>How are you feeling today?</strong></p>
            </div>
            <div class="message-time">Just now</div>
        </div>
    `;
    chatMessages.appendChild(welcomeDiv);
}

// ---------- Scroll to Bottom ----------
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// ---------- Enable Send Button on Input ----------
chatInput.addEventListener('input', () => {
    sendBtn.disabled = chatInput.value.trim() === '';
});