#in this tutorial will extract ip address from the text file
#!/usr/bin/python3
import re
def ip_address():
	ip_add=[]
	f=open('/home/shuhari/resource/syslog')
	line=f.readline()
	while(line):
		x=[]
		x=re.findall('(\d+\.\d+\.\d+\.\d+)',line)
		if(x!=[]):
			ip_add+=x
		line=f.readline()

	print(ip_add)





def main():
	ip_address()




if __name__=='__main__':
	main()
