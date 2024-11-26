import socket
from datetime import datetime

def port_scanner(target, start_port, end_port):
    print(f"Scanning Target: {target}")
    print(f"Scanning Ports: {start_port}-{end_port}")
    print(f"Start Time: {datetime.now()}\n")
    
    # Try to resolve the target to an IP address
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname {target}")
        return
    
    print(f"Resolved IP: {target_ip}\n")
    
    # Iterate through the specified port range
    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Set timeout for faster scanning
                s.settimeout(0.5)
                # Try connecting to the port
                result = s.connect_ex((target_ip, port))
                
                # If the port is open
                if result == 0:
                    print(f"Port {port}: OPEN")
        except KeyboardInterrupt:
            print("\nScan stopped by user.")
            return
        except Exception as e:
            print(f"Error on port {port}: {e}")
            continue

    print(f"\nScanning completed at: {datetime.now()}")

# Example usage
if __name__ == "__main__":
    print("Simple Port Scanner")
    print("-" * 20)
    target_host = input("Enter target (IP or hostname): ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))
    
    port_scanner(target_host, start_port, end_port)
