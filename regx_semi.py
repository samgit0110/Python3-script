#!/usr/bin/python3
import re
def regex_semi():
	res=[]
	ls=['int num;', 'printf("Enter an integer:");', 'if(num % 2 == 0)', 'else', 'return 0;']
	print('Before regex')
	print('----------------- ')
	print(ls)
	print('After regex\n----------------------')
	for i in ls:
		x=re.findall(';$',i)
		if x:
		 res+=[i]
	print(res)
		





def main():
	regex_semi()





if __name__=='__main__':
	main()
