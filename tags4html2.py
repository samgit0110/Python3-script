#!/usr/bin/python3

def tags4html2():
	f=open('/home/shuhari/resource/index.html')
	tags=f.read()
	tags_list=[]
	upper=1
	#for i in range(0,len(tags),upper):
	while(tags.find('>')!=-1):
		temp=''
		lower=tags.find('<')
		upper=tags.find('>')
		temp+=tags[lower:upper+1]
		if(len(temp)>4):
			tags_list+=[temp]
		tags=tags.replace(tags[lower:upper+1],'')
	print(tags_list)





def main():
	tags4html2()





if __name__=='__main__':
	main()
