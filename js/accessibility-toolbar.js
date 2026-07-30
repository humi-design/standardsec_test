// Accessibility Toolbar JavaScript
// Initialize when DOM is ready
(function() {
    'use strict';
    
    let initialized = false;
    
    function initAccessibilityToolbar() {
        if (initialized) return;
        
        const toggleBtn = document.getElementById("accessibilityToggle");
        const panel = document.getElementById("accessibilityPanel");
        
        if (!toggleBtn || !panel) {
            console.log('Accessibility toolbar elements not found');
            return;
        }
        
        initialized = true;
        
        // Toggle panel on button click
        toggleBtn.addEventListener("click", function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const expanded = toggleBtn.getAttribute("aria-expanded") === "true";
            toggleBtn.setAttribute("aria-expanded", !expanded);
            
            if (expanded) {
                panel.setAttribute('hidden', '');
            } else {
                panel.removeAttribute('hidden');
                // Focus first button in panel
                const firstBtn = panel.querySelector('button, a');
                if (firstBtn) firstBtn.focus();
            }
        });
        
        // Close panel when clicking outside
        document.addEventListener('click', function(e) {
            if (!toggleBtn.contains(e.target) && !panel.contains(e.target)) {
                toggleBtn.setAttribute("aria-expanded", "false");
                panel.setAttribute('hidden', '');
            }
        });
        
        // Close on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                const expanded = toggleBtn.getAttribute("aria-expanded") === "true";
                if (expanded) {
                    toggleBtn.setAttribute("aria-expanded", "false");
                    panel.setAttribute('hidden', '');
                    toggleBtn.focus();
                }
            }
        });
    }
    
    // Initialize on DOMContentLoaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAccessibilityToolbar);
    } else {
        initAccessibilityToolbar();
    }
})();

// Font resize
function changeFontSize(delta) {
    var body = document.body;
    var currentSize = parseFloat(window.getComputedStyle(body, null).getPropertyValue('font-size'));
    var newSize = currentSize + (delta * 2);
    newSize = Math.max(12, Math.min(24, newSize));
    body.style.fontSize = newSize + 'px';
}

// Dark mode toggle
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}

// Text-to-speech
function readContent() {
    var content = document.querySelector("main") || document.body;
    var text = content.innerText;
    if (window.speechSynthesis) {
        window.speechSynthesis.cancel();
        var speech = new SpeechSynthesisUtterance(text);
        speech.lang = "en-IN"; 
        speech.rate = 1.0;
        speech.pitch = 1.0;
        window.speechSynthesis.speak(speech);
    }
}
