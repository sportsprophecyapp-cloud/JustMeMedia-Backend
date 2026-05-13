from flask import Flask, render_template_string, request
import sqlite3
import os
from database import DB_NAME

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>JMM Lead Dashboard</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #f4f7f6; padding: 40px; }
        .container { max-width: 1000px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; }
        .stats { display: flex; gap: 20px; margin-bottom: 30px; }
        .stat-card { flex: 1; background: #fff; border: 1px solid #ddd; padding: 15px; border-radius: 6px; text-align: center; }
        .stat-card h3 { margin: 0; font-size: 14px; color: #666; text-transform: uppercase; }
        .stat-card p { font-size: 24px; font-weight: bold; margin: 10px 0 0; color: #222; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { text-align: left; padding: 12px; border-bottom: 1px solid #eee; }
        th { background: #f9f9f9; }
        .status { padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; text-transform: uppercase; }
        .status-pending { background: #fff3cd; color: #856404; }
        .status-sent { background: #d1ecf1; color: #0c5460; }
        .status-followed_up { background: #cce5ff; color: #004085; }
        .status-replied { background: #d4edda; color: #155724; }
        .status-generated { background: #e2e3e5; color: #383d41; }
        .email-view { background: #f8f9fa; padding: 15px; border: 1px solid #ddd; margin-top: 20px; white-space: pre-wrap; display: none; }
    </style>
</head>
<body>
    <div class="container">
        <h1>JMM Lead Machine</h1>
        
        <div class="stats">
            <div class="stat-card"><h3>Total Leads</h3><p>{{ stats.total }}</p></div>
            <div class="stat-card"><h3>Sent Today</h3><p>{{ stats.sent_today }}</p></div>
            <div class="stat-card"><h3>Replies</h3><p>{{ stats.replied }}</p></div>
            <div class="stat-card"><h3>Pending</h3><p>{{ stats.pending }}</p></div>
        </div>

        <table>
            <thead>
                <tr>
                    <th>Company</th>
                    <th>Email</th>
                    <th>Status</th>
                    <th>Last Activity</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                {% for lead in leads %}
                <tr>
                    <td>{{ lead.company_name }}</td>
                    <td>{{ lead.contact_email }}</td>
                    <td><span class="status status-{{ lead.status }}">{{ lead.status }}</span></td>
                    <td>{{ lead.sent_at or 'N/A' }}</td>
                    <td><button onclick="viewEmail('{{ lead.id }}')">View Email</button></td>
                </tr>
                <tr id="email-{{ lead.id }}" style="display:none;"><td colspan="5"><div class="email-view">{{ lead.generated_email or 'No email generated yet.' }}</div></td></tr>
                {% endfor %}
            </tbody>
        </table>
    </div>

    <script>
        function viewEmail(id) {
            var el = document.getElementById('email-' + id);
            el.style.display = (el.style.display === 'none' || el.style.display === '') ? 'table-row' : 'none';
        }
    </script>
</body>
</html>
"""

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    leads = conn.execute('SELECT * FROM leads ORDER BY created_at DESC').fetchall()
    
    from datetime import datetime
    today = datetime.now().strftime('%Y-%m-%d')
    
    stats = {
        'total': conn.execute('SELECT COUNT(*) FROM leads').fetchone()[0],
        'sent_today': conn.execute("SELECT COUNT(*) FROM leads WHERE status IN ('sent', 'followed_up') AND sent_at LIKE ?", (f"{today}%",)).fetchone()[0],
        'replied': conn.execute("SELECT COUNT(*) FROM leads WHERE status = 'replied'").fetchone()[0],
        'pending': conn.execute("SELECT COUNT(*) FROM leads WHERE status = 'pending'").fetchone()[0],
    }
    
    conn.close()
    return render_template_string(HTML_TEMPLATE, leads=leads, stats=stats)

if __name__ == '__main__':
    app.run(port=5050, debug=True)
