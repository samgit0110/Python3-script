#!/usr/bin/python3
import re
from datetime import datetime, timedelta

def haproxy_fail2Ban2():
    ip_time_dict = {}
    ip_cnt_dict = {}
    
    with open('/var/log/haproxy.log', 'r') as f:
        for line in f:
            time = re.search('\d+\:\d+\:\d', line)
            ip_address = re.findall('\d+\.\d+\.\d+\.\d+', line)
            
            if time and ip_address:
                if ip_address[0] not in ip_time_dict:
                    ip_time_dict[ip_address[0]] = time[0]
                else:
                    prev_time = ip_time_dict[ip_address[0]]
                    now_time = time[0]
                    format_string = "%H:%M:%S"
                    prev_time = datetime.strptime(prev_time, format_string)
                    now_time = datetime.strptime(now_time, format_string)
                    
                    diff = now_time - prev_time
                    five_min = timedelta(minutes=5)
                    
                    if ip_address[0] not in ip_cnt_dict:
                        ip_cnt_dict[ip_address[0]] = 1
                    else:
                        ip_cnt_dict[ip_address[0]] = ip_cnt_dict[ip_address[0]] + 1
                        if diff > five_min:
                            ip_cnt_dict[ip_address[0]] = 0
                        elif ip_cnt_dict[ip_address[0]] > 10 and diff <= five_min:
                            print(ip_cnt_dict,diff)

def main():
	haproxy_fail2Ban2()

if __name__=='__main__':
	main()
