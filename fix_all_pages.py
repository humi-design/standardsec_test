#!/usr/bin/env python3
"""
Fix WCAG 1.3.1 issues across ALL HTML pages:
1. Multiple H1s - Keep one, change others to H2
2. Missing H1 - Add visually hidden H1
3. Heading hierarchy issues
4. Form labels
"""

import re
import os

def fix_all_pages():
    files_to_fix = [
        'contact.html',
        'history.html', 
        'careers.html',
        'news.html',
        'signin.html',
        'single.html',
        'complaint.html',
        'customers.html',
        'team.html',
        'about.html',
        'management.html',
        'products.html',
        'accessibility.html',
        'downloads.html',
        'procedures.html',
        'invester_charter.html',
        'privacy.html',
        'disclaimer.html',
        'Terms.html',
        'Advisory.html',
        'Commodities.html',
        'Currency.html',
        'Depository.html',
        'Equity.html',
        'IPOs.html',
        'pay.html',
        '404.html',
    ]
    
    for filename in files_to_fix:
        if os.path.exists(filename):
            fix_page(filename)
    
    print("All pages fixed!")

def fix_page(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # 1. Fix duplicate H1s - change second H1 to H2
    h1_matches = list(re.finditer(r'<h1[^>]*>([^<]+)</h1>', content))
    if len(h1_matches) > 1:
        # Keep first H1, change rest to H2
        for match in h1_matches[1:]:
            old_h1 = match.group(0)
            inner_text = match.group(1)
            # Preserve any classes from the h1 tag
            class_match = re.search(r'class="([^"]*)"', old_h1)
            classes = class_match.group(1) if class_match else ''
            new_tag = f'<h2 class="{classes}">' if classes else '<h2>'
            new_h2 = f'{new_tag}{inner_text}</h2>'
            content = content.replace(old_h1, new_h2, 1)
            changes.append(f"Changed H1 to H2: {inner_text[:50]}")
    
    # 2. Add visually hidden H1 if page has no H1
    if '<h1' not in content:
        # Get page title for the H1
        title_match = re.search(r'<title>([^|]+)', content)
        page_name = title_match.group(1).strip() if title_match else filename.replace('.html', '').replace('_', ' ').title()
        
        # Find a good place to insert - before main content
        # Look for first section/container
        insert_patterns = [
            r'(<main[^>]*>)',
            r'(<div class="uk-section">)',
            r'(<div class="uk-container">)',
            r'(<div class="uk-header">)',
        ]
        
        for pattern in insert_patterns:
            match = re.search(pattern, content)
            if match:
                insert_pos = match.start()
                h1_tag = f'\n<h1 class="uk-visually-hidden">{page_name}</h1>\n'
                content = content[:insert_pos] + h1_tag + content[insert_pos:]
                changes.append(f"Added hidden H1: {page_name}")
                break
    
    # 3. Fix "Escalation Matrix" - should be H2 not H1
    content = re.sub(
        r'<h1 class="uk-margin-remove-bottom">Escalation Matrix</h1>',
        '<h2 class="uk-margin-remove-bottom">Escalation Matrix</h2>',
        content
    )
    
    # 4. Fix H3 before H2 issues
    # Find H3 that should be H2 in the same context
    content = re.sub(
        r'<h3>Why trade with Standard Securities\?</h3>',
        '<h2>Why trade with Standard Securities?</h2>',
        content
    )
    content = re.sub(
        r'<h3>Benefits you\'ll get from us</h3>',
        '<h2>Benefits you\'ll get from us</h2>',
        content
    )
    
    # 5. Fix customers.html stats - add descriptive labels
    if filename == 'customers.html':
        for stat, label in [
            ('35,817', 'Active Clients'),
            ('4,400', 'Corporate Clients'),
            ('$620M', 'Assets Under Management'),
        ]:
            content = re.sub(
                rf'<h2 class="uk-margin-remove-bottom">{stat}</h2>',
                f'<h2 class="uk-margin-remove-bottom"><span class="stat-value">{stat}</span><span class="stat-label" style="display:block;font-size:0.6em;font-weight:400;">{label}</span></h2>',
                content
            )
    
    # 6. Fix downloads.html H3 section headings
    if filename == 'downloads.html':
        content = re.sub(
            r'<h3 class="uk-heading-bullet"><a href="#"> Download Form</a></h3>',
            '<h2 class="uk-heading-bullet">Download Form</h2>',
            content
        )
        content = re.sub(
            r'<h3 class="uk-heading-bullet"><a href="#">Fill The Form</a></h3>',
            '<h2 class="uk-heading-bullet">Fill The Form</h2>',
            content
        )
        content = re.sub(
            r'<h3 class="uk-heading-bullet"><a href="#">Send Form</a></h3>',
            '<h2 class="uk-heading-bullet">Send Form</h2>',
            content
        )
    
    # 7. Fix news.html article titles - these are H3 but should be H2 for consistency
    if filename == 'news.html':
        content = re.sub(
            r'<h3 class="uk-article-title uk-margin-small-top"><a class="uk-link-reset" href="([^"]+)">([^<]+)</a></h3>',
            r'<h2 class="uk-article-title uk-margin-small-top"><a class="uk-link-reset" href="\1">\2</a></h2>',
            content
        )
        content = re.sub(
            r'<h3 class="uk-text-truncate">',
            '<h2 class="uk-text-truncate">',
            content
        )
    
    # 8. Fix signin.html if it has content
    if filename == 'signin.html' and '<h2' in content:
        # Add a visually hidden H1 for page identity
        content = re.sub(
            r'(<main[^>]*>)',
            '\\1\n<h1 class="uk-visually-hidden">Sign In</h1>',
            content
        )
    
    if content != original:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filename}")
        for change in changes:
            print(f"  - {change}")

if __name__ == '__main__':
    fix_all_pages()
