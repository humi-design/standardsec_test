#!/usr/bin/env python3
"""
Fix Hindi language toggle issues in feature/custom-hindi-language branch
"""

import re

def fix_hindi_toggle():
    filepath = '/workspace/standardsec_files/index.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix translations object - add 'en' key and rename 'hi' to have both languages
    old_translations = r"const translations = \{'hi': \{"
    new_translations = """const translations = {
        'en': {},
        'hi': {"""
    
    content = content.replace("const translations = {'hi': {", new_translations)
    
    # 2. Fix the setLanguage function - don't reload on English
    old_setlang = """function setLanguage(lang) {
        document.documentElement.lang = lang;
        const langEn = document.getElementById('lang-en');
        const langHi = document.getElementById('lang-hi');
        if (langEn) langEn.setAttribute('aria-pressed', lang === 'en' ? 'true' : 'false');
        if (langHi) langHi.setAttribute('aria-pressed', lang === 'hi' ? 'true' : 'false');
        if (langEn) langEn.classList.toggle('active', lang === 'en');
        if (langHi) langHi.classList.toggle('active', lang === 'hi');
        localStorage.setItem('preferredLang', lang);
        if (lang === 'hi') {
            translatePageToHindi();
        } else {
            location.reload();
        }
    }"""
    
    new_setlang = """function setLanguage(lang) {
        document.documentElement.lang = lang;
        const langEn = document.getElementById('lang-en');
        const langHi = document.getElementById('lang-hi');
        if (langEn) langEn.setAttribute('aria-pressed', lang === 'en' ? 'true' : 'false');
        if (langHi) langHi.setAttribute('aria-pressed', lang === 'hi' ? 'true' : 'false');
        if (langEn) langEn.classList.toggle('active', lang === 'en');
        if (langHi) langHi.classList.toggle('active', lang === 'hi');
        localStorage.setItem('preferredLang', lang);
        if (lang === 'hi') {
            translatePageToHindi();
        } else {
            // Restore English text from data attributes or reload
            restoreEnglish();
        }
    }"""
    
    content = content.replace(old_setlang, new_setlang)
    
    # 3. Add restoreEnglish function before the closing </script>
    restore_func = """
    function restoreEnglish() {
        // Find all elements with data-translated attribute and restore original text
        var translatedElements = document.querySelectorAll('[data-translated]');
        translatedElements.forEach(function(el) {
            var originalText = el.getAttribute('data-original-text');
            if (originalText) {
                el.textContent = originalText;
            }
            el.removeAttribute('data-translated');
        });
        // Remove all data-original-text attributes
        document.querySelectorAll('[data-original-text]').forEach(function(el) {
            el.removeAttribute('data-original-text');
        });
    }
    """
    
    # Insert restoreEnglish function before closing of the script
    content = content.replace(
        'document.addEventListener(\'DOMContentLoaded\', function() {',
        restore_func + '\n    document.addEventListener(\'DOMContentLoaded\', function() {'
    )
    
    # 4. Fix translatePageToHindi to save original text
    old_translate = """textNodes.forEach(node => {
            const text = node.textContent.trim();
            if (text && translations['hi'][text]) {
                node.textContent = translations['hi'][text];
                node.parentElement.setAttribute('data-translated', 'true');
            }
        });"""
    
    new_translate = """textNodes.forEach(node => {
            const text = node.textContent.trim();
            if (text && translations['hi'][text]) {
                // Save original text before translating
                if (!node.parentElement.hasAttribute('data-original-text')) {
                    node.parentElement.setAttribute('data-original-text', node.textContent);
                }
                node.textContent = translations['hi'][text];
                node.parentElement.setAttribute('data-translated', 'true');
            }
        });"""
    
    content = content.replace(old_translate, new_translate)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed Hindi language toggle in feature/custom-hindi-language branch")

if __name__ == '__main__':
    fix_hindi_toggle()
