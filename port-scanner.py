import socket
import os
import re

ipv4_pattern = re.compile(
    r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.'
    r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.'
    r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.'
    r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])$'
)


 
TARGET_IP_ADRESS = str(input("Enter a target IPv4 Adress: "))

while len(TARGET_IP_ADRESS) == 0:
    TARGET_IP_ADRESS = str(input("Empty field! Enter a target IPv4 Adress: "))

def check_IPv4(TARGET_IP_ADRESS):
    if ipv4_pattern.match(TARGET_IP_ADRESS):
        pass
    else:
        print("Enter a correct IPv4 Adress pattern")
        return 1

while len(TARGET_IP_ADRESS) == 0:
    TARGET_IP_ADRESS = str(input("Empty field! Enter a target IPv4 Adress: "))

BASE_PORT = int(input("Enter base range of the target ports: "))


END_PORT = int(input("Enter end range of the target ports: "))


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    print("Socket created successfully.")
except socket.error as err:
    print("Error.")


while BASE_PORT < END_PORT:

    try:
      
        s.connect((TARGET_IP_ADRESS, BASE_PORT))
        s.settimeout(2)
        print("Connection success.")
        print(f"Port {BASE_PORT} open")
        
    except socket.error as e:
        print("Connection failed.")
    
    
    BASE_PORT += 1
