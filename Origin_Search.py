#!/bin/python3
import re
import sys

string = r'(?i)..herit\w+'
object = re.compile(string)

print('Opening origin.txt')
with open('origin.txt', 'r') as in_stream:
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
print("Done!")
print('origin.txt is closed?', in_stream.closed)
print('wordsearch.txt is closed?', out_stream.closed)