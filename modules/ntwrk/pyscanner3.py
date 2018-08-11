import socket

def scan_host_ip():
    # scans the network host for open ports
    host = "192.168.1.1"
    lowPort = 1
    highPort = 65535
    ports = range(lowPort, highPort)
    for port in ports:
        try:
            #print("[+] Connecting to " + host + ":" + str(port))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.0000101125)
            result = s.connect_ex((host, port))
            #banner = s.recv(1024) # Will cause a timeout w/o a response
            if result == 0:
                print("  [*]OPEN " + host + ':' + str(port))
            s.close()
        except KeyboardInterrupt:
            quit()
