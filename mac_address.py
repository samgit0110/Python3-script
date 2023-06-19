#!/usr/bin/python3
import re
def mac_address():
	mac_add=[]
	f=open('/home/shuhari/resource/mac.txt')
	line=f.readline()
	while(line):
		x=[]
#		x=re.findall('(\d+\.\d+\.\d+\.\d+)',line)
#		x=re.findall('\w+\:\w+\:\w+\:\w+\:\w+\:\w+',line)
		x=re.findall('\w+:\w+:\w+:\w+:\w+:\w+',line)
		if(x!=[]):
			mac_add+=x
		line=f.readline()

	print(mac_add)





def main():
	mac_address()




if __name__=='__main__':
	main()
