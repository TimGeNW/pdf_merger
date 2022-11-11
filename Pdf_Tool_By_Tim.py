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


    with open('new_merged.pdf') as f:    
        PDF.write(f)
    















def intro():
    introduction = ['PDF-TOOL by TIM\n\n', '1 --- Pdf-Dateien zusammenführen\n', '2 --- Pdf-Dateien enkrypten\n', '--\n', '--\n', 'Geben Sie die Nummer ein um eine der angeführeten Optionen zu wählen']

    for i in introduction:
        print(i)
    
    s = int(input('>>> '))
    
    if s == 1:
        extract()
    elif s == 2:
        print('Function2')
    elif s == 3:
        print('Function3')
    elif s == 3:
        print('Function4')
    else:
        print('Ungültige Eingabe...')
        intro()
    
    
        


        
intro()
