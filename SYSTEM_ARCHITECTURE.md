# Just Me Media — System Architecture & Deployment

## Core Infrastructure

This document outlines the production infrastructure for the Just Me Media web presence, established in May 2026. 

### Company Context
* **Founding:** Just Me Media was originally registered in 2022.
* **AI Evolution:** The agency expanded into Advanced AI development and bespoke software projects in early 2025.
* **Digital Presence:** This dedicated web infrastructure and landing page was developed and deployed in 2026 to support the new AI-focused partner network and sales pipeline.

The architecture below is designed for **Zero Monthly Cost**, high reliability, and maximum scalability.

### 1. Frontend (Static Hosting)
* **Provider:** Netlify
* **Domain:** `justmemedia.ca`
* **Workflow:** Drag-and-drop deployment via Netlify dashboard.
* **Configuration:** `netlify.toml` handles API proxying if necessary, but primary forms bypass Netlify completely to avoid 100-submission limits and forced CAPTCHAs.

### 2. Backend (API Server)
* **Provider:** Render (Dedicated Account: `william@justmemedia.ca`)
* **Repository:** `sportsprophecyapp-cloud/JustMeMedia-Backend` (Public)
* **Language/Framework:** Python 3.11 / Flask
* **Server:** Gunicorn (`gunicorn server:app`)
* **Role:** Processes form submissions, structures data, and securely communicates with external APIs without exposing keys to the frontend.
* **Resource Strategy:** Placed on its own dedicated free Render account to provide a fresh pool of 750 free hours/month. This ensures the backend can run 24/7 without consuming the primary account's resources (which are dedicated to TripSync).

### 3. Email Delivery (API)
* **Provider:** Resend (`resend.com`)
* **Integration:** Python `resend` library.
* **Why Resend?** Render's free tier blocks outbound SMTP traffic (ports 25, 465, 587) to prevent spam. Resend bypasses this by using standard REST API calls over port 443. 
* **Key:** Stored securely as an Environment Variable (`RESEND_API_KEY`) in the Render dashboard.

### 4. Uptime Monitoring
* **Provider:** UptimeRobot (Free)
* **Target:** `https://justmemedia-backend-fdgq.onrender.com/health`
* **Interval:** Every 5 minutes.
* **Purpose:** Render free instances sleep after 15 minutes of inactivity. Pinging the `/health` endpoint every 5 minutes ensures the server stays awake permanently, resulting in instant form submissions with zero timeout delays.

---

## Form Submission Flow
1. User submits Partner or Contact form on `justmemedia.ca`.
2. Frontend JavaScript (`js/main.js`) intercepts the submit event, preventing the default browser reload.
3. JS formats the data as JSON and performs a direct `fetch()` POST request to the Render backend URL.
4. Render receives the JSON, formats the email body, and passes it to the Resend API.
5. Resend delivers the email to `william@justmemedia.ca`.
6. Render returns a `200 OK` JSON response.
7. Frontend displays the green "Application Received" success state.

---

## Maintenance & Updates
* **Backend Updates:** Commit changes to the GitHub repository. Render will automatically pull and deploy the new code.
* **Frontend Updates:** Drag the updated `JustMe Media` folder into the Netlify dashboard.

*Note: Always ensure the Render backend is using Python 3.11 (via `.python-version`) to avoid compatibility issues with cutting-edge Python releases.*
