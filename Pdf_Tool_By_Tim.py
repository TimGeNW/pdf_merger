













def intro():
    introduction = ['PDF-TOOL by TIM\n\n', '1 --- Pdf-Dateien zusammenführen\n', '2 --- Pdf-Dateien enkrypten\n', '--\n', '--\n', 'Geben Sie die Nummer ein um eine der angeführeten Optionen zu wählen']

    for i in introduction:
        print(i)
    
    s = int(input('>>> '))
    
    if s == 1:
        print('Function1')
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
