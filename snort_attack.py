#!/usr/bin/python3
import re
def snort_attack():
	f=open('/home/shuhari/resource/snort.log')
	line=f.readline()
	attack=[]
	while(line):
		x=re.findall('\] \w+ \[$',line)
		print(x)
		attack+=[x[1:len(x)]]
		line=f.readline()






def main():
	snort_attack()




if __name__=='__main__':
	main()
