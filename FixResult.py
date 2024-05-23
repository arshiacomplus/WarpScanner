import socket
from concurrent.futures import ThreadPoolExecutor
import time

results = []

def scan_ip_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            start_time = time.time()
            result = s.connect_ex((ip, port))
            end_time = time.time()
            if result == 0:
                elapsed_time = (end_time - start_time) * 1000
                results.append((ip, port, elapsed_time))
            else:
                print(f"IP: {ip} Port: {port} is not responding or closed.")
    except Exception as e:
        print(f"Error scanning {ip}:{port} - {e}")

def create_ip_range(start_ip, end_ip):
    start = list(map(int, start_ip.split('.')))
    end = list(map(int, end_ip.split('.')))
    temp = start[:]
    ip_range = []

    while temp != end:
        ip_range.append('.'.join(map(str, temp)))
        temp[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 256:
                temp[i] = 0
                temp[i-1] += 1
    ip_range.append(end_ip)
    return ip_range

def main():
    start_ip = "188.114.96.1"
    end_ip = "188.114.98.224"
    ports = [1074, 894]
    ip_range = create_ip_range(start_ip, end_ip)

    with ThreadPoolExecutor(max_workers=200) as executor:
        for ip in ip_range:
            for port in ports:
                executor.submit(scan_ip_port, ip, port)

    executor.shutdown(wait=True)

    sorted_results = sorted(results, key=lambda x: x[2])

    for result in sorted_results[:10]:
        print(f"IP: {result[0]}, Port: {result[1]}, Ping: {result[2]:.2f} ms")

    
    if sorted_results:
        best_result = sorted_results[0]
        print(f"nBest ping: IP: {best_result[0]}, Port: {best_result[1]}, Ping: {best_result[2]:.2f} ms")

if __name__ == "__main__":
    main()
