# Standard Securities Design System - Implementation Guide

## Overview
This document outlines the modern design system implemented for the Standard Securities website.

## Files Created

### 1. css/modern-design-system.css
The core design system file containing:
- CSS Custom Properties (Design Tokens)
- Typography System
- Layout System (Grid, Flexbox)
- Component System (Buttons, Cards, Forms, etc.)
- Animation System
- Accessibility System
- Responsive Breakpoints

### 2. css/uikit-compat.css
UIKit compatibility layer that:
- Bridges UIKit utility classes with the modern design system
- Ensures backward compatibility with existing HTML
- Provides consistent styling for all UIKit components

### 3. index.html (Rebuilt)
Complete rebuild of the homepage with:
- Semantic HTML5 structure
- Clean, modern design
- WCAG 2.2 AA accessibility compliance
- Responsive layout
- No inline styles

## Design Tokens

### Colors
```css
--color-primary: #146CE0
--color-secondary: #012c6d
--color-success: #2ecc71
--color-danger: #f44336
--text-primary: #0f172a
--text-secondary: #475569
```

### Spacing Scale (8px base)
```css
--space-1: 0.25rem  (4px)
--space-2: 0.5rem   (8px)
--space-3: 0.75rem   (12px)
--space-4: 1rem      (16px)
--space-6: 1.5rem    (24px)
--space-8: 2rem      (32px)
--space-12: 3rem     (48px)
--space-16: 4rem     (64px)
--space-20: 5rem     (80px)
--space-24: 6rem     (96px)
```

### Typography
- Font Family: Open Sans, Work Sans
- Type Scale: xs, sm, base, lg, xl, 2xl, 3xl, 4xl, 5xl, 6xl
- Line Heights: tight (1.25), normal (1.5), relaxed (1.625)

### Border Radius
```css
--radius-sm: 0.25rem   (4px)
--radius-md: 0.375rem  (6px)
--radius-lg: 0.5rem    (8px)
--radius-xl: 0.75rem   (12px)
--radius-2xl: 1rem     (16px)
--radius-3xl: 1.5rem   (24px)
```

### Shadows
```css
--shadow-xs: 0 1px 2px rgba(0,0,0,0.05)
--shadow-sm: 0 1px 3px rgba(0,0,0,0.1)
--shadow-md: 0 4px 6px rgba(0,0,0,0.1)
--shadow-lg: 0 10px 15px rgba(0,0,0,0.1)
--shadow-xl: 0 20px 25px rgba(0,0,0,0.1)
```

## Component Classes

### Buttons
```html
<button class="btn">Default</button>
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-outline">Outline</button>
<button class="btn btn-ghost">Ghost</button>
<button class="btn btn-white">White</button>
```

Button Sizes:
- `btn-sm` - Small button
- `btn-lg` - Large button
- `btn-xl` - Extra large button
- `btn-full` - Full width button

### Cards
```html
<div class="card">
    <div class="card-body">
        Card content
    </div>
</div>
```

Card Variants:
- `card-border` - With border
- `card-shadow` - With shadow
- `card-shadow-md` - Medium shadow
- `card-shadow-lg` - Large shadow
- `card-hover` - Hover effect

### Forms
```html
<div class="form-group">
    <label class="form-label">Label</label>
    <input class="form-input" type="text">
</div>
```

### Badges/Labels
```html
<span class="badge">Default</span>
<span class="badge badge-primary">Primary</span>
<span class="badge badge-success">Success</span>
<span class="badge badge-danger">Danger</span>
<span class="badge badge-warning">Warning</span>
```

### Tiles (Feature Cards)
```html
<div class="tile">
    <div class="tile-icon">
        <img src="icon.svg" alt="">
    </div>
    <h3>Title</h3>
    <p>Description</p>
</div>
```

### Stats
```html
<div class="stat-card">
    <div class="stat-value">100+</div>
    <div class="stat-label">Label</div>
</div>
```

## Layout Classes

