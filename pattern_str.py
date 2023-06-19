#!/usr/bin/python3

import re

def pattern_str():
	inp_str=input("Enter String ")
	inp_pattern=input("Enter Pattern ")
	x=re.search(inp_pattern,inp_str)
	if x:
	  print(x.group())
	else:
	 print('not found')


def main():
	pattern_str()

if __name__=='__main__':
	main() 

