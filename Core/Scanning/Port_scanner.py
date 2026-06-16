import socket
import sys
import threading
import tqdm
import time


COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    5900: "VNC",
    8080: "HTTP-Alt"
}

class PortScanner:
    def __init__(self):
        self.ip = input("🎯 Please enter your IP Address: ")
        self.start_port = int(input("🔌 Please enter your start Port: "))
        self.end_port = int(input("🔌 Please enter your End Port: "))
        self.result_port = []
        self.lock = threading.Lock()

    def get_service_name(self , port):
        return COMMON_PORTS.get(port , "Unknown")

    def get_banner(self, sock):
        try:
            sock.settimeout(1)
            data = sock.recv(1024)
            return data.decode(errors='ignore').strip()
        except:
            return None

    def scan(self, port , ip):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((ip, port))
            service_name = self.get_service_name(port)
            banner = self.get_banner(s)
            s.close()
            return {
                "port": port,
                "service_name": service_name,
                "banner": banner
            }
        except:
            s.close()
            return None

    def scan_thread(self, port, ip):
        result = self.scan(port, ip)
        if result is not None:
            with self.lock:
                self.result_port.append(result)

    def run(self):
        threads = []
        for p in tqdm.tqdm(range(self.start_port, self.end_port + 1), desc="Processing Items", unit="item"):
            time.sleep(0.03)
            thread = threading.Thread(target=self.scan_thread, args=(p, self.ip ))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        if not self.result_port:
            print("🔒 No open ports found in the specified range.")
        else:
            for item in self.result_port:
                print(f"{item['port']} : {item['service_name']} : {item['banner']}")


scanner = PortScanner()
scanner.run()