### Container
```html
<div class="container">Content</div>
<div class="container container-sm">Small</div>
<div class="container container-lg">Large</div>
```

### Section
```html
<section class="section">Default</section>
<section class="section section--primary">Primary</section>
<section class="section section--muted">Muted</section>
<section class="section section--dark">Dark</section>
```

### Grid
```html
<div class="grid">Default grid</div>
<div class="grid grid-2">2 columns</div>
<div class="grid grid-3">3 columns</div>
<div class="grid grid-4">4 columns</div>
```

### Flexbox
```html
<div class="flex">Flex container</div>
<div class="flex flex-col">Column</div>
<div class="flex flex-wrap">Wrap</div>
<div class="flex items-center">Center items</div>
<div class="flex justify-between">Space between</div>
```

## Responsive Breakpoints

| Breakpoint | Min Width | Description |
|------------|-----------|-------------|
| xs | 320px | Extra small devices |
| sm | 640px | Small devices |
| md | 768px | Tablets |
| lg | 1024px | Laptops |
| xl | 1280px | Desktops |
| 2xl | 1440px | Large desktops |

### Responsive Classes
```css
/* Show/hide */
.uk-hidden@m    /* Hide on medium screens */
.uk-visible@m    /* Show on medium screens */

/* Widths */
.uk-width-1-2@m  /* Half width on medium+ */
.uk-width-1-3@m  /* Third width on medium+ */
.uk-width-1-4@m  /* Quarter width on medium+ */
```

## Accessibility Features

### Skip Link
```html
<a href="#main-content" class="skip-link">Skip to main content</a>
```

### Focus Indicators
All interactive elements have:
- 3px solid outline
- 2px outline offset
- High contrast colors
- Visible on keyboard navigation

### Target Size
Minimum 44x44px for all interactive elements (WCAG 2.5.5)

### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}
```

## Header Template

```html
<header class="header" role="banner">
    <div class="container">
        <div class="header-inner">
            <div class="header-logo">
                <a href="index.html">
                    <img src="img/logo.png" alt="Logo">
                </a>
            </div>
            <nav class="header-nav" role="navigation" aria-label="Main navigation">
                <!-- Navigation links -->
            </nav>
            <div class="header-actions">
                <!-- Buttons, language toggle, etc. -->
            </div>
        </div>
    </div>
</header>
```

## Footer Template

```html
<footer class="footer" role="contentinfo">
    <div class="container">
        <div class="footer-grid">
            <div class="footer-brand">
                <img src="img/logo.png" alt="Logo">
                <p>Company description</p>
            </div>
            <div>
                <h3 class="footer-title">Column</h3>
                <ul class="footer-links">
                    <li><a href="#">Link</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p class="footer-copyright">Copyright</p>
        </div>
    </div>
</footer>
```

## Updating Other Pages

To update other HTML pages to use the new design system:

1. Update CSS links in `<head>`:
```html
<link rel="stylesheet" href="css/modern-design-system.css">
<link rel="stylesheet" href="css/uikit-compat.css">
```

2. Add skip link after `<body>`:
```html
<a href="#main-content" class="skip-link">Skip to main content</a>
```

3. Wrap main content in `<main id="main-content">`

4. Replace inline styles with CSS classes:
   - `style="color: #xxx"` → Use text color classes
   - `style="padding: Xpx"` → Use spacing classes
   - `style="margin: Xpx"` → Use margin classes

5. Update header and footer to match templates

6. Test responsive behavior at all breakpoints

## Best Practices

1. **Use Design Tokens**: Always use CSS variables for colors, spacing, etc.
2. **Semantic HTML**: Use proper HTML5 elements
3. **Accessibility**: Include ARIA labels, focus states, and keyboard support
4. **Responsive First**: Design for mobile first, enhance for larger screens
5. **No Inline Styles**: Use CSS classes instead
6. **Consistent Spacing**: Stick to the 8px spacing scale
7. **Typography Hierarchy**: Use heading classes properly
