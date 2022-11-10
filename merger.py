import PyPDF2
import os
import sys


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
