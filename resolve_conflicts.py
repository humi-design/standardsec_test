#!/usr/bin/env python3
"""
Resolve merge conflicts in index.html, contact.html, and css/style.css
Keep the best version from HEAD (accessibility fixes)
"""

import re

def resolve_index_html():
    filepath = '/workspace/standardsec_files/index.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Conflict 1: Skip link href - keep HEAD (#main-content)
    content = re.sub(
        r'<<<<<<< HEAD\n\n    <a href="#main-content" class="skip-link">Skip to main content</a>\n=======\n\n    <a href="#maincontent" class="skip-link">Skip to main content</a>\n>>>>>>> origin/main',
        '\n\n    <a href="#main-content" class="skip-link">Skip to main content</a>\n',
        content
    )
    
    # Conflict 2: "Setting strong" heading - keep HEAD
    content = re.sub(
        r'<<<<<<< HEAD\n                                            <h2 class="uk-margin-remove-bottom" style="font-size: 1rem; font-weight: 400; color: #ffffff;">Setting strong</h2>\n                                            <p class="uk-margin-remove-top" style="font-size: 2.5rem; font-weight: 700; color: #ffffff; line-height: 1.2;">foundations</p>\n=======\n                                            <h2 class="uk-margin-remove-bottom" style="color: #ffffff; font-size: 1rem; font-weight: 400;">Setting strong</h2>\n                                            <p class="uk-margin-remove-top" style="color: #ffffff; font-size: 2.5rem; font-weight: 700; margin-bottom: 0;">foundations</p>\n>>>>>>> origin/main',
        '\n                                            <h2 class="uk-margin-remove-bottom" style="font-size: 1rem; font-weight: 400; color: #ffffff;">Setting strong</h2>\n                                            <p class="uk-margin-remove-top" style="font-size: 2.5rem; font-weight: 700; color: #ffffff; line-height: 1.2;">foundations</p>\n',
        content
    )
    
    # Conflict 3: "Start investing now" heading - keep HEAD
    content = re.sub(
        r'<<<<<<< HEAD\n                                        <h2 class="uk-margin-remove-bottom" style="font-size: 2.5rem; font-weight: 700; color: #ffffff;">Start investing now</h2>\n=======\n                                        <h2 class="uk-margin-remove-bottom" style="color: #ffffff; font-size: 2.5rem; font-weight: 700;">Start investing now</h2>\n>>>>>>> origin/main',
        '\n                                        <h2 class="uk-margin-remove-bottom" style="font-size: 2.5rem; font-weight: 700; color: #ffffff;">Start investing now</h2>\n',
        content
    )
    
    # Conflict 4: Full Name field - keep HEAD (with required)
    content = re.sub(
        r'<<<<<<< HEAD\n              <input class="uk-input" type="text" id="full-name" autocomplete="name" required aria-required="true" name="full-name"\n                placeholder="Full name" aria-label="Full name">\n=======\n              <input class="uk-input" type="text" id="full-name" name="full-name" autocomplete="name"\n                placeholder="Enter your full name" aria-label="Full name">\n>>>>>>> origin/main',
        '\n              <input class="uk-input" type="text" id="full-name" name="full-name" autocomplete="name" required aria-required="true"\n                placeholder="Enter your full name" aria-label="Full name">\n',
        content
    )
    
    # Conflict 5: Email field - keep HEAD (with required)
    content = re.sub(
        r'<<<<<<< HEAD\n              <input class="uk-input" type="email" id="email" autocomplete="email" required aria-required="true" name="email"\n                placeholder="Email address" aria-label="Email address">\n=======\n              <input class="uk-input" type="email" id="email" name="email" autocomplete="email"\n                placeholder="Enter your email address" aria-label="Email address">\n>>>>>>> origin/main',
        '\n              <input class="uk-input" type="email" id="email" name="email" autocomplete="email" required aria-required="true"\n                placeholder="Enter your email address" aria-label="Email address">\n',
        content
    )
    
    # Conflict 6: Phone field - keep HEAD (with required)
    content = re.sub(
        r'<<<<<<< HEAD\n              <input class="uk-input" type="tel" id="phone" autocomplete="tel" required aria-required="true" name="phone"\n                placeholder="Phone number" aria-label="Phone number">\n=======\n              <input class="uk-input" type="tel" id="phone" name="phone" autocomplete="tel"\n                placeholder="Enter your phone number" aria-label="Phone number">\n>>>>>>> origin/main',
        '\n              <input class="uk-input" type="tel" id="phone" name="phone" autocomplete="tel" required aria-required="true"\n                placeholder="Enter your phone number" aria-label="Phone number">\n',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Resolved index.html conflicts")


def resolve_contact_html():
    filepath = '/workspace/standardsec_files/contact.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove any remaining conflict markers
    content = re.sub(r'<<<<<<< HEAD\n', '', content)
    content = re.sub(r'=======\n', '', content)
    content = re.sub(r'>>>>>>> origin/main\n', '', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Resolved contact.html conflicts")


def resolve_css():
    filepath = '/workspace/standardsec_files/css/style.css'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove any conflict markers and keep both versions merged
    # Remove HEAD section markers
    content = re.sub(r'<<<<<<< HEAD\n', '', content)
    content = re.sub(r'=======\n', '\n', content)
    content = re.sub(r'>>>>>>> origin/main\n', '', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Resolved css/style.css conflicts")


if __name__ == '__main__':
    resolve_index_html()
    resolve_contact_html()
    resolve_css()
    print("\nAll conflicts resolved!")
