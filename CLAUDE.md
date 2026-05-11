# Bharat AI Innovation Conference & Exhibition 2026

## Project Overview
Static multi-page website for India's premier AI conference at WTC Mumbai, Dec 10–11, 2026.
- Production: https://bharataiinnovation.com/
- Organizer: Aegis Knowledge Trust
- Contact: info@bharataiinnovation.com | +91 89765 80367
- Venue: World Trade Center Mumbai, Cuffe Parade, Mumbai

## Tech Stack
- Pure HTML/CSS/JS — no build tools, no framework, no package manager
- Hosted as static site (Apache/Cloudflare)
- Registration API: Cloudflare Pages Functions at `https://bharatai-networking.pages.dev/api/external/register`

## File Structure
```
index.html              - Home page (main entry, SEO optimized)
about.html              - About the event and organizers
conference.html         - Conference tracks and schedule
exhibition.html         - Exhibition packages and zones
startup-pitch.html      - Startup pitch competition page
training-workshop.html  - AI/ML training workshops
partner.html            - Partnership & sponsorship tiers
accommodation.html      - Premium hotels near WTC Mumbai
register.html           - 301 Redirect → networking.bharataiinnovation.com/register
contact.html            - 301 Redirect → networking.bharataiinnovation.com/contact
delegation.html         - Redirects to register.html
register-backup.html    - Original registration page (backup, not live)
contact-backup.html     - Original contact page (backup, not live)
.htaccess               - Server-side 301 redirects + SEO config
sitemap.xml             - XML sitemap for search engines
robots.txt              - Crawler instructions
css/style.css           - Main styles
js/main.js              - Main JavaScript
img/                    - Event/gallery images
images/                 - Speaker & dignitary photos
cdn/                    - CDN-cached images
```

## Key Constants (use consistently across all pages)
- **Logo URL (local, self-hosted):** `images/Bharat%20AI%20Innovation%20Logo.png` (relative for `<img src>`); `https://bharataiinnovation.com/images/Bharat%20AI%20Innovation%20Logo.png` (absolute, for OG/Twitter/JSON-LD)
- **Logo style:** rounded corners, padding, subtle shadow
- **Phone:** +91 89765 80367
- **Email:** info@bharataiinnovation.com
- **Event dates:** Dec 10–11, 2026
- **Venue:** World Trade Center Mumbai, Cuffe Parade, Mumbai

## Registration API
```
POST https://bharatai-networking.pages.dev/api/external/register
Payload: { first_name, last_name, email, phone, organization, job_title,
           industry, company_size, city, country, source,
           special_requirements, package, newsletter }
Response: { success, reference, attendee_id, name, email, badge_type,
            networking_app_url, already_registered? }
```

## Pass Types
- Delegate: ₹4,999 | VIP: ₹14,999 | Academic: ₹999 | Media: By Invite | Visitor: FREE
- Team packages: Team 5–9, Enterprise 10–19, Corporate 20+

## Exhibition Booth Packages (132 booths, 977 sqm)
Startup Pod ₹35K → Explorer ₹84K → Innovator ₹92.4K → Accelerator ₹1.56L → Enterprise ₹2.2L → Flagship ₹6.24L → Mega ₹15L

## Confirmed Speakers
- Shri. K.K. Singh — Joint Secretary, MeitY
- Shailesh Dhuri — CEO, Decimal Point Analytics
- Rajesh Dhuddu PhD — Partner & Emerging Tech Leader, PwC
- Bhupesh Daheria — CEO, Aegis School of Data Science & AI
- Dr. Ashish Tendulkar — Lead AI, Google

## Development Notes
- All pages share the same navbar and footer — update both when adding new pages
- No server-side logic; all dynamic behavior is via JS + external API
- SEO is critical: maintain meta tags, structured data, and canonical URLs on every page
- Do not make unverifiable claims (e.g., "India's largest") — use soft phrasing ("a leading", "top speakers")
- `delegation.html` and `register.html` are redirect pages — do not add content to them
- Speaker photos live in `images/`, gallery/event photos in `img/` and `images/gallery/`
