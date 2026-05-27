# Just Me Media — Website & Infrastructure Management
*The single source of truth for hosting, backend environments, email delivery, and deployment protocols.*

---

## 🌐 1. Domain Portfolio & DNS Mappings

| Domain | Purpose | DNS Registrar | Primary Nameservers / Target | Status |
| :--- | :--- | :--- | :--- | :--- |
| **`justmemedia.ca`** | Primary Studio Homepage | Namecheap | Render custom domain config (`justmemedia.ca` A/CNAME) | ✅ **Live** |
| **`lexsort.com`** | LexSort Invite-Only Page | Registrar Account | Netlify CDN (`75.2.60.5` CNAME/A record) | ✅ **Live** |

* **Namecheap Account (for `justmemedia.ca`):**
  * **Login Email:** `wcommu@hotmail.com`
  * **Username:** `ZEROBudget`
  * **Password:** `F7fhK6D_8,exmL/`

---

## 💻 2. Unified Hosting Solution: Render

*The frontend static files, assets, and backend APIs for the studio homepage run in a single, high-availability, unified Python/Flask service.*

* **Account Login:** `wcommu@gmail.com` (Google SSO)
* **Render Service Name:** `justmemedia-backend`
* **Production Service URL:** `https://justmemedia.ca`
* **Local Source Path:** `/Users/williamcommu/Desktop/JUST_ME_MEDIA_VAULT/01_STUDIO_CORE/JustMeMedia_Core`

### 🚀 Production Deployment Workflow
To deploy updates to both the frontend design and the backend APIs, simply commit and push your local changes to GitHub `origin main`. Render will automatically pull, rebuild, and hot-swap:
```bash
git add -A
git commit -m "Your deployment message"
git push origin main
```

*The dynamic backend endpoints (such as project inquiries and partner applications) run as a Python/Flask web service on Render.*

* **Account Login:** `wcommu@gmail.com` (Google SSO)
* **Render Service Name:** `justmemedia-backend`
* **Production Service URL:** `https://justmemedia-backend-fdgq.onrender.com`
* **Runtime:** `Python`
* **Start Command:** `gunicorn server:app`
* **Build Command:** `pip install -r requirements.txt`
* **Connected Repository:** `https://github.com/sportsprophecyapp-cloud/JustMeMedia-Backend.git`
* **Deployment Trigger:** Automatic build & deploy on every push to the `main` branch.

---

## ✉️ 4. Email Delivery: Resend API

*Contact forms are forwarded reliably using the Resend API (replacing blocked SMTP/Gmail settings).*

* **Account:** `wcommu@gmail.com` / `william@justmemedia.ca`
* **Credential:** `RESEND_API_KEY` (configured in Render environment variables)
* **Email Sender:** `Just Me Media <onboarding@resend.dev>`
* **Destination Address:** `william@justmemedia.ca`
* *Note: To send emails from custom `@justmemedia.ca` domain addresses, the domain must be verified in the Resend dashboard.*

---

## 🛡️ 5. Anti-Contamination Protocols (Safety Guidelines)

> [!WARNING]
> **PREVENTING DEPLOYMENT OVERWRITES**
>
> LexSort and Just Me Media both use Netlify, but they must **never** share local Netlify configuration states. A mistake here will overwrite the corporate homepage with the LexSort manual/landing page.

### 📋 Protocol A: Site Verification prior to Deploying
Before running a Netlify command in any workspace, check which site is currently bound to that directory:
```bash
npx -y netlify-cli status
```
Verify that the `Project URL` matches the expected destination (`https://justmemedia.ca` for JMM Core).

### 📋 Protocol B: Clear Duplicate Site IDs in LexSort
The LexSort landing page directory (`/Users/williamcommu/Desktop/Lexsort/website/`) must **never** point to the Just Me Media Site ID.
* The file `/Users/williamcommu/Desktop/Lexsort/website/.netlify/state.json` is intentionally cleared to avoid accidental pushes:
  ```json
  {
      "siteId": ""
  }
  ```

### 📋 Protocol C: Git Exclusion Guidelines
To prevent local Netlify workspace configurations and deployment caches from being tracked or merged across repositories, ensure the following is added to the `.gitignore` files in both directories:
```gitignore
# Netlify local environment
.netlify/
.netlify
```
*(Both project repositories have been updated with this exclusion rule).*

---
*Document maintained under the Just Me Media Studio Core framework.*  
*© 2026 William Commu / Just Me Media*
