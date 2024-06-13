#!/usr/bin/python3
# -*-coding:utf-8 -*
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

#This is pretty much unchanged from original script
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f'{current_word}\t{current_count}') #Used the f'' nomenclature for readability.
        current_count = count
        current_word = word