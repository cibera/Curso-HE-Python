import pyfiglet
import sys
import socket
from datetime import datetime


def print_help():
    print(
        '''Welcome to PortScanner
        
            -h | --help | -H			Help and info about this tool
            -t | --target | -T 			Target host to scan (IP or domain)
            -p | --ports | -P   [22, 25, 80, ...] 	Ports to be scanned ALL BY DEFAULT [1 to 65535]
            ''')
    exit()


# ASCII Banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

ports = range(1, 65535)

# Defining a target
if len(sys.argv) >= 2:
    if sys.argv[1].lower() == '-h' or sys.argv[1].lower() == '--help':
        print_help()

    elif sys.argv[1].lower() == '-t' or sys.argv[1].lower() == '--target':
        # translate hostname to IPv4
        if len(sys.argv) >= 3:
            target = socket.gethostbyname(sys.argv[2])
            if len(sys.argv) >= 5:
                if sys.argv[3].lower() == '-p' or sys.argv[3].lower() == '--ports':

                    ports_str = sys.argv[4].strip().split(",")
                    try:
                        ports = []
                        for port in ports_str:
                            ports.append(int(port))
                    except Exception:
                        print_help()
        else:
            print_help()
    else:
        print_help()

elif len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print_help()

# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:

    # will scan ports between 1 to 65,535
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # returns an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Bye...")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved...")
    sys.exit()
except socket.error:
    print("\n Server not responding...")
    sys.exit()

