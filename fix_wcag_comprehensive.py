#!/usr/bin/env python3
"""
Comprehensive WCAG 2.2 AA Accessibility Remediation Script
Fixes issues across all HTML files in the Standard Securities website
"""

import os
import re
import glob
from pathlib import Path

class AccessibilityFixer:
    def __init__(self, directory):
        self.directory = directory
        self.files = glob.glob(os.path.join(directory, '*.html'))
        
    def fix_all(self):
        """Main method to fix all accessibility issues"""
        for filepath in self.files:
            filename = os.path.basename(filepath)
            print(f"Processing: {filename}")
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip certain files
            if filename in ['accessibility-toolbar.html', 'botbot.html', '404.html']:
                continue
                
            # Apply fixes
            content = self.fix_duplicate_ids(content, filename)
            content = self.remove_duplicate_css(content)
            content = self.fix_heading_hierarchy(content, filename)
            content = self.add_missing_alt_text(content)
            content = self.fix_image_alt_duplicates(content)
            content = self.ensure_skip_link(content, filename)
            content = self.ensure_main_landmark(content, filename)
            content = self.fix_language_toggle(content, filename)
            content = self.fix_autocomplete_duplicates(content)
            content = self.fix_duplicate_translations(content, filename)
            content = self.ensure_page_title(content, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  Fixed: {filename}")
    
    def fix_duplicate_ids(self, content, filename):
        """Make IDs unique per page by prefixing with filename"""
        # Common IDs that appear on every page - make them unique
        id_mappings = {
            'mobile-nav-modal': f'mobile-nav-modal-{self.get_page_prefix(filename)}',
            'mobile-menu-toggle': f'mobile-menu-toggle-{self.get_page_prefix(filename)}',
            'lang-en': f'lang-en-{self.get_page_prefix(filename)}',
            'lang-hi': f'lang-hi-{self.get_page_prefix(filename)}',
            'accessibilityToggle': f'accessibilityToggle-{self.get_page_prefix(filename)}',
            'accessibilityPanel': f'accessibilityPanel-{self.get_page_prefix(filename)}',
            'google_translate_element_nav': f'google-translate-{self.get_page_prefix(filename)}',
            'main-content': f'main-content-{self.get_page_prefix(filename)}',
        }
        
        for old_id, new_id in id_mappings.items():
            # Only replace if this is a standalone ID attribute
            content = re.sub(
                rf'\bid="{re.escape(old_id)}"\b',
                f'id="{new_id}"',
                content
            )
        
        return content
    
    def get_page_prefix(self, filename):
        """Generate a unique prefix based on filename"""
        # Remove extension and convert to safe identifier
        name = filename.replace('.html', '')
        # Remove common words for cleaner IDs
        name = name.replace('standardsec-', '').replace('standardsec_', '')
        return name
    
    def remove_duplicate_css(self, content):
        """Remove duplicate .lang-toggle CSS blocks"""
        # Pattern to match duplicate lang-toggle CSS blocks
        lang_toggle_pattern = r'<style>\s*\.lang-toggle\s*\{[^}]+\}[^}]*\}\s*</style>'
        
        # Find all matches
        matches = list(re.finditer(lang_toggle_pattern, content, re.DOTALL))
        
        if len(matches) > 1:
            # Keep only the first occurrence, remove others
            # Process from end to beginning to preserve positions
            for match in reversed(matches[1:]):
                content = content[:match.start()] + content[match.end():]
        
        return content
    
    def fix_heading_hierarchy(self, content, filename):
        """Fix heading hierarchy issues where levels are skipped"""
        # This is a page-specific fix - we'll do basic fixes here
        # More complex fixes require manual review
        
        # Ensure there's exactly one H1 per page
        h1_count = len(re.findall(r'<h1[^>]*>', content))
        
        if h1_count > 1:
            # If there are multiple H1s, convert extras to H2
            # This is a basic fix - visual design may need review
            pass  # Complex fix - needs careful handling
        
        return content
    
    def add_missing_alt_text(self, content):
        """Add alt attributes to images that are missing them"""
        # Fix logo images
        content = re.sub(
            r'<img\s+src="img/logo\.png"(?![^>]*alt=)',
            '<img src="img/logo.png" alt="Standard Securities logo"',
            content
        )
        
        # Fix other images with data-src pattern
        content = re.sub(
            r'<img\s+src="([^"]+)"\s+data-src="([^"]+)"(?![^>]*alt=)',
            r'<img src="\1" data-src="\2" alt=""',
            content
        )
        
        return content
    
    def fix_image_alt_duplicates(self, content):
        """Fix cases where alt appears multiple times"""
        # Remove duplicate alt attributes
        def fix_img_tag(match):
            tag = match.group(0)
            # Keep only the first alt attribute
            alts = re.findall(r'alt="[^"]*"', tag)
            if len(alts) > 1:
                # Keep first alt, remove duplicates
                tag = tag.replace(alts[-1], '', 1)
            return tag
        
        content = re.sub(r'<img[^>]+>', fix_img_tag, content)
        return content
    
    def ensure_skip_link(self, content, filename):
        """Ensure skip link exists and points to correct main content ID"""
        prefix = self.get_page_prefix(filename)
        main_id = f'main-content-{prefix}'
        
        # Check if skip link exists
        if 'skip-link' not in content.lower() or 'class="skip-link"' not in content:
            # Add skip link after body tag
            skip_link = f'<a href="#{main_id}" class="skip-link">Skip to main content</a>'
            content = content.replace('<body>', f'<body>\n    {skip_link}', 1)
        else:
            # Update existing skip link to point to correct ID
            content = re.sub(
                r'href="#[^"]*"[^>]*class="skip-link"',
                f'href="#{main_id}" class="skip-link"',
                content
            )
            content = re.sub(
                r'class="skip-link"[^>]*href="#[^"]*"',
                f'class="skip-link" href="#{main_id}"',
                content
            )
        
        return content
    
    def ensure_main_landmark(self, content, filename):
        """Ensure main landmark exists and has correct ID"""
        prefix = self.get_page_prefix(filename)
        main_id = f'main-content-{prefix}'
        
        # Check if <main> exists
        if '<main' not in content:
            # Find where to insert main - after any header/nav, before first section
            # This is a basic insertion - may need adjustment
            pass  # Complex fix - needs careful handling
        
        # Update existing main tag to have correct ID
        content = re.sub(
            r'<main([^>]*)>',
            f'<main id="{main_id}"\\1>',
            content
        )
        
        # If main doesn't have id, add it
        if 'id="' + main_id + '"' not in content and '<main' in content:
            content = re.sub(
                r'<main(?![^>]*id=)([^>]*)>',
                f'<main id="{main_id}"\\1>',
                content
            )
        
        return content
    
    def fix_language_toggle(self, content, filename):
        """Fix language toggle buttons with correct IDs"""
        prefix = self.get_page_prefix(filename)
        
        # Update button IDs
        content = re.sub(
            r'<button[^>]*id="lang-en"',
            f'<button type="button" id="lang-en-{prefix}"',
            content
        )
        content = re.sub(
            r'<button[^>]*id="lang-hi"',
            f'<button type="button" id="lang-hi-{prefix}"',
            content
        )
        
        # Update onclick handlers to use correct IDs
        content = re.sub(
            r"getElementById\('lang-en'\)",
            f"getElementById('lang-en-{prefix}')",
            content
        )
        content = re.sub(
            r'getElementById\("lang-en"\)',
            f'getElementById("lang-en-{prefix}")',
            content
        )
        content = re.sub(
            r"getElementById\('lang-hi'\)",
            f"getElementById('lang-hi-{prefix}')",
            content
        )
        content = re.sub(
            r'getElementById\("lang-hi"\)',
            f'getElementById("lang-hi-{prefix}")',
            content
        )
        
        return content
    
    def fix_autocomplete_duplicates(self, content):
        """Remove duplicate autocomplete attributes"""
        def fix_input(match):
            tag = match.group(0)
            # Find all autocomplete attributes
            autocompletes = re.findall(r'autocomplete="[^"]*"', tag)
            if len(autocompletes) > 1:
                # Keep only the first autocomplete
                for dup in autocompletes[1:]:
                    tag = tag.replace(' ' + dup, '')
            return tag
        
        content = re.sub(r'<input[^>]+>', fix_input, content)
        return content
    
    def fix_duplicate_translations(self, content, filename):
        """Remove duplicate translation objects in JavaScript"""
        # Find multiple var translations = {...} blocks and merge them
        pattern = r'var\s+translations\s*=\s*\{[^}]+\};'
        matches = list(re.finditer(pattern, content, re.DOTALL))
        
        if len(matches) > 1:
            # Keep only the first translation block
            for match in reversed(matches[1:]):
                content = content[:match.start()] + content[match.end():]
        
        return content
    
    def ensure_page_title(self, content, filename):
        """Ensure page has proper title"""
        if '<title>' not in content:
            # Add a basic title if missing
            page_name = filename.replace('.html', '').replace('-', ' ').title()
            content = content.replace(
                '<head>',
                f'<head>\n    <title>{page_name} | Standard Securities</title>'
            )
        return content


def main():
    """Main entry point"""
    directory = '/workspace/project/standardsec_test'
    fixer = AccessibilityFixer(directory)
    fixer.fix_all()
    print("\nAccessibility fixes complete!")


if __name__ == '__main__':
    main()
