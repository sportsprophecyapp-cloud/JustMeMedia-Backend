# Just Me Media | Master Studio Architecture
**Version:** 2026.05
**Standard:** Zero-Contamination / Sovereign Intelligence

## 1. Directory Structure (The Vault)
The studio's digital assets are organized into three primary silos to prevent cross-contamination:

### **01_STUDIO_CORE**
*   **Purpose:** Corporate operations and the master production backend.
*   **Key Assets:** `JustMeMedia_Core`, Production Server (`server.py`), Corporate Docs, Branding.

### **02_ACTIVE_PROJECTS**
*   **Purpose:** Development and client matter management.
*   **Current Silos:**
    *   `Certiorari`: Senior Partner Legal Terminal.
    *   `TripSync`: AI Travel Intelligence.
    *   `JMM-Outreach`: Automated Lead Generation.
    *   `SaaspricingDB`: Competitive Intelligence.

### **03_ASSETS_AND_TOOLS**
*   **Purpose:** Shared resources and dev-tooling.
*   **Key Assets:** 3D Icons, Branding Renders, Deployment Scripts.

## 2. Data Integrity Protocol (3-Tier Backup)
To ensure zero data loss and eliminate "Ghost Repositories," the studio follows the 3-Tier Protocol:

1.  **TIER 1 (WORKING):** `Desktop/JUST_ME_MEDIA_VAULT/` — The ONLY active development location.
2.  **TIER 2 (LOCAL):** `~/Documents/STUDIO_BACKUP_ARCHIVE/` — Weekly snapshots of Tier 1.
3.  **TIER 3 (EXTERNAL):** Physical SSD — Monthly cold-storage backups.

## 3. Deployment Standards
*   **Local Apps:** Must use "Self-Healing" `.command` launchers for one-click initialization.
*   **Cloud Apps:** Must include an **API Watchdog** (e.g., in `server.py`) to prevent 502 Gateway errors during configuration delays.
*   **AI Engine:** Standardized on local-first processing (Ollama/Llama 3.2) for maximum client confidentiality.

---
**Custodian:** Antigravity (AI Assistant)
**Owner:** Just Me Media
