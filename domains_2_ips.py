import sys
import socket
from termcolor import colored

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return None

def main(file_path):
    with open(file_path, 'r') as file:
        domains = file.readlines()

    for domain in domains:
        domain = domain.strip()
        ip = get_ip(domain)
        if ip:
            print(colored(f"{domain}:", 'red'), colored(ip, 'green'))
        else:
            print(colored(f"{domain}:", 'red'), colored("Not found", 'red'))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ip_rev.py <domains_file>")
    else:
        main(sys.argv[1])
