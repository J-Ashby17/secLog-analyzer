import re
import os

import re._compiler

log_file_path = "test.log"

if not os.path.exists(log_file_path):
    with open(log_file_path, 'w') as file:
        file.write("Failed password for invalid user admin from 192.168.1.1\n")
        file.write("Failed password for root from 10.0.0.5\n")
        file.write("Failed password for invalid user test from 172.16.0.3\n")
    print(f"{log_file_path} was created with sample content.")
else:
    print(f"{log_file_path} already exists.")

def log_pass(log_file_path):
    with open(log_file_path, 'r') as file:
        logs = file.readlines()

    #regex for IP
    pattern = re.compile(r'Failed password for (?:invalid user )?(\w+) from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    failed_logins = {}

    #failed login counter 
    for log in logs:
        match = pattern.search(log)
        if match: 
            user = match.group(1)
            ip = match.group(2)
        
            #failed login ip appended to HM otherwise increment is increased
            if ip not in failed_logins:
                failed_logins[ip]=0
            failed_logins[ip] += 1

    for ip, count in failed_logins.items():
        if count > 3:
            print(f"Flagged activity from {ip} with {count} failed logins")

if __name__ == "__main__":
    log_pass(log_file_path)

