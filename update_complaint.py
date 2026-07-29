#!/usr/bin/env python3
import re

with open('complaint.html', 'r') as f:
    content = f.read()

# Add CSS links after </title>
old_title_end = '</title>'
new_css = '''</title>
    <link rel="stylesheet" href="css/modern-design-system.css">
    <link rel="stylesheet" href="css/uikit-compat.css">'''

content = content.replace(old_title_end, new_css)

# Find the main tag and wrap with header
old_skip_link = '''        <a href="#main-cmp" class="skip-link">Skip to main content</a>

    <main id="main-cmp">'''

new_skip_link = '''    <!-- Skip Link for Accessibility -->
    <a href="#main-cmp" class="skip-link">Skip to main content</a>

    <!-- Header -->
    <header class="header" role="banner">
        <div class="container">
            <div class="header-inner">
                <div class="header-logo">
                    <a href="index.html" aria-label="Standard Securities - Go to homepage">
                        <img src="img/logo.png" alt="Standard Securities logo" width="180" height="48">
                    </a>
                </div>
                <nav class="header-nav" role="navigation" aria-label="Main navigation">
                    <a href="index.html" class="header-nav-link">Home</a>
                    <a href="products.html" class="header-nav-link">Products</a>
                    <a href="about.html" class="header-nav-link">About Us</a>
                    <a href="contact.html" class="header-nav-link">Contact</a>
                    <a href="complaint_new.html" class="header-nav-link">Complaints</a>
                </nav>
                <div class="header-actions">
                    <a href="https://ekyc.standardsec.net:8002" class="btn btn-primary btn-sm">Open Account</a>
                </div>
                <button class="mobile-nav-toggle" aria-label="Open navigation menu" aria-expanded="false">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="3" y1="6" x2="21" y2="6"></line>
                        <line x1="3" y1="12" x2="21" y2="12"></line>
                        <line x1="3" y1="18" x2="21" y2="18"></line>
                    </svg>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main id="main-cmp">'''

content = content.replace(old_skip_link, new_skip_link)

# Add footer before </body>
old_body_end = '''    </body>'''

new_body_end = '''
    <!-- Footer -->
    <footer class="footer" role="contentinfo">
        <div class="container">
            <div class="footer-bottom">
                <p class="footer-copyright">Copyright ©2024 Standard Securities & Investment Intermediates Pvt Ltd.</p>
            </div>
        </div>
    </footer>

    <!-- Scripts -->
    <script src="js/vendor/jquery.min.js"></script>
    <script src="js/vendor/uikit.min.js"></script>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const mobileToggle = document.querySelector('.mobile-nav-toggle');
            if (mobileToggle) {
                mobileToggle.addEventListener('click', function() {
                    alert('Mobile menu - to be implemented');
                });
            }
        });
    </script>
</body>'''

content = content.replace(old_body_end, new_body_end)

# Remove inline styles
content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)

with open('complaint.html', 'w') as f:
    f.write(content)

print("complaint.html updated")
