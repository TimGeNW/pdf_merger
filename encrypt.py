import PyPDF2
import getpass
import time
from tqdm import tqdm 

# create reader and writer object
# append reader-object-pages to to writer-object
# encrypt pdf-file with encrypt-methode
# with open() to create new file which overrides input-file
# tqdm doesn't have any essential function


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


enc()

        
    
