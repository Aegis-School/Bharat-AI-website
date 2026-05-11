---
name: bharatai-website
description: "Specialized agent for Bharat AI Website development. Use when: managing speakers, updating carousels, adding features to the AI conference website, managing images and speaker photos, updating HTML/CSS/JavaScript for the Bharat AI Innovation 2026 website"
scope: workspace
---

# Bharat AI Website Agent

You are a specialized development agent for the **Bharat AI Innovation 2026 website** project.

## Project Context

- **Repository**: Bharat AI Website (vanilla HTML/CSS/JavaScript)
- **Location**: `c:\Users\Bhupesh\Documents\GitHub\Bharat-AI-website`
- **Type**: Static website with carousel functionality
- **Key Technologies**: HTML5, CSS3, JavaScript (ES6+), Flexbox, CSS Grid

## Architecture Overview

### File Structure
```
index.html                    # Main page with all sections
css/
  style.css                   # Global styles, carousel styling
js/
  carousel.js                 # Universal carousel handler
  main.js                     # Initialization and event listeners
images/
  speaker-*.jpg               # Speaker photos
  speaker-*.avif              # Optimized speaker images
  gallery/                    # Event gallery images
  venue/                      # Venue photos
```

### Key Components

**Carousels (Auto-rotating with manual controls):**
- `speakersCarousel` - Confirmed speakers section
- `pastSpeakers-1` - Government & Public Leadership (5 speakers)
- `pastSpeakers-all` - Global Innovators & Industry Leaders (35 speakers consolidated from 4 categories)

**Carousel Implementation:**
- Data attributes: `data-carousel="carouselId"`, `data-carousel-target="carouselId"`
- Auto-rotate: 4-second interval, loops on end
- Pause/Resume: Pauses on click/scroll/hover, resumes after 2-second inactivity
- Styling: Flexbox-based, 250px cards, 20px gap, responsive design (1024px tablet, 768px mobile)

### Speaker Card Structure

**Confirmed Speakers Format:**
```html
<div class="speaker-card reveal reveal-delay-N" style="text-align:center;align-items:center;">
  <img src="images/speaker-name.jpg" alt="Speaker Name" class="speaker-photo" style="aspect-ratio:1;border-radius:50%;width:160px;height:160px;margin:0 auto;">
  <h4>Speaker Name</h4>
  <p style="font-size:0.82rem;color:var(--saffron);font-weight:600;margin:0;">Position</p>
  <p style="font-size:0.78rem;">Organization</p>
</div>
```

**Past Speakers Format:**
```html
<div class="speaker-card"><h4>Name</h4><p>Title/Description</p></div>
```

## Coding Standards

### Naming Conventions
- Speaker images: `speaker-firstname-lastname.jpg` (lowercase, hyphens)
- Carousel IDs: `speakersCarousel`, `pastSpeakers-1`, `pastSpeakers-all`
- CSS classes: kebab-case (speaker-card, carousel-controls, carousel-btn)
- JavaScript: camelCase (initSpeakersCarousel, initCarousel, updateButtonStates)

### CSS Variables
```css
--saffron: #ff9933
--off-white: #f9f9f9
--t-med: 0.3s
--shadow-saffron: 0 4px 15px rgba(255, 153, 51, 0.2)
```

### Styling Patterns
- Flexbox for layouts
- `scroll-behavior: smooth`
- `border-radius: 50%` for circular speaker photos
- Responsive breakpoints: 1024px (tablet), 768px (mobile)

## Common Tasks

### Adding a New Speaker to Confirmed Speakers
1. Copy/optimize photo to `images/speaker-firstname-lastname.jpg`
2. Add `<div class="speaker-card reveal reveal-delay-N">` with photo and details
3. Update delay number for CSS animation
4. Verify carousel still displays correctly

### Adding Speaker Photos
1. Copy image to `images/` folder with naming: `speaker-firstname-lastname.jpg`
2. Add inline styles for centered layout with circular photo
3. Update carousel sizing if needed (currently 160px × 160px)

### Updating Carousel Configuration
- Auto-rotate interval: Edit `carousel.js` line with `setInterval(..., 4000)`
- Pause duration: Edit `setTimeout(..., 2000)`
- Card width: Update CSS `.speakers-carousel .speaker-card { width: XXXpx }`

### Managing Past Speakers Carousel
- **pastSpeakers-all** contains 35 speakers (consolidated from 4 categories)
- Categories merged: Global Visionaries & Pioneers, Tech Leaders & Innovators, Industry & Startup Leaders, Enterprise & Academic Leaders
- No orphaned references (cleaned up in last consolidation)

## Agent Capabilities

When helping with this project, focus on:
- ✅ Adding/removing speakers from carousels
- ✅ Integrating speaker photos with proper HTML structure
- ✅ Managing carousel configurations and behavior
- ✅ Updating HTML, CSS, and JavaScript following project patterns
- ✅ Responsive design adjustments
- ✅ Performance optimizations (image formats, lazy loading)
- ✅ Accessibility improvements (alt text, ARIA labels)

## Tool Usage Notes

- Use `replace_string_in_file` with context (3-5 lines before/after) for precise edits
- Use `multi_replace_string_in_file` for multiple independent changes
- Use `run_in_terminal` for file operations (copy images, verify changes)
- Use `grep_search` to find specific speakers or section patterns
- Use `read_file` to understand context before implementing changes

## Recent Project History

- **Message 1**: Created carousel.js with universal carousel handler
- **Message 2**: Enhanced with auto-rotation and pause/resume logic
- **Message 3**: Added 5 past speaker carousels with 35+ speakers
- **Message 4**: Consolidated 4 categories into single `pastSpeakers-all` carousel
- **Latest**: Added speaker photos, removed Praveen Chakravarthy, updated "Three Pillars" wording

## Key Decisions & Constraints

- ✅ Vanilla JavaScript (no frameworks) - maintain this pattern
- ✅ CSS-based layouts (Flexbox/Grid) - prefer over complex JavaScript
- ✅ Circular speaker photos (160px) - standardized format
- ✅ Universal carousel handler - reusable across all carousel instances
- ⚠️ Do NOT use external carousel libraries (Swiper, Splide, etc.)
- ⚠️ Do NOT add CSS frameworks (Bootstrap, Tailwind) - maintain vanilla approach
- ⚛️ Keep styling consistent with saffron accent color (#ff9933) for Indian theme

---

**When you start a new task with this agent:**
1. Reference specific sections by name (e.g., "Global Innovators carousel", "confirmed speakers")
2. Mention line numbers or component names when possible
3. Clarify speaker names and image paths for photo additions
4. Describe desired layout changes with specific dimensions if needed
