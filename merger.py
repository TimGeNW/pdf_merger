import PyPDF2
import os
import sys

# initialize PdfMerger-Object.
# iterate with for loop over sys.argv-list starting at element 1 not at element 0.
# only .pdf-files getting appended to the PdfMerger-Object.
# write files wchich are stored in the PdfMerger-Object to new files with the write()-Function.

def extract():
    PDF = PyPDF2.PdfMerger()
    lists = []
    while True:
        s = input('Drag and Drop File here (Press just Enter when you inserted desired files): ')
        lists.append(s)
        if s == True:
            s = input('Drag and Drop File here (Press just Enter when you inserted desired files): ')
            lists.append(s)
        elif s == '':
            break
            
    for i in lists:
        if i.endswith('.pdf'):
            PDF.append(i)


            
    PDF.write('new_merged.pdf')
    PDF.close()

extract()
