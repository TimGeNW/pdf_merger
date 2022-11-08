import PyPDF2
import os

def check():
  for i in os.listdir(os.curdir):
      if i.endswith('.pdf'):

          PDF = PyPDF2.PdfReader(i)
          print(PDF.is_encrypted)
      
check()
