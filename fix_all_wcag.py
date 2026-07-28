#!/usr/bin/env python3
"""
Fix ALL remaining WCAG 2.2 failures
"""

import re
import os

def fix_all():
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # 1.4.11 - Fix form input borders contrast
        content = re.sub(
            r'class="uk-input"',
            'class="uk-input" style="border-color: #666;"',
            content
        )
        content = re.sub(
            r'class="uk-textarea"',
            'class="uk-textarea" style="border-color: #666;"',
            content
        )
        
        # 2.4.7 - Fix focus visibility on buttons
        content = re.sub(
            r'(uk-button-primary[^"]*)',
            '\\1 style="outline: 2px solid #0066cc; outline-offset: 2px;"',
            content
        )
        
        # 2.5.8 - Fix target sizes (min 44x44)
        content = re.sub(
            r'(uk-button[^>]*)>',
            '\\1 style="min-height: 44px; min-width: 44px; padding: 10px 20px;">',
            content
        )
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {filepath}")


if __name__ == '__main__':
    fix_all()
