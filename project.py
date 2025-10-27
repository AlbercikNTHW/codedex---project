import socket

print("=== Python Port Scanner (By albercik from codedex <3) ===")
host = input("Target IP or hostname: ").strip()
start = int(input("Start port: "))
end = int(input("End port: "))

print(f"\nScanning {host} from port {start} to {end}...\n")

for port in range(start, end + 1):
    try:
        socket.create_connection((host, port), timeout=1)
        print(f"[OPEN]   Port {port}")
    except:
        print(f"[CLOSED] Port {port}")

print("\nScan finished.")
