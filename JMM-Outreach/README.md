# Just Me Media - AI Lead Machine

Automated, privacy-first cold outreach system.

## Project Structure
- `main.py`: Core engine. Handles scraping, Ollama generation, and Gmail SMTP sending.
- `database.py`: SQLite wrapper for `pipeline.db`.
- `prospect_loader.py`: Load leads from CSV into the pipeline.
- `scraper.py`: Extracts business context from prospect websites.
- `follow_up.py`: Sends automated 3-day follow-ups to non-responders.
- `reply_detector.py`: Monitors IMAP for replies and updates statuses.
- `dashboard.py`: Flask web dashboard at `localhost:5050`.

## Rate Limiting (Enforced)
- Max 20 emails per day.
- 4-minute gap between every send.

## Setup
1. Fill `.env` with your `GMAIL_APP_PASSWORD`.
2. Ensure Ollama is running `llama3.2:3b`.
3. Load leads: `python prospect_loader.py leads.csv`.
4. Run engine: `python main.py`.
5. View stats: `python dashboard.py`.
