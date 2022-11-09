import PyPDF2
import os
import sys

def check():
  for i in sys.argv[1::]:
      if i.endswith('.pdf'):

          PDF = PyPDF2.PdfReader(i)
          print(PDF.is_encrypted)

      else:
          print(f'{i} ---- is not a pdf-file ----')

          
check()
