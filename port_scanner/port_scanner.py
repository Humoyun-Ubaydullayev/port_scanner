import socket
import threading
from queue import Queue

target = "10.0.0.138"
queue = Queue()
open_port = []


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False
for port in range(1,1024):
    result = portscan(port)
    if result:
        print("port {} is open",format(port))
    else:
        print("port {} is closed",format(port))

def fill_queue(port_list):
    for in port_list:
        queue.put(port)
    
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("port {} is open",format,( port))
             open_ports.append(port)

port_list = range(1, 1024)
fill_queue(port_list)
        
thread_list = []

for i in range(500):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for theard in thread_list:
    thread.start()
    
for thread in thread_list:
    thread.join()
    
print("open ports are", open_port)
    
    
            
            
            
        