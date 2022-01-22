# Py PDF Find
# created by: Earl Lamier
# python forum
# MAC
# v1.3.0
# 
# Using pdfplumber is easier, latest module, and works well

# status: release

#from cgi import print_directory
from asyncio import coroutines
import enum
from itertools import count
from multiprocessing.sharedctypes import Value
from operator import index
from re import search
from tkinter.messagebox import YES
from typing import Counter
import pdfplumber
import csv

pdf_file = open(r'/Users/doc/sample.pdf', mode='rb')
# pdf_file = open(r'/Users/doc/sample.pdf', mode='rb')
search_word = 'Page (5)'
header = ['Record','(Py)Start Page No.','Page No.']

with pdfplumber.open(pdf_file) as pdf, open('Output_Results.csv', 'w', newline='') as f_out:
    writer = csv.writer(f_out)
    pages = pdf.pages
    writer.writerow(header)
    rec = 1     

    for pageNumber, pg in enumerate(pages, 1):
        content = pg.extract_text()
        
        if search_word in content:               
            pyStartPageN = pageNumber - 5
            print("Index: {}, Search: {}, (Py)Start Page#: {}, Page#: {}".format(rec, search_word, pyStartPageN,pageNumber))
            #print(rec, search_word, pageNumber)
            writer.writerow([rec, pyStartPageN, pageNumber])
            rec = rec + 1 
print()
        
