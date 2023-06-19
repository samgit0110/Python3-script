#!/usr/bin/python3

def word8():
	sent ='Find the words with exactly 8 letters Identify all the unique'
	for i in sent.split(' '):
		if(len(i)==8):
			print(i)




def main():
	word8()





if __name__=='__main__':
	main()
