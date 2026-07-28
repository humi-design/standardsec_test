#!/usr/bin/env python3
"""
Fix duplicate JavaScript functions and JS errors
"""

import re

def fix_js_duplicates():
    filepath = '/workspace/standardsec_files/index.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all script blocks
    script_pattern = r'<script[^>]*>(.*?)</script>'
    scripts = re.findall(script_pattern, content, re.DOTALL)
    
    # Consolidate all translations into one
    translations_en = '''
        'About Us': 'About Us',
        'Products': 'Products',
        'Contact': 'Contact',
        'Login': 'Login',
        'Home': 'Home',
        'Learn More': 'Learn More',
        'Start Investing Now': 'Start Investing Now',
        'Trade on world-class platform': 'Trade on world-class platform',
        'Currency': 'Currency',
        'Commodities': 'Commodities',
        'Equity': 'Equity',
        'IPOs': 'IPOs',
        'Advisory': 'Advisory',
        'Depository': 'Depository',
    '''
    
    translations_hi = '''
        'About Us': 'हमारे बारे में',
        'Products': 'उत्पाद',
        'Contact': 'संपर्क',
        'Login': 'लॉगिन',
        'Home': 'होम',
        'Learn More': 'और जानें',
        'Start Investing Now': 'अभी निवेश शुरू करें',
        'Trade on world-class platform': 'विश्व-स्तरीय प्लेटफॉर्म पर व्यापार करें',
        'Currency': 'मुद्रा',
        'Commodities': 'कमोडिटीज',
        'Equity': 'इक्विटी',
        'IPOs': 'आईपीओ',
        'Advisory': 'सलाह',
        'Depository': 'डिपॉजिटरी',
    '''
    
    # Replace the inline translations in the HTML
    # Remove duplicate script blocks with translations
    content = re.sub(
        r'<!-- English Translations -->.*?<!-- English Translation End -->',
        '<!-- Translations consolidated -->',
        content,
        flags=re.DOTALL
    )
    
    # Add consolidated JavaScript before </body>
    consolidated_js = '''
<script>
// Consolidated Language Translation System (WCAG 3.1.2)
(function() {
    const translations = {
        'en': {
            'About Us': 'About Us',
            'Products': 'Products',
            'Contact': 'Contact',
            'Login': 'Login',
            'Home': 'Home',
            'Learn More': 'Learn More',
            'Start Investing Now': 'Start Investing Now',
            'Trade on world-class platform': 'Trade on world-class platform',
            'Currency': 'Currency',
            'Commodities': 'Commodities',
            'Equity': 'Equity',
            'IPOs': 'IPOs',
            'Advisory': 'Advisory',
            'Depository': 'Depository'
        },
        'hi': {
            'About Us': 'हमारे बारे में',
            'Products': 'उत्पाद',
            'Contact': 'संपर्क',
            'Login': 'लॉगिन',
            'Home': 'होम',
            'Learn More': 'और जानें',
            'Start Investing Now': 'अभी निवेश शुरू करें',
            'Trade on world-class platform': 'विश्व-स्तरीय प्लेटफॉर्म पर व्यापार करें',
            'Currency': 'मुद्रा',
            'Commodities': 'कमोडिटीज',
            'Equity': 'इक्विटी',
            'IPOs': 'आईपीओ',
            'Advisory': 'सलाह',
            'Depository': 'डिपॉजिटरी'
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
        
        // Update document language
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
        
        // Dispatch event
        window.dispatchEvent(new CustomEvent('languageChanged', { detail: { language: lang } }));
    }

    // Initialize language toggle buttons
    function initLanguageToggle() {
        var langEn = document.getElementById('lang-en');
        var langHi = document.getElementById('lang-hi');
        
        if (langEn) {
            langEn.addEventListener('click', function() {
                setLanguage('en');
            });
        }
        if (langHi) {
            langHi.addEventListener('click', function() {
                setLanguage('hi');
            });
        }
        
        // Load saved preference
        var savedLang = localStorage.getItem('preferredLanguage');
        if (savedLang) {
            setLanguage(savedLang);
        }
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initLanguageToggle);
    } else {
        initLanguageToggle();
    }
})();
</script>
'''
    
    # Add the consolidated script before </body>
    content = content.replace('</body>', consolidated_js + '</body>')
    
    # Remove the old inline translations blocks
    # First, remove the English translation comments and their content
    content = re.sub(
        r'<!-- English Translation -->\s*<script[^>]*>\s*const translations.*?</script>',
        '',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<!-- Hindi Translation -->\s*<script[^>]*>\s*const translations.*?</script>',
        '',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<!-- Translation Script -->\s*<script[^>]*>.*?function setLanguage.*?</script>',
        '',
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed JavaScript duplicates")

if __name__ == '__main__':
    fix_js_duplicates()
