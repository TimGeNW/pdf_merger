import PyPDF2
import os
import sys

PDF = PyPDF2.PdfMerger()

for i in sys.argv[1::]:
    if i.endswith('.pdf'):
      

        PDF.append(sys.argv[1])
        PDF.append(sys.argv[2])

        PDF.write('test.pdf')

    else:
        print(f'{i} ---- is not a pdf-file ----')
