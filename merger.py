import PyPDF2
import os
import sys

# initialize PdfMerger-Object.
# iterate with for loop over sys.argv-list starting at element 1 not at element 0.
# only .pdf-files getting appended to the PdfMerger-Object.
# write files wchich are stored in the PdfMerger-Object to new files with the write()-Function.

def merge():
    PDF = PyPDF2.PdfMerger()

    for i in sys.argv[1::]:
        if i.endswith('.pdf'):
            PDF.append(i)

        else:
            print(f'{i} ---- is not a pdf-file ----')

    PDF.write('test.pdf')
    PDF.close()

merge()
