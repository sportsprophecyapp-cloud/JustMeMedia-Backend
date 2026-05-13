import os
import sqlite3
import time
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
from database import DB_NAME, update_lead_status
from prompt_templates import FOLLOW_UP_PROMPT
from main import send_email, get_sends_today, MAX_EMAILS_PER_DAY, SEND_GAP_SECONDS, GMAIL_USER, OLLAMA_URL, OLLAMA_MODEL
from scraper import scrape_website

load_dotenv()

def get_leads_for_follow_up():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Find leads sent more than 72 hours ago that haven't been followed up or replied to
    three_days_ago = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("SELECT * FROM leads WHERE status = 'sent' AND sent_at < ?", (three_days_ago,))
    leads = cursor.fetchall()
    conn.close()
    return leads

def generate_follow_up(lead):
    # We might need to scrape again or just use the company info. 
    # For better results, we'll try to re-scrape or use the previous info if we had it stored.
    # Currently we don't store scraped content in DB, so let's re-scrape or just use basic info.
    website_url = lead[4]
    website_content = scrape_website(website_url)
    
    prompt = FOLLOW_UP_PROMPT.format(
        company_name=lead[1],
        contact_name=lead[2] if lead[2] else "there",
        website_content=website_content
    )
    
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        print(f"Error generating follow-up for {lead[3]}: {e}")
        return None

def run_follow_ups():
    leads = get_leads_for_follow_up()
    if not leads:
        print("No leads eligible for follow-up today.")
        return

    print(f"Found {len(leads)} leads for follow-up.")
    
    for lead in leads:
        if get_sends_today() >= MAX_EMAILS_PER_DAY:
            print("Daily send limit reached. Skipping remaining follow-ups.")
            break
            
        lead_id = lead[0]
        company_name = lead[1]
        contact_email = lead[3]
        
        print(f"\n--- Following up with: {company_name} ({contact_email}) ---")
        
        body = generate_follow_up(lead)
        if body:
            subject = f"Re: Quick question regarding {company_name}"
            if send_email(contact_email, subject, body):
                print(f"Follow-up sent to {contact_email}.")
                update_lead_status(lead_id, 'followed_up', sent_at=datetime.now())
                time.sleep(SEND_GAP_SECONDS)
            else:
                print(f"Failed to send follow-up to {contact_email}.")
        else:
            print("Failed to generate follow-up text.")

if __name__ == "__main__":
    run_follow_ups()
