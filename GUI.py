import PySimpleGUI as sg
from Database import Medlem
from funktioner import medlemsök, alla_medlemmar_lista, Funktioner, sub_windows

Medlem.create_database_table()

sg.theme('Dark Green 5')

förnamn_knapp = sg.Button('Förnamn', button_color='green')
efternamn_knapp = sg.Button('Efternamn', button_color='green')
gatuadress_knapp = sg.Button('Gatuadress', button_color='green')
id_knapp = sg.Button('ID', button_color='green')


layout1 = [[sg.Text(''), sg.Input(k='-IN2-', do_not_clear=False), sg.Button('Sök'), sg.Text('Välj mellan alternativen till höger vad du vill söka på'), förnamn_knapp, efternamn_knapp, gatuadress_knapp, id_knapp],
           [sg.Button('Exit', s = 16, button_color = 'tomato'), sg.Button('Alla medlemmar'), sg.Button('Refresh'), sg.Button('Lägg till medlem'), sg.Button('Radera medlem'), sg.Button('Uppdatera betalning')],
           [sg.Text('Förnamn', size=(30, 1), k='-1-'), sg.Text('Efternamn', size=(30, 1), k='-2-'), sg.Text('Gatuadress', size=(30, 1), k='-3-'), sg.Text('Postnummer', size=(30, 1), k='-4-'), sg.Text('Postadress', size=(30, 1), k='-2-'), sg.Text('ID', size=(30, 1), k='-3-'), sg.Text('Avgift', size=(30, 1), k='-4-')],
           [sg.Text('', size=(30, 30), k='-Sök1-'), sg.Text('', size=(30, 30), k='-Sök2-'), sg.Text('', size=(30, 30), k='-Sök3-'),sg.Text('', size=(30, 30), k='-Sök4-'), sg.Text('', size=(30, 30), k='-Sök5-'), sg.Text('', size=(30, 30), k='-Sök6-'),sg.Text('', size=(30, 30), k='-Sök7-')]]
            #Alla platser i tabellen är en tom sträng som är kopplade till en key i ett dictionary. Så varje plats i tabellen
            #blir åtkomlig genom sin key. Alla medlemmar sparas i en lista och kan därigenom skrivas ut i GUIN med hjälp av en for-loop.

window = sg.Window('Idrottsföreningen', layout1)

refreshlista = ['-Sök1-', '-Sök2-', '-Sök3-', '-Sök4-', '-Sök5-', '-Sök6-', '-Sök7-'] #lista med alla Keys i tabellen som man använder till Sök-funktionen och Alla_medlemmar() funktionen

förnamn = False
efternamn = False
gatuadress = False
id = False


def refresh1(): #Funktion som ritar en tom sträng på alla keys som ligger i tabellen

    for i, x in enumerate(refreshlista):
        window[x].update('')


while True:

    event, values = window.read()

    if event == 'Förnamn':
        förnamn_knapp.update(button_color='red') #Om man vill söka på Förnamn trycker man på den knappen och då blir knappen rödmarkerad och alla andra knappar blir gröna.
        efternamn_knapp.update(button_color='green')
        gatuadress_knapp.update(button_color='green')
        id_knapp.update(button_color='green')
        förnamn = True
        efternamn = False
        gatuadress = False
        id = False
    if event == 'Efternamn':
        efternamn_knapp.update(button_color='red') #Om man vill söka på Efternamn trycker man på den knappen och då blir knappen rödmarkerad och alla andra knappar blir gröna.
        förnamn_knapp.update(button_color='green')
        gatuadress_knapp.update(button_color='green')
        id_knapp.update(button_color='green')
        förnamn = False
        efternamn = True
        gatuadress = False
        id = False
    if event == 'Gatuadress':
        gatuadress_knapp.update(button_color='red') #Om man vill söka på Gatuadress trycker man på den knappen och då blir knappen rödmarkerad och alla andra knappar blir gröna.
        efternamn_knapp.update(button_color='green')
        förnamn_knapp.update(button_color='green')
        id_knapp.update(button_color='green')
        förnamn = False
        efternamn = False
        gatuadress = True
        id = False
    if event == 'ID':
        id_knapp.update(button_color='red') #Om man vill söka på ID trycker man på den knappen och då blir knappen rödmarkerad och alla andra knappar blir gröna.
        förnamn_knapp.update(button_color='green')
        efternamn_knapp.update(button_color='green')
        gatuadress_knapp.update(button_color='green')
        förnamn = False
        efternamn = False
        gatuadress = False
        id = True

    if event == 'Lägg till medlem':
        sub_windows.lägg_till() #kallar på en funktion i py-filen funktioner i klassen sub.windows

    if event == 'Refresh':

        refresh1()

    if event == 'Sök' and förnamn == True:

        refresh1()

        Funktioner.sök_förnamn(values['-IN2-']) #Skickar in förnamn och efternamn till funktionen sök()

        for i in range(0, len(medlemsök), 7):
            for j in range(7):
                window[refreshlista[j]].print(f'{medlemsök[i + j]}\n')

        if len(medlemsök):
            medlemsök.clear()

    if event == 'Sök' and efternamn == True:

        refresh1()

        Funktioner.sök_efternamn(values['-IN2-']) #Skickar in förnamn och efternamn till funktionen sök()

        for i in range(0, len(medlemsök), 7):
            for j in range(7):
                window[refreshlista[j]].print(f'{medlemsök[i + j]}\n')

        if len(medlemsök):
            medlemsök.clear()

    if event == 'Sök' and gatuadress == True:

        refresh1()

        Funktioner.sök_gatuadress(values['-IN2-']) #Skickar in förnamn och efternamn till funktionen sök()

        for i in range(0, len(medlemsök), 7):
            for j in range(7):
                window[refreshlista[j]].print(f'{medlemsök[i + j]}\n')

        if len(medlemsök):
            medlemsök.clear()

    if event == 'Sök' and id == True:

        refresh1()

        Funktioner.sök_id(values['-IN2-'])  # Skickar in förnamn och efternamn till funktionen sök()
        index = 0

        for i in range(0, len(medlemsök), 7):
            for j in range(7):
                window[refreshlista[j]].print(f'{medlemsök[i + j]}\n')

        if len(medlemsök):
            medlemsök.clear()

    if event == 'Alla medlemmar':
        Funktioner.alla_medlemmar() #Kallar på funktionen alla_medlemmar i filen funktioner.py
        refresh1()

        for i in range(0, len(alla_medlemmar_lista), 7): #Printar ut medlemmens sju attribut på sju olika ställen i tabellen sedan byter den rad och printar ut nästa medlems attribut osv.
            for j in range(7):
                window[refreshlista[j]].print(f'{alla_medlemmar_lista[i + j]}\n')

        if len(alla_medlemmar_lista):
            alla_medlemmar_lista.clear()

    if event == 'Radera medlem':
        sub_windows.radera_medlem()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if event == 'Uppdatera betalning':
        sub_windows.uppdatera_betalning()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
