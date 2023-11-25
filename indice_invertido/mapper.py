#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys
import re

numLinea = 0
numDoc = 0

substring = ".txt"

for line in sys.stdin:
    if (line != "") and (substring in line):
        numLinea = numLinea + 1
        #line = re.sub(r'\W+',' ',line.strip())
        words = line.split('.')
        numDoc = words[len(words) - 2]
        numDoc = int(numDoc)
    else:

        line = re.sub(r'\W+',' ',line.strip())
        words = line.split()

        for word in words:
            #hola = "hola"
            print('{}\t{}\t{}'.format(word,1,numDoc))

