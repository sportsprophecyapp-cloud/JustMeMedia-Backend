# Future Project Ideas

This document serves as a repository for upcoming SaaS, PWA, and application ideas for Just Me Media.

---

## Project Name: Echoes
**Date:** May 11, 2026
**Client:** William Commu – Just Me Media

### 1. Product Overview
Echoes is a beautiful, easy-to-use, 100% private Progressive Web App (PWA) that helps families preserve, organize, and search their photos, videos, voice stories, and memories using AI.

*   **Tagline:** Your Family’s Private AI Memory Keeper & Legacy Builder
*   **Core Promise:** Never lose your family’s stories again. Everything stays completely private to the people you invite.

### 2. Core Philosophy
*   **Privacy First:** 100% private by default. Only invited family members can see content. No public access unless explicitly shared.
*   **Simple Onboarding:** Users must be able to start fast with zero friction.
*   **Built for Generations:** Strong succession features so the family legacy continues even when members pass away.
*   **Emotional & Easy:** Designed for non-technical users aged 40–75.

### 3. Key Features (MVP – Phase 1: Must Have)
*   User creates a Family Collection in under 60 seconds.
*   Bulk upload: photos, videos, voice recordings, documents, zip files.
*   Smart AI auto-organization into timeline + albums.
*   Powerful conversational search (“Show me all photos of Grandpa fishing”, “What did Mom say about her wedding?”).
*   One-click Memory Book / PDF generator.
*   Family member invitations.
*   Basic sharing (internal + controlled external).

#### Important Rules

**Privacy:**
*   All collections are private by default.
*   Only invited members can view or add content.
*   External sharing is always intentional and controlled by the user.

**Legacy Guardians (Succession System):**
*   Creator starts as the only Guardian (for fast onboarding).
*   System gently encourages adding at least 2 more Guardians after user has uploaded content.
*   Minimum 3 Guardians strongly recommended for long-term protection.
*   Guardians have full management rights (invite members, manage billing, succession, etc.).
*   When a Guardian passes away, remaining Guardians can mark them as deceased and add replacements.

### 4. User Flow (Onboarding)
1.  Sign up / Create Family Collection.
2.  Name the collection (e.g. “Smith Family Legacy”).
3.  Automatically becomes first Guardian.
4.  Immediately able to upload content.
5.  Later nudges to add more Guardians (after 10–20 uploads or 7–14 days).

### 5. Import Capabilities
*   Easy bulk upload from phone/computer.
*   Folder upload + Zip file support.
*   Google Photos Picker integration.
*   Guided migration help from Google Photos, iCloud, etc.

### 6. Sharing Capabilities
*   Share individual memories or albums inside the family group.
*   Share to Facebook, Instagram, WhatsApp (beautiful formatted cards).
*   Private link sharing (with optional password).
*   All external sharing is opt-in with clear controls.

### 7. Pricing Tiers (Freemium)

| Plan | Price (CAD) | Max Members | Guardians | Storage Limit | AI Usage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Free** | $0 | 5 | 1–3 | 5 GB | Limited |
| **Family** | $12.99/mo or $119/yr | 15 | Up to 5 | 250 GB | 100/mo |
| **Legacy** | $19.99/mo or $189/yr | Unlimited | Up to 8 | 1 TB* | Unlimited |

*\*Additional storage blocks available (e.g., $5/mo per extra 500GB) to protect server margins.*

### 8. Tech Requirements
*   Progressive Web App (PWA) – Installable on phone and desktop.
*   Strong mobile experience.
*   Fast performance even with thousands of photos.
*   Private AI support (local models preferred where possible).
*   Stripe integration for payments + Canadian taxes.
*   Secure hosting with good Canadian privacy compliance.

### 9. Future Phases (After MVP)
*   AI Video Montages.
*   “Ask a Family Member” chatbot mode.
*   Printed book exports.
*   Anniversary memory reminders.
*   Advanced succession tools (digital executor settings).

### 10. Unit Economics & Profitability Strategy
To ensure Echoes remains highly profitable after all server and AI costs, "Unlimited Storage" has been replaced with generous, but strictly capped tiers. 
*   **Storage Costs (Cloudflare R2 / Backblaze B2):** Storage costs approximately $0.006 to $0.015 per GB. 
*   **Family Plan Margin:** At 250GB, our maximum storage cost is ~$1.50 - $3.75/month. At a $12.99/mo subscription, we retain a massive **70-88% gross margin**.
*   **AI Processing Costs:** AI tagging (the most expensive compute task) only happens *once* upon upload. Conversational searches use lightweight vector database queries (fractions of a cent per search).
*   **Result:** By preventing users from dumping 10 Terabytes of 4K video for a flat fee, Echoes becomes a highly scalable cash-cow with exceptional lifetime value (LTV).

### 11. Corporate Succession (The "Forever" Promise)
A product built on "Legacy" requires a company that will outlive its founder. To sell the promise that memories will be safe for generations, Just Me Media will implement a phased structural succession plan.

**Phase 1: The Server Endowment (Day 1)**
*   **Structure:** A dedicated, high-yield business savings account owned by Just Me Media. 
*   **Funding:** 5% of all Echoes subscription revenue is automatically diverted into this untouchable account.
*   **The "Dead Man's Switch":** An executor (spouse, trusted partner, or attorney) is given legal access *only* to this specific account and server credentials in the event of the founder's passing.
*   **The Goal:** The account holds enough capital to mathematically auto-pay Cloudflare/Backblaze server bills for 10+ years without requiring a single new customer.
*   **Cost:** $0 (Standard banking fees).

**Phase 2: The Data Trust (Year 3 - Scaling Phase)**
*   **Structure:** Transition the Endowment into a formal legal structure known as a **Perpetual Purpose Trust (PPT)** or **Data Trust** (similar to the Signal Foundation).
*   **Legal Purpose:** The Trust's operating agreement legally mandates that funds can *only* be used to maintain Echoes server infrastructure to protect user data.
*   **Management:** A Trustee (law firm, accounting firm, or board of operators) is appointed to manage the trust and pay server bills indefinitely if the founder passes away. They cannot legally liquidate the servers for profit.
*   **Cost:** $5,000 - $15,000 in legal setup fees.

**Marketing Advantage (The "Forever" Guarantee):**
We do not need to spend $15,000 on a lawyer to start marketing this on launch day. Our launch copy will read:
> *"A portion of every subscription goes directly into the Echoes Server Endowment. This is an untouchable financial reserve mathematically designed to keep our servers running for decades, even if our company stops accepting new users tomorrow. We aren't a startup that will run out of funding and delete your photos. Your legacy is mathematically protected."*
