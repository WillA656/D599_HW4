#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys
import re #Need to import this for the below regex use

# Use regex to verify if something is actually a word
#This is really the thing that makes the mapper/reducer combo actually work.
real_word = re.compile(r'\b\w+\b')

for line in sys.stdin:
    line = line.strip()
    words = real_word.findall(line)
    for word in words:
        print(f'{word.lower()}\t1') #Used f'' nomenclature for readability
