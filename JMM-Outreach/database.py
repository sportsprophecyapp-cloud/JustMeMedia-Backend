import sqlite3
from datetime import datetime

DB_NAME = "pipeline.db"

def init_db():
    """Initializes the SQLite database with the leads table."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT NOT NULL,
            contact_name TEXT,
            contact_email TEXT NOT NULL UNIQUE,
            website TEXT,
            practice_areas TEXT,
            status TEXT DEFAULT 'pending', -- pending, generated, sent, replied
            generated_email TEXT,
            created_at DATETIME,
            sent_at DATETIME
        )
    ''')
    conn.commit()
    conn.close()

def add_lead(company_name, contact_name, contact_email, website, practice_areas):
    """Adds a new lead to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO leads (company_name, contact_name, contact_email, website, practice_areas, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (company_name, contact_name, contact_email, website, practice_areas, datetime.now()))
        conn.commit()
        print(f"Added lead: {contact_email}")
    except sqlite3.IntegrityError:
        print(f"Lead already exists: {contact_email}")
    finally:
        conn.close()

def get_pending_leads():
    """Retrieves all leads that haven't been emailed yet."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leads WHERE status = 'pending'")
    leads = cursor.fetchall()
    conn.close()
    return leads

def update_lead_status(lead_id, status, generated_email=None, sent_at=None):
    """Updates the status of a lead."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    if generated_email:
        cursor.execute("UPDATE leads SET status = ?, generated_email = ? WHERE id = ?", (status, generated_email, lead_id))
    elif sent_at:
        cursor.execute("UPDATE leads SET status = ?, sent_at = ? WHERE id = ?", (status, sent_at, lead_id))
    else:
        cursor.execute("UPDATE leads SET status = ? WHERE id = ?", (status, lead_id))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # If you run this file directly, it will just initialize the DB.
    init_db()
    print("Database initialized.")
