import sqlite3
from datetime import datetime

DB_NAME = "offline_storage/aegis_ledger.db"

def init_db():
    """Generates the local SQLite file database ledger infrastructure completely offline."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incident_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            sender_id TEXT,
            raw_text TEXT,
            image_path TEXT,
            urgency_level TEXT,
            escape_directions TEXT,
            broadcast_payload TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_incident_to_ledger(sender_id, raw_text, image_path, ai_triage):
    """Safely commits the processed edge AI triage data into the persistent file ledger."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    urgency = ai_triage.get("urgency_level", "UNKNOWN")
    escape_directions = ai_triage.get("escape_directions", "Evacuate to open ground immediately.")
    broadcast_payload = ai_triage.get("broadcast_payload", "ALERT: SYSTEM PASSIVE.")
    
    cursor.execute("""
        INSERT INTO incident_logs 
        (timestamp, sender_id, raw_text, image_path, urgency_level, escape_directions, broadcast_payload)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (timestamp, sender_id, raw_text, image_path, urgency, escape_directions, broadcast_payload))
    
    conn.commit()
    conn.close()
    print(f"[LEDGER] Incident transaction securely logged to local offline storage file.")