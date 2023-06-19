#!/usr/bin/python3
import re
def special_char():
	f=open('/home/shuhari/resource/ip_add.txt')
	spe_list=['!@#$%^&*<>.,:;']	
	spe_dict={}
	for i in list(spe_list[0]):
		spe_dict[i]=0
	line=f.readline()
	spe_list=re.compile(str(spe_list))
	while(line):
		x= spe_list.search(line)
		if x != None:
			val=spe_dict[x.group()]
			spe_dict[x.group()]=val+1
		line=f.readline()

	print(spe_dict)
			





def main():
	special_char()





if __name__=='__main__':
	main()
