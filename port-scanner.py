import socket
import re
import datetime
import time
import os
import platform    
import subprocess

open_port_counter = 0
counter = 0


ipv4_pattern = re.compile(
    r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.'
    r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.'
    r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.'
    r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])$'
)

common_ports = {
    20: "FTP",
    #21: "FTP",
    #22: "SSH",
    #23: "Telnet",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    587: "SMTP",
    3389: "RDP (Remote Desktop Protocol)",
    8080: "HTTP-ALT"
}


TARGET_IP_ADRESS = str(input("Enter a target IPv4 Adress: "))


def check_IPv4_pattern(TARGET_IP_ADRESS):
    
        if ipv4_pattern.match(TARGET_IP_ADRESS):
            return TARGET_IP_ADRESS
        else:
            print("Enter a correct IPv4 Adress pattern")
            while ipv4_pattern.match(TARGET_IP_ADRESS) is None:
                TARGET_IP_ADRESS = str(input("Enter a correct target IPv4 Adress: "))
            return TARGET_IP_ADRESS

TARGET_IP_ADRESS = check_IPv4_pattern(TARGET_IP_ADRESS)


BASE_PORT = input("Enter base range of the target ports: ")
    
if BASE_PORT.isdigit() and int(BASE_PORT) <= 65535 and int(BASE_PORT) > 0:
    pass
else:
    while BASE_PORT.isdigit() == False or int(BASE_PORT) > 65535 or int(BASE_PORT) < 0:
        BASE_PORT = input("Enter a corect base range of the target ports (1-65535): ")


END_PORT = input("Enter end range of the target ports: ")
if END_PORT.isdigit() and int(END_PORT) <= 65535 and int(END_PORT) > 0:
    pass
else:
    while END_PORT.isdigit() == False or int(END_PORT) > 65535 or int(END_PORT) < 0:
        END_PORT = input("Enter a corect end range of the target ports: ")

if int(END_PORT) <= int(BASE_PORT):
    while END_PORT <= BASE_PORT:
        END_PORT = input("End port can't be smaller than base port!. Enter a corect end range of the target ports: ")

os.system('cls' if os.name == 'nt' else 'clear')

BASE_PORT = int(BASE_PORT)
END_PORT = int(END_PORT)


def ping_host(TARGET_IP_ADRESS):

    parameter =  '-n' if platform.system().lower() == 'windows' else '-c'

    result = subprocess.run(
        ["ping", parameter, "4", TARGET_IP_ADRESS],#pinging the target w 4 icmp packets
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL #hide the output w these two lines
    )

    if result.returncode == 0:
        print("Host is up.")
    else:
        print("The host is either down or blocking ping requests.")


def check_port_service(BASE_PORT):
    if BASE_PORT in common_ports:
        print(common_ports[BASE_PORT])
   
      
print(f"Starting the scan on target: {TARGET_IP_ADRESS}", end = "")  


current_time = datetime.datetime.now()

print(" at ",str(current_time)[:-7])

ping_host(TARGET_IP_ADRESS)

print("")
time.sleep(3)

def banner(s, BASE_PORT):
    try:
        
        return s.recv(1024).decode().strip()
        
    except socket.error as e:
       return "No banner"
    

while BASE_PORT <= END_PORT:

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((TARGET_IP_ADRESS, BASE_PORT))
        
        print(f"Port {BASE_PORT} open -> ",(banner(s, BASE_PORT)), end = " ")
        check_port_service(BASE_PORT)

        open_port_counter += 1
        s.close()

    except socket.timeout:
        pass
    except ConnectionRefusedError:
        pass
    
    counter += 1
    BASE_PORT += 1


print("")
print("Scan finished")
print(f"{counter} ports scanned.")
print(f"{open_port_counter} ports are open")
print("")
