import time
import random

def show_message(message):
    """A simple function to display messages to the user."""
    print(f"\n--- {message} ---\n")

def port_scanner_module():
    """
    Simulated Port Scanner module.
    This function simulates scanning ports on a target IP/hostname.
    It does NOT perform actual network scans due to security restrictions
    and ethical considerations.
    """
    show_message("Port Scanner (Simulated)")
    target_ip = input("Enter Target IP/Hostname (e.g., 192.168.1.1 or example.com): ").strip()
    port_range_input = input("Enter Port Range (comma-separated, e.g., 80,443,22 or 1-1024): ").strip()

    if not target_ip or not port_range_input:
        show_message("Error: Please enter both a target IP/Hostname and a port range.")
        return

    ports_to_scan = []
    # Handle comma-separated list
    if ',' in port_range_input:
        ports_to_scan = [p.strip() for p in port_range_input.split(',') if p.strip().isdigit()]
    # Handle range (e.g., 1-1024)
    elif '-' in port_range_input:
        try:
            start_port, end_port = map(int, port_range_input.split('-'))
            if 1 <= start_port <= end_port <= 65535:
                ports_to_scan = [str(p) for p in range(start_port, end_port + 1)]
            else:
                show_message("Error: Invalid port range. Ports must be between 1 and 65535.")
                return
        except ValueError:
            show_message("Error: Invalid port range format. Use 'start-end' or 'port1,port2'.")
            return
    else: # Single port
        if port_range_input.isdigit():
            ports_to_scan = [port_range_input]
        else:
            show_message("Error: Invalid port format. Please enter a valid port number.")
            return

    if not ports_to_scan:
        show_message("Error: No valid ports to scan. Please check your input.")
        return

    print("\nStarting simulated scan...")
    print(f"Target: {target_ip}")
    print(f"Ports to simulate: {', '.join(ports_to_scan)}\n")

    open_ports = []
    closed_ports = []

    for port_str in ports_to_scan:
        port = int(port_str)
        if not (1 <= port <= 65535):
            print(f"Skipping invalid port: {port_str}")
            continue

        time.sleep(0.1)  # Simulate network delay

        # Simulate some common ports as open based on target_ip
        is_open = False
        if "example.com" in target_ip and (port == 80 or port == 443):
            is_open = True
        elif "192.168.1.1" in target_ip and (port == 22 or port == 80 or port == 3389):
            is_open = True
        elif random.random() > 0.8:  # 20% chance of being open for other cases
            is_open = True

        if is_open:
            open_ports.append(port)
            print(f"[+] Port {port} on {target_ip}: OPEN")
        else:
            closed_ports.append(port)
            print(f"[-] Port {port} on {target_ip}: CLOSED")

    print("\n--- Scan Complete! ---")
    print(f"Open Ports: {', '.join(map(str, open_ports)) if open_ports else 'None'}")
    print(f"Closed Ports: {len(closed_ports)}")
    print("----------------------\n")

def brute_forcer_module():
    """
    Simulated Brute-Forcer module.
    This function simulates brute-forcing login credentials.
    It does NOT perform actual login attempts due to security restrictions
    and ethical considerations.
    """
    show_message("Brute-Forcer (Simulated)")
    target_url = input("Enter Target URL (Login Page - e.g., https://example.com/login): ").strip()
    username = input("Enter Username (e.g., admin): ").strip()
    password_list_input = input("Enter Password List (comma-separated, e.g., password123,admin,123456): ").strip()

    if not target_url or not username or not password_list_input:
        show_message("Error: Please fill in all fields: Target URL, Username, and Password List.")
        return

    passwords = [p.strip() for p in password_list_input.split(',') if p.strip()]

    if not passwords:
        show_message("Error: Please provide a comma-separated list of passwords.")
        return

    print("\nStarting simulated brute-force attempt...")
    print(f"Target URL: {target_url}")
    print(f"Username: {username}")
    print(f"Passwords to try: {', '.join(passwords)}\n")

    found = False
    attempt_count = 0

    for password in passwords:
        if found:
            break # Stop if credentials are found

        attempt_count += 1
        time.sleep(0.5)  # Simulate network delay for each attempt

        # Simulate successful login for specific credentials
        is_success = (username == 'admin' and password == 'password123') or \
                     (username == 'test' and password == 'test')

        if is_success:
            print(f"[+] SUCCESS! Credentials found: Username: {username}, Password: {password}")
            found = True
        else:
            print(f"[-] Attempt {attempt_count}: Username: {username}, Password: {password} - Failed")

    if found:
        print("\n--- Brute-Force Complete! Found credentials. ---")
    else:
        print("\n--- Brute-Force Complete! No credentials found in the list. ---")
    print("-------------------------------------------------\n")

def main():
    """Main function to run the penetration testing toolkit."""
    print("-------------------------------------------------")
    print("   Welcome to the Penetration Testing Toolkit    ")
    print("-------------------------------------------------")
    print("Disclaimer: This toolkit provides *simulated* functionalities for educational purposes only.")
    print("It does NOT perform actual network attacks. Unauthorized access to computer systems is illegal and unethical.")
    print("Use these concepts responsibly and only on systems you have explicit permission to test.\n")

    while True:
        print("Select a module:")
        print("1. Port Scanner (Simulated)")
        print("2. Brute-Forcer (Simulated)")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            port_scanner_module()
        elif choice == '2':
            brute_forcer_module()
        elif choice == '3':
            print("Exiting Toolkit. Goodbye!")
            break
        else:
            show_message("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
