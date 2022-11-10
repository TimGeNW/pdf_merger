import PyPDF2
import os
import sys


# itereate over sys.argv-list starting at position 1
# only files with the .pdf file-extensions will be read by the PdfReader
# files with different file-extensions won't be read. Instead there is a ---- is not a pdf-file ---- output
# encrypted > true // not encrypted > false

def check():
  for i in sys.argv[1::]:
      if i.endswith('.pdf'):
          PDF = PyPDF2.PdfReader(i)
          print(PDF.is_encrypted)

      else:
          print(f'{i} ---- is not a pdf-file ----')

          
check()
