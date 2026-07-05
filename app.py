from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware  # <-- ADDED
from fastapi.responses import HTMLResponse
import shutil
import os
import uvicorn
import sqlite3
# Import the AI functions
from ai_engine import analyze_disaster_data
from database import init_db, save_incident_to_ledger

app = FastAPI(title="AegisNet Edge Core Engine")

# --- CORS MIDDLEWARE ALLOWS CORNER-CASE BROWSER PERMISSIONS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("offline_storage/images", exist_ok=True)
init_db()

@app.get("/", response_class=HTMLResponse)
async def serve_operator_dashboard():
    try:
        with open("dashboard.html", "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return "<h3>AegisNet Error: dashboard.html missing from root folder.</h3>"

@app.post("/emergency/report")
async def receive_emergency_report(
    text_message: str = Form(...),
    sender_id: str = Form(...),
    drone_image: UploadFile = File(None)
):
    saved_image_path = None

    if drone_image and drone_image.filename:
        saved_image_path = f"offline_storage/images/{drone_image.filename}"
        with open(saved_image_path, "wb") as buffer:
            shutil.copyfileobj(drone_image.file, buffer)

    # Call your local multimodal processing script loops
    ai_analysis = {
        "urgency_level": "UNKNOWN", 
        "escape_directions": "No explicit data. Seek higher ground.", 
        "broadcast_payload": "ALERT: EMERGENCY LOGGED."
    }
    
    if saved_image_path:
        ai_analysis = analyze_disaster_data(saved_image_path, text_message)
    else:
        # Fallback triage parameters if text message only is received
        ai_analysis = {
            "urgency_level": "HIGH" if "help" in text_message.lower() else "MEDIUM",
            "escape_directions": "Local AI mapping modules initializing. Evacuate to high ground immediately.",
            "broadcast_payload": "ALERT: Distress message received."
        }

    # Save the smart data packet permanently to our resilient local SQLite ledger
    save_incident_to_ledger(sender_id, text_message, saved_image_path, ai_analysis)

    payload = {
        "status": "Logged & Processed by Edge AI",
        "sender": sender_id,
        "text_raw": text_message,
        "image_path": saved_image_path,
        "ai_triage_decision": ai_analysis
    }
    
    print(f"\n[SERVER] Complete AI Processing Finished:\n{payload}")
    return {"message": "Incident processed completely offline", "data": payload}

# --- THIS IS THE KEY EXTENSION LINKING YOUR REACT DASHBOARD ---
@app.get("/status")
async def get_emergency_status():
    """Reads the persistent ledger and passes structural indices back to React."""
    try:
        conn = sqlite3.connect("offline_storage/aegis_ledger.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT urgency_level, escape_directions, broadcast_payload 
            FROM incident_logs 
            ORDER BY id DESC LIMIT 1
        """)
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                "urgency": row[0],
                "recommended_escape_route": row[1],
                "radio_broadcast_pulse": row[2]
            }
    except Exception as e:
        print(f"[STATUS FETCH ERROR]: {e}")
        
    return {
        "urgency": "STANDBY",
        "recommended_escape_route": "Sovereign Node Listening. No critical structural hazard maps received.",
        "radio_broadcast_pulse": "GRID STATUS: NOMINAL"
    }

# --- AUTOMATIC ENCRYPTION MECHANISM FOR TARGET NODE CHANNELS ---
if __name__ == "__main__":
    import datetime
    from cryptography import x509
    from cryptography.x509.oid import NameOID
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa

    # 1. Generate an on-the-fly certificate for your Hotspot IP
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, '192.168.137.1')])
    cert = x509.CertificateBuilder().subject_name(name).issuer_name(name).public_key(
        key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=365)
    ).sign(key, hashes.SHA256())

    # 2. Write them as temporary files so uvicorn can read them natively
    with open("temp_cert.pem", "wb") as f: f.write(cert.public_bytes(serialization.Encoding.PEM))
    with open("temp_key.pem", "wb") as f: f.write(key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.TraditionalOpenSSL, serialization.NoEncryption()))

    print("\n🚀 [AEGISNET SECURITY] Launching Secure Multi-Device HTTPS Channel...")
    uvicorn.run(
        "app:app", 
        host="0.0.0.0", 
        port=8000, 
        ssl_certfile="temp_cert.pem", 
        ssl_keyfile="temp_key.pem", 
        reload=True
    )