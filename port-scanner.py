import socket
import re

ipv4_pattern = re.compile(
    r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.'
    r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.'
    r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.'
    r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])$'
)

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
    
if BASE_PORT.isdigit():
    pass
else:
    while BASE_PORT.isdigit() == False:
        BASE_PORT = input("Enter a corect base range of the target ports: ")


END_PORT = input("Enter end range of the target ports: ")
if END_PORT.isdigit():
    pass
else:
    while END_PORT.isdigit() == False:
        END_PORT = input("Enter a corect end range of the target ports: ")

BASE_PORT = int(BASE_PORT)
END_PORT = int(END_PORT)

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
