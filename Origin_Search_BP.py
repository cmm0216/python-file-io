#!/bin/python3
import re
import sys

string = r'(?i)..herit\w+'
object = re.compile(string)

def investigate(foo):
"""

Using this file & function will help you search for any word related to heritability!
All occurances of that type of word, as well as what line number it is on will be printed 
to a text file called "wordsearch.txt"
Hope this is helpful :) 

Parameters
___________
foo = an input file put in quotation marks when calling the function.

Examples
_________

>>>import Origin_Search_BP
>>>Origin_Search_BP.investigate("origin.txt")
Opening origin.txt
Opening wordsearch.txt
Input file is closed? True
wordsearch.txt is closed? True
>>>
"""
	string = r'(?i)..herit\w+'
	object = re.compile(string)

	print('Opening origin.txt')
	with open(foo, 'r') as in_stream:
		print('Opening wordsearch.txt')
		with open('wordsearch.txt','w') as out_stream:
			word_line = 1
			for line in in_stream:
				line = line.strip()
				word_list = line.split()
				if object.search(line):
					word = object.search(line)
					#print(word_line, "\t", word.group())
					print(word_line, "\t", word.group(), file = out_stream)
				word_line += 1
	print('Input file is closed?', in_stream.closed)
	print('wordsearch.txt is closed?', out_stream.closed)
if __name__ == "__main__":
	investigate(foo)

print("Done!")
