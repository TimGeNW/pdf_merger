import PyPDF2
import os
import sys

# initialize PdfMerger-Object. Create aan empty list called lists
# while loop to insert as many pdf as wanted
# pdf-file is getting appended to empty list
# iterate with for loop over list(lists) to insert pdf file to PDF(PdfMerger)-Object
# create new merged file with write()-methode
# close PDF(PdfMerger)-Object with close()-methode

def extract():
    PDF = PyPDF2.PdfMerger()
    lists = []
    while True:
        s = input('Drag and Drop File here (Press just Enter when you inserted desired files): ')
        lists.append(s[:-1])
        if s == True:
            s = input('Drag and Drop File here (Press just Enter when you inserted desired files): ')
            lists.append(s[:-1])
        elif s == '':
            break
            
    for i in lists:
        if i.endswith('.pdf'):
            PDF.append(i)


            
    PDF.write('new_merged.pdf')
    PDF.close()

extract()
