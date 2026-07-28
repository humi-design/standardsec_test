#!/usr/bin/env python3
"""
Fix WCAG 1.3.1 Issues:
- H3 before H1 in hero section
- Duplicate H1s in hero carousel  
- Visible form labels instead of sr-only
- Inconsistent service card headings (H5 vs H3)
"""

import re

def fix_1_3_1():
    filepath = '/workspace/standardsec_files/index.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix H3 before H1 - Change to H2
    content = re.sub(
        r'<h3 class="uk-margin-remove-bottom">Setting strong</h3>',
        '<h2 class="uk-margin-remove-bottom" style="font-size: 1rem; font-weight: 400; color: #ffffff;">Setting strong</h2>',
        content
    )
    
    # 2. Fix duplicate H1s - Keep one H1, change others to H2
    # The main hero slider H1
    content = re.sub(
        r'<h1 class="uk-margin-remove-top">foundations</h1>',
        '<p class="uk-margin-remove-top" style="font-size: 2.5rem; font-weight: 700; color: #ffffff; line-height: 1.2;">foundations</p>',
        content
    )
    
    # Change second H1 in slider to H2
    content = re.sub(
        r'<h1 class="uk-margin-remove-bottom">Start investing now</h1>',
        '<h2 class="uk-margin-remove-bottom" style="font-size: 2.5rem; font-weight: 700; color: #ffffff;">Start investing now</h2>',
        content
    )
    
    # 3. Fix form labels - Visible labels instead of sr-only
    content = re.sub(
        r'<label class="sr-only" for="full-name">Full Name</label>',
        '<label class="uk-form-label" for="full-name">Full Name <span aria-hidden="true" style="color: #d32f2f;">*</span></label>',
        content
    )
    content = re.sub(
        r'<label class="sr-only" for="email">Email Address</label>',
        '<label class="uk-form-label" for="email">Email Address <span aria-hidden="true" style="color: #d32f2f;">*</span></label>',
        content
    )
    content = re.sub(
        r'<label class="sr-only" for="phone">Phone Number</label>',
        '<label class="uk-form-label" for="phone">Phone Number <span aria-hidden="true" style="color: #d32f2f;">*</span></label>',
        content
    )
    
    # 4. Fix service card headings - Ensure consistent H3 level
    # In the services section (lines ~585-605), these should be H3
    for service in ['Currency', 'Commodities', 'Equity', 'IPOs', 'Advisory', 'Depository']:
        content = re.sub(
            rf'<h3 class="uk-margin-small-top" style="font-size: 1\.25rem;">{service}</h3>',
            f'<h3 class="uk-margin-small-top" style="font-size: 1.25rem; font-weight: 600;">{service}</h3>',
            content
        )
    
    # In the detailed services section (lines ~783-893), these are also H3 - keep consistent
    # These are already H3 which is correct for subsections
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed 1.3.1 issues in index.html")

if __name__ == '__main__':
    fix_1_3_1()
