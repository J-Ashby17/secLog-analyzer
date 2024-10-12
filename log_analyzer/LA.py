import re

import re._compiler

log_file_path = "C:/Users/Jackson/source/repos/test.log"

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
            user = match.group(2)
            ip = match.group(3)
        
            #failed login ip appended to HM otherwise increment is increased
            if ip not in failed_logins:
                failed_logins[ip]=0
            failed_logins[ip] += 1

    for ip, count in failed_logins.items():
        if count > 3:
            print(f"Flagged activity from {ip} with {count} failed logins")

if __name__ == "__main__":
    log_pass(log_file_path)

