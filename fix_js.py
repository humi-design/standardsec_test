#!/usr/bin/env python3
"""
Fix all JavaScript issues in index.html
"""

import re

def fix_js():
    filepath = '/workspace/standardsec_files/index.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the broken setLanguage function
    # Remove the incomplete else block
    content = re.sub(
        r'\} else \{\s*location\.reload\(\); // Reset to English\s*\}',
        '}',
        content
    )
    
    # Consolidate translations - ensure both en and hi exist
    # First, find and fix the main translations object
    old_translations = r"const translations = \{\s*'hi':\s*\{[^}]+\}\s*\};"
    
    new_translations = """const translations = {
        'en': {
            'Products': 'Products',
            'About Us': 'About Us',
            'Contact': 'Contact',
            'Login': 'Login',
            'Home': 'Home',
            'Learn More': 'Learn More',
            'Read more': 'Read more'
        },
        'hi': {
            'Products': 'उत्पाद',
            'About Us': 'हमारे बारे में',
            'Contact': 'संपर्क करें',
            'Login': 'लॉग इन',
            'Home': 'होम',
            'Learn More': 'और जानें',
            'Read more': 'और पढ़ें'
        }
    };"""
    
    content = re.sub(old_translations, new_translations, content, flags=re.DOTALL)
    
    # Add complete working setLanguage function at the end before </body>
    # First, remove any broken setLanguage functions
    
    # Find and remove duplicate/old setLanguage functions
    # The function starts with "function setLanguage" and ends with matching closing brace
    
    # Remove the first broken setLanguage (the one inside script tags after translations)
    content = re.sub(
        r"function setLanguage\(lang\) \{[\s\S]*?window\.dispatchEvent\(new CustomEvent\('languageChanged', \{ detail: \{ language: lang \} \}\)\);",
        "// setLanguage defined below",
        content
    )
    
    # Remove translatePageToHindi function (it has issues)
    content = re.sub(
        r'function translatePageToHindi\(\) \{[\s\S]*?document\.getElementById\(\'lang-hi\'\)\.click\(\);\s*\}',
        '// translatePageToHindi removed - use setLanguage instead',
        content
    )
    
    # Remove old DOMContentLoaded handlers that might cause issues
    content = re.sub(
        r"document\.addEventListener\('DOMContentLoaded', function\(\) \{[\s\S]*?'preferredLang'[\s\S]*?\}\);",
        '',
        content
    )
    
    # Add a clean, working setLanguage function and initialization at the end
    clean_js = '''
<script>
// WCAG 3.1.2 - Working Language Toggle
(function() {
    // Consolidated translations
    var translations = {
        'en': {
            'Products': 'Products',
            'About Us': 'About Us',
            'Contact': 'Contact',
            'Login': 'Login',
            'Home': 'Home',
            'Learn More': 'Learn More',
            'Read more': 'Read more',
            'Start Investing Now': 'Start Investing Now',
            'Trade on world-class platform': 'Trade on world-class platform'
        },
        'hi': {
            'Products': 'उत्पाद',
            'About Us': 'हमारे बारे में',
            'Contact': 'संपर्क करें',
            'Login': 'लॉग इन',
            'Home': 'होम',
            'Learn More': 'और जानें',
            'Read more': 'और पढ़ें',
            'Start Investing Now': 'अभी निवेश शुरू करें',
            'Trade on world-class platform': 'विश्व-स्तरीय प्लेटफॉर्म पर व्यापार करें'
        }
    };

    function setLanguage(lang) {
        if (!translations[lang]) lang = 'en';
        
        // Update button states
        var langEn = document.getElementById('lang-en');
        var langHi = document.getElementById('lang-hi');
        
        if (langEn) {
            langEn.setAttribute('aria-pressed', lang === 'en' ? 'true' : 'false');
            langEn.classList.toggle('active', lang === 'en');
        }
        if (langHi) {
            langHi.setAttribute('aria-pressed', lang === 'hi' ? 'true' : 'false');
            langHi.classList.toggle('active', lang === 'hi');
        }
        
        // Update document language attribute
        document.documentElement.lang = lang;
        
        // Translate elements with data-translate attribute
        var elements = document.querySelectorAll('[data-translate]');
        elements.forEach(function(el) {
            var key = el.getAttribute('data-translate');
            if (translations[lang][key]) {
                el.textContent = translations[lang][key];
            }
        });
        
        // Store preference
        localStorage.setItem('preferredLanguage', lang);
        
        // Dispatch event for other components
        window.dispatchEvent(new CustomEvent('languageChanged', { detail: { language: lang } }));
    }

    // Initialize on DOM ready
    function init() {
        var langEn = document.getElementById('lang-en');
        var langHi = document.getElementById('lang-hi');
        
        if (langEn) {
            langEn.addEventListener('click', function() { setLanguage('en'); });
        }
        if (langHi) {
            langHi.addEventListener('click', function() { setLanguage('hi'); });
        }
        
        // Load saved preference
        var savedLang = localStorage.getItem('preferredLanguage');
        if (savedLang && translations[savedLang]) {
            setLanguage(savedLang);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
</script>
'''
    
    # Insert before </body>
    content = content.replace('</body>', clean_js + '</body>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed JavaScript issues")

if __name__ == '__main__':
    fix_js()
