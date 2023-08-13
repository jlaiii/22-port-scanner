import socket

def check_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Adjust the timeout as needed
        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:
            return True
        else:
            return False

    except socket.error:
        return False

def main():
    print("Welcome to the SSH Port Checker")
    print("Drag and drop a text file containing IP addresses.")

    file_path = input("Drag and drop the text file here: ").strip()
    
    try:
        with open(file_path, "r") as file:
            ip_list = [line.strip() for line in file]
    except Exception as e:
        print(f"Error reading the file: {e}")
        return
    
    common_ports = [22]
    open_ips = []

    total_ips = len(ip_list)
    completed_ips = 0

    print("Scanning IP addresses:")
    with open("open_ports_results.txt", "w") as outfile:
        for ip in ip_list:
            completed_ips += 1
            progress = (completed_ips / total_ips) * 100

            print(f"Progress: {progress:.2f}%", end="\r")

            open_ports = []
            for port in common_ports:
                if check_port(ip, port):
                    open_ports.append(port)
                    result = f"IP: {ip}, Open Port: {port}"
                    open_ips.append(result)
                    print(result)
                    outfile.write(result + "\n")
                    outfile.flush()  # Flush the file buffer

    print("\nPort scanning completed. Results saved to open_ports_results.txt")
    print("Press Enter to exit...")
    input()  # Pause before exiting

if __name__ == "__main__":
    main()
