/**
 * Standard Securities - Chatbot JavaScript
 * Enhanced chatbot with improved UX and accessibility
 */

class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }

        this.state = false;
        this.messages = [];
        this.isLoading = false;
        
        // Initialize if elements exist
        if (this.args.openButton && this.args.chatBox && this.args.sendButton) {
            this.display();
        }
    }

    display() {
        const { openButton, chatBox, sendButton } = this.args;

        // Open/close toggle with smooth animation
        openButton.addEventListener('click', () => {
            this.toggleState(chatBox);
            openButton.setAttribute('aria-expanded', !this.state);
        });

        // Send button click
        sendButton.addEventListener('click', () => this.onSendButton(chatBox));

        // Enter key to send
        const node = chatBox.querySelector('input');
        if (node) {
            node.addEventListener("keyup", (event) => {
                if (event.key === "Enter" && !event.shiftKey) {
                    event.preventDefault();
                    this.onSendButton(chatBox);
                }
            });
        }

        // Trap focus within modal when open
        chatBox.addEventListener('keydown', (e) => {
            if (e.key === 'Tab') {
                this.trapFocus(chatBox, e);
            }
            if (e.key === 'Escape' && this.state) {
                this.toggleState(chatBox);
                openButton.focus();
            }
        });

        // Close when clicking outside
        document.addEventListener('click', (e) => {
            if (this.state && !chatBox.contains(e.target) && !openButton.contains(e.target)) {
                this.toggleState(chatBox);
            }
        });
    }

    toggleState(chatbox) {
        this.state = !this.state;

        if (this.state) {
            chatbox.classList.add('chatbox--active');
            // Focus the input when opened
            setTimeout(() => {
                const input = chatbox.querySelector('input');
                if (input) input.focus();
            }, 300);
        } else {
            chatbox.classList.remove('chatbox--active');
        }
    }

    onSendButton(chatbox) {
        if (this.isLoading) return;
        
        var textField = chatbox.querySelector('input');
        let text1 = textField.value.trim();
        
        if (text1 === "") {
            textField.focus();
            return;
        }

        this.isLoading = true;
        
        // Add user message
        let msg1 = { name: "User", message: text1 };
        this.messages.push(msg1);
        this.updateChatText(chatbox);
        textField.value = '';

        // Show typing indicator
        this.showTypingIndicator(chatbox);

        // Simulate bot response (in production, this would be an API call)
        setTimeout(() => {
            this.hideTypingIndicator(chatbox);
            
            // For demo, echo the message with a prefix
            let msg2 = { name: "Sam", message: `Thank you for your message. Our team will get back to you shortly regarding: "${text1}"` };
            this.messages.push(msg2);
            this.updateChatText(chatbox);
            this.isLoading = false;
            
            // Scroll to bottom
            const messagesContainer = chatbox.querySelector('.chatbox__messages');
            if (messagesContainer) {
                messagesContainer.scrollTop = messagesContainer.scrollHeight;
            }
        }, 1500);
        
        // Uncomment below for real API integration
        /*
        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          })
          .then(r => r.json())
          .then(r => {
            this.hideTypingIndicator(chatbox);
            let msg2 = { name: "Sam", message: r.answer };
            this.messages.push(msg2);
            this.updateChatText(chatbox);
            textField.value = '';
            this.isLoading = false;
          }).catch((error) => {
            console.error('Error:', error);
            this.hideTypingIndicator(chatbox);
            let msg2 = { name: "Sam", message: "I apologize, but I'm having trouble connecting. Please try again or contact us through other channels." };
            this.messages.push(msg2);
            this.updateChatText(chatbox);
            textField.value = '';
            this.isLoading = false;
          });
        */
    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Sam") {
                html += '<div class="messages__item messages__item--visitor" role="log" aria-label="Support response">' + this.escapeHtml(item.message) + '</div>';
            } else {
                html += '<div class="messages__item messages__item--operator" role="log" aria-label="Your message">' + this.escapeHtml(item.message) + '</div>';
            }
        }.bind(this));

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        if (chatmessage) {
            chatmessage.innerHTML = html;
            chatmessage.setAttribute('aria-live', 'polite');
        }
    }

    showTypingIndicator(chatbox) {
        const chatmessage = chatbox.querySelector('.chatbox__messages');
        if (chatmessage) {
            const typingHtml = '<div class="messages__item messages__item--typing" aria-label="Support is typing"><span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span></div>';
            chatmessage.insertAdjacentHTML('beforeend', typingHtml);
            chatmessage.scrollTop = chatmessage.scrollHeight;
        }
    }

    hideTypingIndicator(chatbox) {
        const typing = chatbox.querySelector('.messages__item--typing');
        if (typing) {
            typing.remove();
        }
    }

    trapFocus(chatbox, event) {
        const focusableElements = chatbox.querySelectorAll('button, input, [tabindex]:not([tabindex="-1"])');
        const firstElement = focusableElements[0];
        const lastElement = focusableElements[focusableElements.length - 1];

        if (event.shiftKey && document.activeElement === firstElement) {
            event.preventDefault();
            lastElement.focus();
        } else if (!event.shiftKey && document.activeElement === lastElement) {
            event.preventDefault();
            firstElement.focus();
        }
    }

    escapeHtml(text) {
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, (m) => map[m]);
    }
}

// Initialize chatbox when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    const chatbox = new Chatbox();
});

// Also initialize if script loads after DOM
if (document.readyState === 'complete' || document.readyState === 'interactive') {
    setTimeout(() => {
        const chatbox = new Chatbox();
    }, 1);
}