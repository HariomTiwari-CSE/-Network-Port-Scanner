#!/usr/bin/env python3
import socket
import sys
from datetime import datetime

def scan_port(ip, port):
    """Scan a single port on target IP"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print(f"[+] Port {port:5d}: OPEN")
            return True
        # Uncomment to see closed ports:
        # else:
        #     print(f"[-] Port {port:5d}: CLOSED")
        
        sock.close()
        return False
        
    except Exception as e:
        return False

def scan_common_ports(target):
    """Scan a list of common service ports"""
    print("-" * 50)
    print(f"Scanning target: {target}")
    print(f"Started: {datetime.now()}")
    print("-" * 50)
    
    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        135: "MS RPC",
        139: "NetBIOS",
        143: "IMAP",
        443: "HTTPS",
        445: "SMB",
        3306: "MySQL",
        3389: "RDP",
        8080: "HTTP-Alt"
    }
    
    open_ports = []
    
    for port, service in common_ports.items():
        if scan_port(target, port):
            open_ports.append((port, service))
    
    return open_ports

def main():
    """Main function"""
    print("\n" + "="*50)
    print("        BASIC PORT SCANNER")
    print("="*50)
    
    # Get target
    target = input("Enter IP or hostname (default: scanme.nmap.org): ").strip()
    if not target:
        target = "scanme.nmap.org"
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[!] Error: Cannot resolve hostname")
        sys.exit(1)
    
    print(f"\nTarget IP: {target_ip}")
    print("Scanning common ports (15 ports)...")
    
    open_ports = scan_common_ports(target_ip)
    
    # Results summary
    print("\n" + "-" * 50)
    print("SCAN RESULTS:")
    print("-" * 50)
    
    if open_ports:
        print(f"Found {len(open_ports)} open port(s):")
        for port, service in open_ports:
            print(f"  • Port {port}: {service}")
    else:
        print("No open ports found in common port list.")
    
    print(f"\nScan completed at: {datetime.now()}")
    print("="*50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user (Ctrl+C)")
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error: {e}")
