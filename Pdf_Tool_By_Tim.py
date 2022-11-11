import PyPDF2
import os
import sys
from tqdm import tqdm
import time
import getpass

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


    with open('new_merged.pdf') as f:    
        PDF.write(f)
    
    time.sleep(2)
    
    intro()
    
    
    
 def enc():
    file = str(input('Ziehen Sie die zu enkryptende Pdf-File in das Terminal: '))
    reader = PyPDF2.PdfReader(file[:-1])
    writer = PyPDF2.PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
        
    writer.encrypt(getpass.getpass('Geben Sie ein Passwort ei: n'))
    
    with open(f'{file[:-1]}', 'wb') as f:
        writer .write(f)
    
    print('Encrypting Pdf-File... ')     
    for i in tqdm(range(47)):
        time.sleep(0.01)
    
    print('\n\nFile has been successfully encrypted !!!\n\n')
    time.sleep(2)
    
    intro()






def intro():
    introduction = ['PDF-TOOL by TIM\n\n', '1 --- Pdf-Dateien zusammenführen\n', '2 --- Pdf-Dateien enkrypten\n', '--\n', '--\n', 'Geben Sie die Nummer ein um eine der angeführeten Optionen zu wählen']

    for i in introduction:
        print(i)
    
    s = int(input('>>> '))
    
    if s == 1:
        extract()
    elif s == 2:
        enc()
    elif s == 3:
        print('Function3')
    elif s == 3:
        print('Function4')
    else:
        print('Ungültige Eingabe...')
        intro()
    
    
        


        
intro()
