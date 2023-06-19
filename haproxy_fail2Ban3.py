#!/usr/bin/python3

import re
import subprocess
from datetime import datetime, timedelta

# Define the HAProxy log file path
haproxy_log_file = "/var/log/haproxy.log"

# Define the threshold values
request_threshold = 10
time_window = timedelta(minutes=5)

# Define the regular expression pattern to extract IP addresses from log lines
ip_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

# Get the current time and the time threshold
current_time = datetime.now()
time_threshold = current_time - time_window

# Initialize a dictionary to store the request counts for each IP address
ip_counts = {}

# Open the HAProxy log file
with open(haproxy_log_file, 'r') as file:
    # Iterate over each line in the log file
    for line in file:
        # Extract the IP address from the log line
        match = re.search(ip_pattern, line)
        if match:
            ip_address = match.group(0)
        else:
            continue

        # Parse the timestamp from the log line
        timestamp_str = line.split()[0]
        timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")

        # Check if the timestamp is within the time window
        if timestamp >= time_threshold and timestamp <= current_time:
            # Update the request count for the IP address
            ip_counts[ip_address] = ip_counts.get(ip_address, 0) + 1

# Iterate over the IP addresses and block the ones exceeding the threshold
for ip_address, count in ip_counts.items():
    if count > request_threshold:
        # Block the IP address using Fail2ban
        command = f"sudo fail2ban-client set haproxy banip {ip_address}"
        subprocess.run(command, shell=True)
        print(f"Blocked IP address: {ip_address} (requests: {count})")
