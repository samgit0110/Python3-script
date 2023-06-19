#!/usr/bin/python3

import re
from datetime import datetime,timedelta
def haproxy_fail2Ban():
	ip_time_dict={}
	ip_cnt_dict={}
	f=open('/var/log/haproxy.log')
	line=f.readline()
	while(line):
		time=re.search('\d+\:\d+\:\d',line)
		ip_address=re.findall('\d+\.\d+\.\d+\.\d+',line)
		if (time !=[] and ip_address!=[]):
			if ip_address[0] not in ip_time_dict:
				ip_time_dict[ip_address[0]]= time[0]
			else:
				prev_time=ip_time_dict[ip_address[0]]
				now_time = time[0]
				format_string = "%H:%M:%S"
				prev_time = datetime.strptime(prev_time, format_string)
				now_time =  datetime.strptime(now_time, format_string)
				#hrs=int(now_time[0:2])-int(prev_time[0:2])
				#min= int(now_time[3:5])-int(prev_time[3:5])
				diff = now_time - prev_time
				#print(diff)
				five_min=timedelta(minutes=5)				
				if ip_address[0] not in ip_cnt_dict:			
							ip_cnt_dict[ip_address[0]]=1
				else:
					ip_cnt_dict[ip_address[0]]=ip_cnt_dict[ip_address[0]]+1
					if  diff > five_min:
						ip_cnt_dict[ip_address[0]]=0
					else ip_cnt_dict[ip_address[0]]>5 and diff <= five_min:
						print(ip_address,diff)
		line=f.readline()
	print(ip_cnt_dict)
def main():
	haproxy_fail2Ban()

if __name__=='__main__':
	main()
