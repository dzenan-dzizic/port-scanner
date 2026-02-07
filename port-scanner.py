import socket
import re

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
21: "FTP",
22: "SSH (possible brute force attack, not guaranted)", 
23: "Telnet",
53: "DNS",
80: "HTTP",
443: "HTTPS",
587: "SMTP",
3389: "RDP (Remote Desktop Protocol)"

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

BASE_PORT = int(BASE_PORT)
END_PORT = int(END_PORT)


while BASE_PORT < END_PORT:

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((TARGET_IP_ADRESS, BASE_PORT))
        print("Connection success.")
        print(f"Port {BASE_PORT} open")
        open_port_counter += 1
        s.close()
    except socket.error as e:
        pass
    
    counter += 1
    BASE_PORT += 1


print("Scan finished")
print(f"{counter} ports scanned.")
print(f"{open_port_counter} ports are open")
