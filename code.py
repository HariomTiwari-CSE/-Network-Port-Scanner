#!/usr/bin/env python3

import socket
import sys
from datetime import datetime

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)  # Timeout in seconds
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        sock.close()
        
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user")
        sys.exit()
    except socket.gaierror:
        print("[!] Hostname could not be resolved")
        sys.exit()
    except socket.error:
        print("[!] Could not connect to server")
        sys.exit()

# Main execution
if __name__ == "__main__":
    target = input("Enter IP to scan: ") or "127.0.0.1"
    
    print("-" * 50)
    print(f"Scanning target: {target}")
    print(f"Scan started: {datetime.now()}")
    print("-" * 50)
    
    for port in [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389]:
        scan_port(target, port)
    
    print(f"\nScan completed: {datetime.now()}")
