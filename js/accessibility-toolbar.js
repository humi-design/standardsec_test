// Accessibility Toolbar JavaScript
// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initAccessibilityToolbar();
});

// Also try to initialize if DOM is already loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAccessibilityToolbar);
} else {
    // DOM already loaded, initialize immediately
    initAccessibilityToolbar();
}

function initAccessibilityToolbar() {
    const toggleBtn = document.getElementById("accessibilityToggle");
    const panel = document.getElementById("accessibilityPanel");
    
    if (!toggleBtn || !panel) {
        console.log('Accessibility toolbar elements not found');
        return;
    }
    
    // Remove inline hidden attribute once JS is initialized
    // Use CSS class instead for better control
    panel.classList.add('accessibility-panel-initialized');
    
    // Ensure panel is hidden initially
    panel.hidden = true;
    
    // Toggle panel on button click
    toggleBtn.addEventListener("click", (e) => {
        e.preventDefault();
        const expanded = toggleBtn.getAttribute("aria-expanded") === "true";
        toggleBtn.setAttribute("aria-expanded", !expanded);
        panel.hidden = expanded;
        
        // Set z-index to ensure panel is on top
        panel.style.zIndex = '10000';
    });
    
    // Close panel when clicking outside
    document.addEventListener('click', (e) => {
        if (!toggleBtn.contains(e.target) && !panel.contains(e.target)) {
            toggleBtn.setAttribute("aria-expanded", "false");
            panel.hidden = true;
        }
    });
    
    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && panel.hidden === false) {
            toggleBtn.setAttribute("aria-expanded", "false");
            panel.hidden = true;
            toggleBtn.focus();
        }
    });
}

// Font resize
function changeFontSize(delta) {
    let body = document.body;
    let currentSize = parseFloat(window.getComputedStyle(body, null).getPropertyValue('font-size'));
    let newSize = currentSize + (delta * 2); // 2px per step
    // Clamp between 12px and 24px
    newSize = Math.max(12, Math.min(24, newSize));
    body.style.fontSize = newSize + 'px';
}

// Dark mode toggle
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}

// Text-to-speech
function readContent() {
    let content = document.querySelector("main") || document.body;
    let text = content.innerText;
    if (window.speechSynthesis) {
        // Cancel any ongoing speech
        window.speechSynthesis.cancel();
        let speech = new SpeechSynthesisUtterance(text);
        speech.lang = "en-IN"; 
        speech.rate = 1.0;
        speech.pitch = 1.0;
        window.speechSynthesis.speak(speech);
    }
}
