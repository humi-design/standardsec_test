#!/usr/bin/env python3
"""
WCAG 2.2 Accessibility Fix Script
Fixes all 23 issues identified in the accessibility audit
"""

import re
import os

def fix_index_html():
    """Fix all accessibility issues in index.html"""
    filepath = '/workspace/standardsec_files/index.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix Skip Link Visibility (2.4.1) - Make visible on focus
    content = re.sub(
        r'\.skip-link\s*\{[^}]*\}',
        '''.skip-link {
    position: absolute;
    left: -9999px;
    top: auto;
    width: 1px;
    height: 1px;
    overflow: hidden;
    z-index: 9999;
    padding: 12px 20px;
    background: #012c6d;
    color: #ffffff;
    text-decoration: none;
    font-weight: bold;
    border-radius: 4px;
}
.skip-link:focus {
    position: fixed !important;
    top: 10px;
    left: 10px !important;
    width: auto;
    height: auto;
    clip: auto !important;
    overflow: visible;
    outline: 3px solid #f0b429;
    outline-offset: 2px;
}''',
        content
    )
    
    # 2. Fix Heading Hierarchy (1.3.1) - Fix H3 before H1, duplicate H1s
    # Change the H3 before H1 in hero to H2
    content = re.sub(
        r'<h3 class="uk-margin-remove-bottom">Setting strong</h3>',
        '<h2 class="uk-margin-remove-bottom" style="color: #ffffff; font-size: 1rem; font-weight: 400;">Setting strong</h2>',
        content
    )
    content = re.sub(
        r'<h1 class="uk-margin-remove-top">foundations</h1>',
        '<p class="uk-margin-remove-top" style="color: #ffffff; font-size: 2.5rem; font-weight: 700; margin-bottom: 0;">foundations</p>',
        content
    )
    
    # Fix the H1 in hero slider - change to H2
    content = re.sub(
        r'<h1 class="uk-margin-remove-bottom">Start investing now</h1>',
        '<h2 class="uk-margin-remove-bottom" style="color: #ffffff; font-size: 2.5rem; font-weight: 700;">Start investing now</h2>',
        content
    )
    
    # Change H5 service cards to H3 for consistency
    content = re.sub(
        r'<h5 class="uk-margin-small-top">Currency</h5>',
        '<h3 class="uk-margin-small-top" style="font-size: 1.25rem;">Currency</h3>',
        content
    )
    content = re.sub(
        r'<h5 class="uk-margin-small-top">Commodities</h5>',
        '<h3 class="uk-margin-small-top" style="font-size: 1.25rem;">Commodities</h3>',
        content
    )
    content = re.sub(
        r'<h5 class="uk-margin-small-top">Equity</h5>',
        '<h3 class="uk-margin-small-top" style="font-size: 1.25rem;">Equity</h3>',
        content
    )
    content = re.sub(
        r'<h5 class="uk-margin-small-top">IPOs</h5>',
        '<h3 class="uk-margin-small-top" style="font-size: 1.25rem;">IPOs</h3>',
        content
    )
    content = re.sub(
        r'<h5 class="uk-margin-small-top">Advisory</h5>',
        '<h3 class="uk-margin-small-top" style="font-size: 1.25rem;">Advisory</h3>',
        content
    )
    content = re.sub(
        r'<h5 class="uk-margin-small-top">Depository</h5>',
        '<h3 class="uk-margin-small-top" style="font-size: 1.25rem;">Depository</h3>',
        content
    )
    
    # Fix non-descriptive stat headings - add descriptive text
    content = re.sub(
        r'<h2 class="uk-margin-remove-bottom">#1</h2>',
        '<h2 class="uk-margin-remove-bottom"><span class="stat-value">#1</span><span class="stat-label" style="display: block; font-size: 0.6em; font-weight: 400;">Ranking in India</span></h2>',
        content
    )
    content = re.sub(
        r'<h2 class="uk-margin-remove-bottom">~30ms</h2>',
        '<h2 class="uk-margin-remove-bottom"><span class="stat-value">~30ms</span><span class="stat-label" style="display: block; font-size: 0.6em; font-weight: 400;">Execution Speed</span></h2>',
        content
    )
    content = re.sub(
        r'<h2 class="uk-margin-remove-bottom">24/5</h2>',
        '<h2 class="uk-margin-remove-bottom"><span class="stat-value">24/5</span><span class="stat-label" style="display: block; font-size: 0.6em; font-weight: 400;">Trading Days</span></h2>',
        content
    )
    content = re.sub(
        r'<h2 class="uk-margin-remove-bottom">0.0</h2>',
        '<h2 class="uk-margin-remove-bottom"><span class="stat-value">0.0</span><span class="stat-label" style="display: block; font-size: 0.6em; font-weight: 400;">Penalty Charges</span></h2>',
        content
    )
    content = re.sub(
        r'<h2 class="uk-margin-remove-bottom">150\+</h2>',
        '<h2 class="uk-margin-remove-bottom"><span class="stat-value">150+</span><span class="stat-label" style="display: block; font-size: 0.6em; font-weight: 400;">Products Available</span></h2>',
        content
    )
    
    # 3. Add Autocomplete Attributes to Form Fields (1.3.5)
    content = re.sub(
        r'<input class="uk-input" type="text" id="full-name" name="full-name"',
        '<input class="uk-input" type="text" id="full-name" name="full-name" autocomplete="name"',
        content
    )
    content = re.sub(
        r'<input class="uk-input" type="email" id="email" name="email"',
        '<input class="uk-input" type="email" id="email" name="email" autocomplete="email"',
        content
    )
    content = re.sub(
        r'<input class="uk-input" type="tel" id="phone" name="phone"',
        '<input class="uk-input" type="tel" id="phone" name="phone" autocomplete="tel"',
        content
    )
    
    # 4. Fix Label in Name (2.5.3) - aria-label should contain visible text
    content = re.sub(
        r'aria-label="Open a new trading account"',
        'aria-label="Open Account - Open a new trading account"',
        content
    )
    content = re.sub(
        r'aria-label="Transfer funds securely"',
        'aria-label="Fund Transfer - Transfer funds securely"',
        content
    )
    content = re.sub(
        r'aria-label="Access online trading portal"',
        'aria-label="Online Trading - Access online trading portal"',
        content
    )
    content = re.sub(
        r'aria-label="Access back office system"',
        'aria-label="Back Office - Access back office system"',
        content
    )
    
    # 5. Add Unique Page Title (2.4.2)
    content = re.sub(
        r'<title>Standard Securities & Investment Intermediates Ltd</title>',
        '<title>Home | Standard Securities & Investment Intermediates Ltd</title>',
        content
    )
    
    # 6. Fix Form Validation (3.3.1, 3.3.2) - Add required attributes and aria-required
    content = re.sub(
        r'<input class="uk-input" type="text" id="full-name" name="full-name" autocomplete="name">',
        '<input class="uk-input" type="text" id="full-name" name="full-name" autocomplete="name" required aria-required="true">',
        content
    )
    content = re.sub(
        r'<input class="uk-input" type="email" id="email" name="email" autocomplete="email">',
        '<input class="uk-input" type="email" id="email" name="email" autocomplete="email" required aria-required="true">',
        content
    )
    content = re.sub(
        r'<input class="uk-input" type="tel" id="phone" name="phone" autocomplete="tel">',
        '<input class="uk-input" type="tel" id="phone" name="phone" autocomplete="tel" required aria-required="true">',
        content
    )
    
    # Add visible required indicator to labels
    content = re.sub(
        r'<label class="uk-form-label" for="full-name">Full Name</label>',
        '<label class="uk-form-label" for="full-name">Full Name <span aria-hidden="true" style="color: #d32f2f;">*</span></label>',
        content
    )
    content = re.sub(
        r'<label class="uk-form-label" for="email">Email Address</label>',
        '<label class="uk-form-label" for="email">Email Address <span aria-hidden="true" style="color: #d32f2f;">*</span></label>',
        content
    )
    content = re.sub(
        r'<label class="uk-form-label" for="phone">Phone Number</label>',
        '<label class="uk-form-label" for="phone">Phone Number <span aria-hidden="true" style="color: #d32f2f;">*</span></label>',
        content
    )
    
    # 7. Fix Hindi Language Toggle (3.1.2) - Add working implementation
    # Find the setLanguage function and enhance it
    old_lang_func = r"function setLanguage\(lang\) \{[^}]+\}"
    new_lang_func = '''function setLanguage(lang) {
        var translations = {
            'en': {
                'Welcome': 'Welcome',
                'Invest Now': 'Invest Now',
                'Learn More': 'Learn More',
                'Contact Us': 'Contact Us',
                'Products': 'Products',
                'About Us': 'About Us'
            },
            'hi': {
                'Welcome': 'स्वागत है',
                'Invest Now': 'अभी निवेश करें',
                'Learn More': 'और जानें',
                'Contact Us': 'संपर्क करें',
                'Products': 'उत्पाद',
                'About Us': 'हमारे बारे में'
            }
        };
        
        var currentTrans = translations[lang] || translations['en'];
        
        // Update button states
        document.getElementById('lang-en').setAttribute('aria-pressed', lang === 'en' ? 'true' : 'false');
        document.getElementById('lang-hi').setAttribute('aria-pressed', lang === 'hi' ? 'true' : 'false');
        
        // Update button active states
        document.getElementById('lang-en').classList.toggle('active', lang === 'en');
        document.getElementById('lang-hi').classList.toggle('active', lang === 'hi');
        
        // Set document language
        document.documentElement.lang = lang;
        
        // Translate data-translate elements
        document.querySelectorAll('[data-translate]').forEach(function(el) {
            var key = el.getAttribute('data-translate');
            if (currentTrans[key]) {
                el.textContent = currentTrans[key];
            }
        });
        
        // Store preference
        localStorage.setItem('preferredLanguage', lang);
        
        // Dispatch event for other components
        window.dispatchEvent(new CustomEvent('languageChanged', { detail: { language: lang } }));
    }'''
    content = re.sub(old_lang_func, new_lang_func, content)
    
    # 8. Add Google Maps iframe title (4.1.2)
    content = re.sub(
        r'<iframe[^>]*src="https://www.google.com/maps/embed[^"]*"[^>]*></iframe>',
        '<iframe title="Map showing our office location" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3770.956895743923!2d72.82543231490118!3d19.01779798710037!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7cf21727f6e19%3A0x0!2zMTnCsDAxJzA2LjEiTiA3MsKwNDknMzEuNSJF!5e0!3m2!1sen!2sin!4v1621234567890!5m2!1sen!2sin" width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed index.html")


def fix_contact_html():
    """Fix accessibility issues in contact.html"""
    filepath = '/workspace/standardsec_files/contact.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add Unique Page Title (2.4.2)
    content = re.sub(
        r'<title>Standard Securities & Investment Intermediates Ltd</title>',
        '<title>Contact Us | Standard Securities & Investment Intermediates Ltd</title>',
        content
    )
    
    # Add autocomplete attributes to contact form (1.3.5)
    content = re.sub(
        r'<input class="uk-input" id="name" name="name" type="text"',
        '<input class="uk-input" id="name" name="name" type="text" autocomplete="name"',
        content
    )
    content = re.sub(
        r'<input class="uk-input" id="email" name="email" type="email"',
        '<input class="uk-input" id="email" name="email" type="email" autocomplete="email"',
        content
    )
    content = re.sub(
        r'<input class="uk-input" id="phone" name="phone" type="tel"',
        '<input class="uk-input" id="phone" name="phone" type="tel" autocomplete="tel"',
        content
    )
    content = re.sub(
        r'<textarea class="uk-textarea" id="message" name="message"',
        '<textarea class="uk-textarea" id="message" name="message" autocomplete="off"',
        content
    )
    
    # Add aria-required attributes (3.3.1, 3.3.2)
    content = re.sub(
        r'<input class="uk-input" id="name"[^>]*required>',
        '<input class="uk-input" id="name" name="name" type="text" placeholder="Enter your full name" autocomplete="name" required aria-required="true">',
        content
    )
    content = re.sub(
        r'<input class="uk-input" id="email"[^>]*required>',
        '<input class="uk-input" id="email" name="email" type="email" placeholder="Enter your email address" autocomplete="email" required aria-required="true">',
        content
    )
    content = re.sub(
        r'<textarea class="uk-textarea" id="message"[^>]*required>',
        '<textarea class="uk-textarea" id="message" name="message" placeholder="Enter your message" autocomplete="off" required aria-required="true">',
        content
    )
    
    # Fix Google Maps iframe title (4.1.2)
    content = re.sub(
        r'<iframe[^>]*src="https://www.google.com/maps/embed[^"]*"[^>]*></iframe>',
        '<iframe title="Map showing our office location" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3770.956895743923!2d72.82543231490118!3d19.01779798710037!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7cf21727f6e19%3A0x0!2zMTnCsDAxJzA2LjEiTiA3MsKwNDknMzEuNSJF!5e0!3m2!1sen!2sin!4v1621234567890!5m2!1sen!2sin" width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed contact.html")


def fix_css():
    """Fix CSS accessibility issues"""
    filepath = '/workspace/standardsec_files/css/style.css'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix Color Contrast (1.4.3, 1.4.11)
    # Improve footer contrast - #8f8f8f to #666666 (4.5:1 on white)
    content = re.sub(r'#8f8f8f', '#666666', content)
    
    # 2. Fix Text Spacing Clipping (1.4.12) - Remove fixed heights
    # Add overrides for WCAG text spacing
    content += '''
/* WCAG 2.2 Text Spacing Override (1.4.12) */
.uk-section-secondary, .uk-card-body {
    /* Allow content to grow with text spacing overrides */
    overflow: visible !important;
}

/* Service card headings - remove fixed heights */
.in-tile-service .uk-card-body {
    min-height: auto !important;
    height: auto !important;
}

/* Stat headings with labels */
.stat-label {
    font-size: 0.6em !important;
    font-weight: 400 !important;
}
'''
    
    # 3. Fix Focus Indicators (2.4.7) - Add visible focus styles
    content += '''
/* WCAG 2.4.7 - Visible Focus Indicators */
a:focus, button:focus, input:focus, select:focus, textarea:focus, 
.uk-button:focus, .uk-input:focus, .uk-select:focus, .uk-textarea:focus {
    outline: 3px solid #012c6d !important;
    outline-offset: 2px !important;
}

/* High contrast focus for interactive elements */
.uk-icon-button:focus, .uk-totop:focus {
    outline: 3px solid #f0b429 !important;
    outline-offset: 2px !important;
}

/* Form focus states */
.uk-input:focus, .uk-textarea:focus {
    border-color: #012c6d !important;
    box-shadow: 0 0 0 2px rgba(1, 44, 109, 0.2) !important;
}
'''
    
    # 4. Fix Target Size (2.5.8) - Increase to 44x44px minimum
    content += '''
/* WCAG 2.5.8 - Target Size Minimum (44x44px) */
footer a, footer .uk-list li a, footer .uk-subnav li a,
.in-footer-info a, .in-footer-socials a,
.skip-link,
.uk-icon-button, .uk-totop a {
    min-height: 44px !important;
    min-width: 44px !important;
    padding: 10px 12px !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
}

/* Footer links specific */
footer .uk-list li {
    display: flex !important;
}

footer .uk-list li a {
    flex: 1 !important;
}

/* Social media buttons */
.in-footer-socials .uk-icon-button {
    width: 44px !important;
    height: 44px !important;
}

/* Navigation links */
.uk-navbar-nav li a {
    min-height: 44px !important;
    padding: 0 15px !important;
}

/* Form buttons */
.uk-button {
    min-height: 44px !important;
    min-width: 44px !important;
}

/* UKITS toggle */
[data-uk-toggle] {
    min-height: 44px !important;
    min-width: 44px !important;
}
'''
    
    # 5. Improve contrast for specific elements
    content += '''
/* WCAG 1.4.3 - Contrast improvements for text */
/* Hero section text */
.uk-hero-overlay h1, .uk-hero-overlay h2, 
.uk-slideshow-items h1, .uk-slideshow-items h2 {
    color: #ffffff !important;
}

/* Hero CTA button - increase contrast */
.uk-button-primary {
    background-color: #012c6d !important;
    color: #ffffff !important;
}

/* Footer text contrast */
footer, footer p, footer li, footer span {
    color: #666666 !important;
}

footer h3, footer h4 {
    color: #333333 !important;
}

/* Price ticker badges */
.uk-label {
    color: #ffffff !important;
    background-color: #333333 !important;
}

/* Required field indicators */
.uk-text-danger {
    color: #d32f2f !important;
}
'''
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed style.css")


def fix_about_html():
    """Fix about.html page title"""
    filepath = '/workspace/standardsec_files/about.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'<title>Standard Securities & Investment Intermediates Ltd</title>',
        '<title>About Us | Standard Securities & Investment Intermediates Ltd</title>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed about.html")


def fix_accessibility_html():
    """Fix accessibility.html page title"""
    filepath = '/workspace/standardsec_files/accessibility.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'<title>Standard Securities & Investment Intermediates Ltd</title>',
        '<title>Accessibility Statement | Standard Securities & Investment Intermediates Ltd</title>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed accessibility.html")


def fix_products_html():
    """Fix products.html page title and other issues"""
    filepath = '/workspace/standardsec_files/products.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'<title>Standard Securities & Investment Intermediates Ltd</title>',
        '<title>Products & Services | Standard Securities & Investment Intermediates Ltd</title>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed products.html")


def fix_complaint_new_html():
    """Fix complaint_new.html page title"""
    filepath = '/workspace/standardsec_files/complaint_new.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'<title>Standard Securities & Investment Intermediates Ltd</title>',
        '<title>Complaints | Standard Securities & Investment Intermediates Ltd</title>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed complaint_new.html")


def add_carousel_pause():
    """Add pause control to carousel (2.2.2)"""
    filepath = '/workspace/standardsec_files/index.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add pause button before carousel
    content = re.sub(
        r'<div uk-slider="autoplay: true">',
        '''<div class="carousel-controls" style="text-align: center; padding: 10px 0;">
            <button type="button" class="uk-button uk-button-small uk-button-primary" 
                    onclick="toggleCarouselAutoplay()" id="carousel-pause-btn"
                    aria-label="Pause automatic slide advancement">
                <span id="pause-icon"><i class="fas fa-pause"></i></span>
                <span id="play-icon" style="display: none;"><i class="fas fa-play"></i></span>
                <span id="pause-text">Pause</span>
            </button>
        </div>
        <div uk-slider="autoplay: true">''',
        content
    )
    
    # Add JavaScript for pause control before closing </body>
    pause_js = '''
<script>
// WCAG 2.2.2 - Carousel Pause Control
var carouselPaused = false;

function toggleCarouselAutoplay() {
    var sliderElement = document.querySelector('[uk-slider]');
    var pauseBtn = document.getElementById('carousel-pause-btn');
    var pauseIcon = document.getElementById('pause-icon');
    var playIcon = document.getElementById('play-icon');
    var pauseText = document.getElementById('pause-text');
    
    carouselPaused = !carouselPaused;
    
    if (carouselPaused) {
        // Pause the slider
        sliderElement.setAttribute('autoplay', 'false');
        pauseIcon.style.display = 'none';
        playIcon.style.display = 'inline';
        pauseText.textContent = 'Play';
        pauseBtn.setAttribute('aria-label', 'Resume automatic slide advancement');
        pauseBtn.setAttribute('aria-pressed', 'true');
    } else {
        // Resume autoplay
        sliderElement.setAttribute('autoplay', 'true');
        pauseIcon.style.display = 'inline';
        playIcon.style.display = 'none';
        pauseText.textContent = 'Pause';
        pauseBtn.setAttribute('aria-label', 'Pause automatic slide advancement');
        pauseBtn.setAttribute('aria-pressed', 'false');
    }
}

// Ensure keyboard accessibility for carousel dots
document.addEventListener('DOMContentLoaded', function() {
    var dots = document.querySelectorAll('.uk-slider-items .uk-dotnav button');
    dots.forEach(function(dot, index) {
        dot.setAttribute('aria-label', 'Slide ' + (index + 1));
        dot.setAttribute('role', 'tab');
    });
});
</script>
'''
    content = content.replace('</body>', pause_js + '</body>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Added carousel pause control")


def main():
    print("Starting WCAG 2.2 Accessibility Fixes...")
    print("=" * 50)
    
    fix_index_html()
    fix_contact_html()
    fix_css()
    fix_about_html()
    fix_accessibility_html()
    fix_products_html()
    fix_complaint_new_html()
    add_carousel_pause()
    
    print("=" * 50)
    print("All accessibility fixes completed!")


if __name__ == '__main__':
    main()
