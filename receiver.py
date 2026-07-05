import socket
import json

BROADCAST_PORT = 5005

def start_adaptive_mesh_listener():
    print(f"[ADAPTIVE RECEIVER] Radio engine loaded. Scanning local frequencies on Port {BROADCAST_PORT}...")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', BROADCAST_PORT))
    
    last_processed_id = None
    
    try:
        while True:
            data, addr = sock.recvfrom(2048)
            
            try:
                packet = json.loads(data.decode('utf-8'))
                packet_id = packet.get("packet_id") if "packet_id" in packet else packet.get("id")
                
                if packet_id != last_processed_id and packet_id is not None:
                    mode = packet.get("mode", "STANDARD")
                    
                    print("\n" + "⚡"*20)
                    print(f"📡 INTERCEPTED ADAPTIVE PAYLOAD OVER AIRWAVES")
                    print(f"GRID NETWORK MODE: {mode}")
                    print(f"ALERT SIGNAL     : {packet.get('short_alert') if 'short_alert' in packet else packet.get('alert')}")
                    print(f"URGENCY STATUS   : {packet.get('urgency')}")
                    
                    if mode == "FULL":
                        print(f"DETAILED VECTOR  : {packet.get('escape_vector')}")
                        print(f"LOG TIMESTAMP    : {packet.get('time')}")
                    else:
                        print("⚠️ LOW-BANDWIDTH MODE: Detailed routing hidden to save node power. Evacuate following primary alert direction.")
                    
                    print("⚡"*20)
                    last_processed_id = packet_id
                    
            except Exception:
                print(f"\n[RAW PACKET ERROR]: {data.decode('utf-8')}")
                
    except KeyboardInterrupt:
        print("\n[RECEIVER] Disconnecting receiver socket loops cleanly.")
    finally:
        sock.close()

if __name__ == "__main__":
    start_adaptive_mesh_listener() 