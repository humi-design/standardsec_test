#!/usr/bin/env python3
"""
Complete WCAG 2.2 Accessibility Fix Script
Fixes all issues in the feature/custom-hindi-language branch
"""

import re
import os

def fix_all():
    print("Applying all accessibility fixes...")
    
    # Fix index.html
    fix_index_html()
    
    # Fix other HTML pages
    fix_other_pages()
    
    # Fix CSS
    fix_css()
    
    print("All fixes applied!")

def fix_index_html():
    filepath = '/workspace/standardsec_files/index.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix Skip Link Visibility (2.4.1)
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
    
    # Fix H5 service headings to H3
    for heading in ['Currency', 'Commodities', 'Equity', 'IPOs', 'Advisory', 'Depository']:
        content = re.sub(
            rf'<h5 class="uk-margin-small-top">{heading}</h5>',
            f'<h3 class="uk-margin-small-top" style="font-size: 1.25rem;">{heading}</h3>',
            content
        )
    
    # Fix non-descriptive stat headings
    stats = [
        ('#1', 'Ranking in India'),
        ('~30ms', 'Execution Speed'),
        ('24/5', 'Trading Days'),
        ('0.0', 'Penalty Charges'),
        ('150+', 'Products Available')
    ]
    for stat, label in stats:
        content = re.sub(
            rf'<h2 class="uk-margin-remove-bottom">{re.escape(stat)}</h2>',
            f'<h2 class="uk-margin-remove-bottom"><span class="stat-value">{stat}</span><span class="stat-label" style="display: block; font-size: 0.6em; font-weight: 400;">{label}</span></h2>',
            content
        )
    
    # Add aria-required and autocomplete to form fields
    content = re.sub(
        r'<input class="uk-input" type="text" id="full-name"',
        '<input class="uk-input" type="text" id="full-name" autocomplete="name" required aria-required="true"',
        content
    )
    content = re.sub(
        r'<input class="uk-input" type="email" id="email"',
        '<input class="uk-input" type="email" id="email" autocomplete="email" required aria-required="true"',
        content
    )
    content = re.sub(
        r'<input class="uk-input" type="tel" id="phone"',
        '<input class="uk-input" type="tel" id="phone" autocomplete="tel" required aria-required="true"',
        content
    )
    
    # Add required indicators to labels
    for field in ['full-name', 'email', 'phone']:
        label_map = {
            'full-name': 'Full Name',
            'email': 'Email Address', 
            'phone': 'Phone Number'
        }
        content = re.sub(
            rf'<label class="uk-form-label" for="{field}">{label_map[field]}</label>',
            f'<label class="uk-form-label" for="{field}">{label_map[field]} <span aria-hidden="true" style="color: #d32f2f;">*</span></label>',
            content
        )
    
    # Fix aria-label to contain visible text (2.5.3)
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
    
    # Add unique page title (2.4.2)
    content = re.sub(
        r'<title>Standard Securities & Investment Intermediates Ltd\.</title>',
        '<title>Home | Standard Securities & Investment Intermediates Ltd.</title>',
        content
    )
    
    # Add aria-expanded to mobile nav toggle (4.1.2)
    content = re.sub(
        r'<button class="uk-button" type="button" aria-label="Open mobile navigation menu" onclick="UIkit\.toggle\(document\.getElementById\(\'mobile-nav-modal\'\)\)\.toggle\(\);" data-uk-toggle >',
        '<button class="uk-button" type="button" aria-label="Open mobile navigation menu" aria-expanded="false" onclick="UIkit.toggle(document.getElementById(\'mobile-nav-modal\')).toggle();" data-uk-toggle >',
        content
    )
    
    # Add Google Maps iframe title (4.1.2)
    content = re.sub(
        r'<iframe([^>]*)src="https://www\.google\.com/maps/embed([^"]*)"([^>]*)></iframe>',
        '<iframe title="Map showing our office location" \\1src="https://www.google.com/maps/embed\\2"\\3></iframe>',
        content
    )
    
    # Add carousel pause control (2.2.2)
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
    
    # Add carousel pause JS
    pause_js = '''
<script>
var carouselPaused = false;
function toggleCarouselAutoplay() {
    var sliderElement = document.querySelector('[uk-slider]');
    var pauseBtn = document.getElementById('carousel-pause-btn');
    var pauseIcon = document.getElementById('pause-icon');
    var playIcon = document.getElementById('play-icon');
    var pauseText = document.getElementById('pause-text');
    
    carouselPaused = !carouselPaused;
    
    if (carouselPaused) {
        sliderElement.setAttribute('autoplay', 'false');
        pauseIcon.style.display = 'none';
        playIcon.style.display = 'inline';
        pauseText.textContent = 'Play';
        pauseBtn.setAttribute('aria-label', 'Resume automatic slide advancement');
        pauseBtn.setAttribute('aria-pressed', 'true');
    } else {
        sliderElement.setAttribute('autoplay', 'true');
        pauseIcon.style.display = 'inline';
        playIcon.style.display = 'none';
        pauseText.textContent = 'Pause';
        pauseBtn.setAttribute('aria-label', 'Pause automatic slide advancement');
        pauseBtn.setAttribute('aria-pressed', 'false');
    }
}
</script>
'''
    content = content.replace('</body>', pause_js + '</body>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed index.html")

def fix_other_pages():
    """Add unique page titles to all HTML pages"""
    page_titles = {
        'about.html': 'About Us | Standard Securities & Investment Intermediates Ltd.',
        'accessibility.html': 'Accessibility Statement | Standard Securities & Investment Intermediates Ltd.',
        'products.html': 'Products & Services | Standard Securities & Investment Intermediates Ltd.',
        'contact.html': 'Contact Us | Standard Securities & Investment Intermediates Ltd.',
        'complaint_new.html': 'Complaints | Standard Securities & Investment Intermediates Ltd.',
        'careers.html': 'Careers | Standard Securities & Investment Intermediates Ltd.',
        'customers.html': 'Our Customers | Standard Securities & Investment Intermediates Ltd.',
        'disclaimer.html': 'Disclaimer | Standard Securities & Investment Intermediates Ltd.',
        'downloads.html': 'Downloads | Standard Securities & Investment Intermediates Ltd.',
        'history.html': 'Our History | Standard Securities & Investment Intermediates Ltd.',
        'management.html': 'Management Team | Standard Securities & Investment Intermediates Ltd.',
        'news.html': 'News & Updates | Standard Securities & Investment Intermediates Ltd.',
        'privacy.html': 'Privacy Policy | Standard Securities & Investment Intermediates Ltd.',
        'procedures.html': 'Policies & Procedures | Standard Securities & Investment Intermediates Ltd.',
        'signin.html': 'Sign In | Standard Securities & Investment Intermediates Ltd.',
        'team.html': 'Our Team | Standard Securities & Investment Intermediates Ltd.',
        'Commodities.html': 'Commodities Trading | Standard Securities & Investment Intermediates Ltd.',
        'Currency.html': 'Currency Trading | Standard Securities & Investment Intermediates Ltd.',
        'Equity.html': 'Equity Trading | Standard Securities & Investment Intermediates Ltd.',
        'IPOs.html': 'IPO Services | Standard Securities & Investment Intermediates Ltd.',
        'Depository.html': 'Depository Services | Standard Securities & Investment Intermediates Ltd.',
        'Advisory.html': 'Advisory Services | Standard Securities & Investment Intermediates Ltd.',
        'Terms.html': 'Terms of Service | Standard Securities & Investment Intermediates Ltd.',
    }
    
    for filename, title in page_titles.items():
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = re.sub(
                r'<title>Standard Securities & Investment Intermediates Ltd\.</title>',
                f'<title>{title}</title>',
                content
            )
            
            if new_content != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed: {filename}")

def fix_css():
    """Fix CSS accessibility issues"""
    css_path = '/workspace/standardsec_files/css/style.css'
    
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix footer color contrast
        content = re.sub(r'#8f8f8f', '#666666', content)
        
        # Add focus indicators
        if ':focus' not in content or 'outline' not in content:
            content += '''
/* WCAG 2.4.7 - Visible Focus Indicators */
a:focus, button:focus, input:focus, select:focus, textarea:focus {
    outline: 3px solid #012c6d !important;
    outline-offset: 2px !important;
}
'''
        
        # Add target sizes
        if 'min-height: 44px' not in content:
            content += '''
/* WCAG 2.5.8 - Target Size Minimum (44x44px) */
footer a, footer .uk-list li a, footer .uk-subnav li a,
.in-footer-info a, .in-footer-socials a, .skip-link {
    min-height: 44px !important;
    min-width: 44px !important;
    padding: 10px 12px !important;
}
'''
        
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("Fixed CSS")
    else:
        # Create CSS directory and file
        os.makedirs('/workspace/standardsec_files/css', exist_ok=True)
        css_content = '''/* WCAG 2.2 Accessibility Fixes */

/* Skip Link */
.skip-link {
    position: absolute;
    left: -9999px;
    top: auto;
    width: 1px;
    height: 1px;
    overflow: hidden;
}
.skip-link:focus {
    position: fixed !important;
    top: 10px;
    left: 10px !important;
    width: auto;
    height: auto;
    clip: auto !important;
}

/* Focus Indicators (2.4.7) */
a:focus, button:focus, input:focus, select:focus, textarea:focus {
    outline: 3px solid #012c6d !important;
    outline-offset: 2px !important;
}

/* Target Size (2.5.8) */
footer a, footer li a, .skip-link, .uk-icon-button {
    min-height: 44px !important;
    min-width: 44px !important;
    padding: 10px 12px !important;
}

/* Color Contrast (1.4.3) */
footer, footer p, footer li {
    color: #666666 !important;
}
footer h3 {
    color: #333333 !important;
}
'''
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(css_content)
        
        print("Created CSS file")

if __name__ == '__main__':
    fix_all()
