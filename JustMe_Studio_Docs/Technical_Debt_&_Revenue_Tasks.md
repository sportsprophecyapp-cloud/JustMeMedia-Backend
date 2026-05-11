# Technical Debt & Revenue Tasks

These are the specific coding tasks required to activate or optimize revenue streams across the portfolio.

## 🛠 TripSync (AI Travel Planner)
- [ ] **Affiliate ID Integration**: Locate the itinerary link generation logic in `/Users/williamcommu/tripsync/server.py` and append `&tag=ID` (Booking/CJ).
- [ ] **Mobile Layout Audit**: Ensure the PWA remains responsive on iOS/Android physical devices.
- [ ] **SEO Optimization**: Ensure the landing page is indexable for "Private AI Travel Planner."

## 🛠 SaaS Price DB (The "Painkiller" Pivot)
- [x] **Onboarding Bypass**: Removed manual barriers; verified instant access upon Stripe payment.
- [x] **"Monitor" Messaging**: Revamped `index.html` to focus on "Competitive Alerts" and prevent churn.
- [ ] **Slack/Webhook Logic**: Verify the backend is actually firing alerts when a price drift is detected in the DB.
- [ ] **Live Price Polling**: Ensure the cron job is active to maintain the "Real-Time" value of the monitoring.

## 🛠 Events Arena
- [ ] **Sponsor Form Hardening**: Ensure the Base64 image compression is working perfectly for new sponsor banners.
- [ ] **Analytics Dashboard**: Verify the `/admin/studio` metrics are accurate for showing to potential sponsors.
- [ ] **Private Room Logic**: Finalize the creator-code entry system to allow influencers to host their own "Arenas."

## 🛠 JustMe Media Site
- [ ] **Partner Form Webhook**: Ensure applications from `partners.html` are sent to a dedicated email or Slack channel for immediate review.
- [x] **Mobile Optimization**: Audited and optimized header/sidebar layout for premium mobile experience.
