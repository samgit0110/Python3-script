#!/usr/bin/python3
import re

def mob_num():
	f=open('/home/shuhari/resource/details.txt')
	x=f.readline()
	res=[]
	while(x):
		y=re.findall('\d+',x)
		if(len(y)>=2):
			#print(y)
			mob_num='+'+''.join(y[0])+' '+''.join(y[1])
			res+=[mob_num]
		x=f.readline()
	print(res)





def main():
	mob_num()





if __name__=='__main__':
	main()
