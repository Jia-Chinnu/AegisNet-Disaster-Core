import socket
import time
import sqlite3
import json

DB_NAME = "offline_storage/aegis_ledger.db"
BROADCAST_PORT = 5005 

def get_latest_incident_packet():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, timestamp, urgency_level, escape_directions, broadcast_payload 
            FROM incident_logs 
            ORDER BY id DESC LIMIT 1
        """)
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                "packet_id": row[0],
                "time": row[1],
                "urgency": row[2],
                "escape_vector": row[3],
                "short_alert": row[4]
            }
        return {"short_alert": "AEGISNET GRID ACTIVE. STANDBY."}
    except Exception:
        return {"short_alert": "LEDGER STATE TEMPORARILY LOCKED."}

def check_system_energy_profile():
    try:
        packet = get_latest_incident_packet()
        if packet.get("urgency") == "CRITICAL":
            return 2, "FULL"
        return 6, "COMPRESSED"
    except Exception:
        return 10, "MINIMAL"

def start_adaptive_transmission_engine():
    print(f"[ADAPTIVE BEACON] Initializing Resilient Radio Broadcast Engine on Port {BROADCAST_PORT}...")
    
    # 1. Create a fully robust UDP socket configuration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    # 2. FIX: Instead of generic '<broadcast>', target your exact Mobile Hotspot Subnet Broadcast Lane
    # Since your laptop IP is 192.168.137.1, the network broadcast mask is exactly 192.168.137.255
    broadcast_destination = ('192.168.137.255', BROADCAST_PORT)

    try:
        while True:
            transmission_delay, operation_mode = check_system_energy_profile()
            packet_data = get_latest_incident_packet()
            
            if operation_mode == "COMPRESSED" or operation_mode == "MINIMAL":
                stripped_packet = {
                    "id": packet_data.get("packet_id", 0),
                    "alert": packet_data.get("short_alert", "SYSTEM ACTIVE"),
                    "urgency": packet_data.get("urgency", "NORMAL"),
                    "mode": operation_mode
                }
                payload_string = json.dumps(stripped_packet)
            else:
                payload_string = json.dumps(packet_data)
                
            print(f"[{operation_mode} MODE] Pulsing packet (Next cycle in {transmission_delay}s): {packet_data.get('short_alert')}")
            
            # 3. Securely encode data stream to avoid byte overflow drops
            sock.sendto(payload_string.encode('utf-8'), broadcast_destination)
            
            time.sleep(transmission_delay)
            
    except KeyboardInterrupt:
        print("\n[BEACON] Suspending all localized network radio pulses.")
    except Exception as e:
        print(f"\n[NETWORK CRITICAL ERROR] Radio socket blocked: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    start_adaptive_transmission_engine()