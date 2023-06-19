#hello let find out number of tags from the html file
#!/usr/bin/python3

def  tags4html():
	tags_list=[]
	res_tags=''
	f=open('/home/shuhari/resource/index.html')
	tags=f.read()
	for i in range(0,len(tags)):
		res_tags=''
		if(tags[i]=='<'):
			res_tags+='<'
			for j in range(i+1,len(tags)):
				if(tags[j]=='>'):
					res_tags+='>'
					if(len(res_tags)>4):
						tags_list+=[res_tags]
						break
					else:
						break
				else:
					res_tags+=tags[j]
	print(tags_list)



def main():
	tags4html()



if __name__=='__main__':
	main()	
