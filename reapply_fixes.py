#!/usr/bin/env python3
"""
Re-apply accessibility fixes after resolving conflicts
"""

import re

def fix_index_html():
    filepath = '/workspace/standardsec_files/index.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix skip link - use #main-content
    content = re.sub(
        r'<a href="#maincontent" class="skip-link">',
        '<a href="#main-content" class="skip-link">',
        content
    )
    
    # 2. Fix hero section - change h1 to h2 and add visually hidden h1
    # "Setting strong" should be h2
    content = re.sub(
        r'<h1 class="uk-margin-remove-bottom" style="font-size: 1rem; font-weight: 400; color: #ffffff;">Setting strong</h1>',
        '<h2 class="uk-margin-remove-bottom" style="font-size: 1rem; font-weight: 400; color: #ffffff;">Setting strong</h2>',
        content
    )
    content = re.sub(
        r'<p class="uk-margin-remove-top" style="font-size: 2\.5rem; font-weight: 700; color: #ffffff; line-height: 1\.2;">foundations</p>',
        '<p class="uk-margin-remove-top" style="font-size: 2.5rem; font-weight: 700; color: #ffffff; line-height: 1.2;">foundations</p>',
        content
    )
    
    # "Start investing now" should be h2
    content = re.sub(
        r'<h1 class="uk-margin-remove-bottom" style="font-size: 2\.5rem; font-weight: 700; color: #ffffff;">Start investing now</h1>',
        '<h2 class="uk-margin-remove-bottom" style="font-size: 2.5rem; font-weight: 700; color: #ffffff;">Start investing now</h2>',
        content
    )
    
    # 3. Add visually hidden H1 before Features Section
    content = re.sub(
        r'(<!-- Features Section -->\s*<div class="uk-section">)',
        '\\1\n                <h1 class="uk-visually-hidden">Standard Securities & Investment Intermediates Ltd - Trading Platform</h1>',
        content
    )
    
    # 4. Fix service card headings - add style
    for service in ['Currency', 'Commodities', 'Equity', 'IPOs', 'Advisory', 'Depository']:
        content = re.sub(
            rf'<h3 class="uk-margin-small-top">{service}</h3>',
            f'<h3 class="uk-margin-small-top" style="font-size: 1.25rem; font-weight: 600;">{service}</h3>',
            content
        )
    
    # 5. Add aria-required to form fields
    content = re.sub(
        r'(<input[^>]*id="full-name"[^>]*)(>)',
        '\\1 required aria-required="true"\\2',
        content
    )
    content = re.sub(
        r'(<input[^>]*id="email"[^>]*)(>)',
        '\\1 required aria-required="true"\\2',
        content
    )
    content = re.sub(
        r'(<input[^>]*id="phone"[^>]*)(>)',
        '\\1 required aria-required="true"\\2',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed index.html")


def fix_contact_html():
    filepath = '/workspace/standardsec_files/contact.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add visible form labels
    content = re.sub(
        r'<div class="uk-margin uk-width-1-1">\s*<input class="uk-input" id="name"',
        '''<div class="uk-margin uk-width-1-1">
            <label for="name" class="uk-form-label">Full Name <span aria-hidden="true" style="color: #d32f2f;">*</span></label>
            <input class="uk-input" id="name"''',
        content
    )
    
    content = re.sub(
        r'<div class="uk-margin uk-width-1-1">\s*<input class="uk-input" id="email"',
        '''<div class="uk-margin uk-width-1-1">
            <label for="email" class="uk-form-label">Email Address <span aria-hidden="true" style="color: #d32f2f;">*</span></label>
            <input class="uk-input" id="email"''',
        content
    )
    
    content = re.sub(
        r'<div class="uk-margin uk-width-1-1">\s*<textarea class="uk-textarea" id="message"',
        '''<div class="uk-margin uk-width-1-1">
            <label for="message" class="uk-form-label">Message <span aria-hidden="true" style="color: #d32f2f;">*</span></label>
            <textarea class="uk-textarea" id="message"''',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed contact.html")


if __name__ == '__main__':
    fix_index_html()
    fix_contact_html()
    print("\nAccessibility fixes re-applied!")
