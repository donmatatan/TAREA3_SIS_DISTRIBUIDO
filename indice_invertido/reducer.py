#!/usr/bin/env python
# -*-coding:utf-8 -*
import sys

current_word = None
current_count = 0
current_doc = 0
word = None
palabra = None
printeado = False

for line in sys.stdin:
    line = line.strip()
    word, count, numDoc = line.split('\t',2)

    try:
        count = int(count)
        numDoc = int(numDoc)
    except ValueError:
        continue

    if (current_word == word) and (current_doc == numDoc):
        current_count += count
        
    elif (current_word == word) and (current_doc != numDoc) and printeado == False:
        palabra = current_word + "\t" + "(" + str(current_doc) + "," + str(current_count) + ")"
        printeado = True
        current_count = count
        current_doc = numDoc
    elif (current_word == word) and (current_doc != numDoc) and printeado == True:
        palabra = str(palabra) + "\t" + "(" + str(current_doc) + "," + str(current_count) + ")"
        current_count = count
        current_doc = numDoc
    elif (current_word != word):
        if printeado == False and current_word:    #primera iteración
            print(current_word + "\t" + "(" + str(current_doc) + "," + str(current_count) + ")")
        elif printeado == True and palabra:
            palabra = str(palabra) + "\t" + "(" + str(current_doc) + "," + str(current_count) + ")"
            print(palabra)
            palabra = None
            printeado = False
        current_word = word
        current_count = count
        current_doc = numDoc

if current_word == word:    #última iteración
    palabra = current_word + "\t" + "(" + str(current_doc) + "," + str(current_count) + ")"
    print(palabra)
    
