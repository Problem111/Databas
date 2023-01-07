from Database import Medlem, Database1
import PySimpleGUI as sg
from sqlalchemy import update

alla_medlemmar_lista = []
medlemsök = []
Database1.session = Database1.Session()  # Här skapas anslutningen till databasen och gör vårat table tillgängligt för t.ex inserts, deletes och selects


class Funktioner:
    no_match_id = 0

    @classmethod
    def delete(cls, id):

        results = Database1.session.query(Medlem).filter(
            Medlem.id == id).all()  # Skapar en query med en sql-sökning i som man kan loopa igenom
        for medlem1 in results:  # Letar om någon i registret har det specificerade id:t användaren har satt som input. Om det hittas så raderar den medlemmen.
            if medlem1 in results:
                print(f'{medlem1.förnamn} {medlem1.efternamn} har nu tagits bort ur registret.')
                medlem = Database1.session.query(Medlem).filter(Medlem.id == id).first()
                Database1.session.delete(medlem)
                Database1.session.commit()  # Committar alla ändringar till databasen
                return medlem1.förnamn, medlem1.efternamn

        if not results:  # Om inte medlems-id hittas i results
            print('Medlem finns inte i registret.')
            no_match_id = 1
            return no_match_id  # Detta kommer att göra att en if-sats i radera_medlem() funktionen blir sann och som gör ett nytt fönster där den ger ett errormeddelande
            # som säger att medlemen inte hittades

    @classmethod
    def kontroll_id(cls, id):

        results = Database1.session.query(Medlem).filter(Medlem.id == id).all()  # Skapar en query med en sql-sökning i som man kan loopa igenom
        for medlem1 in results:  # Letar om någon i registret har det specificerade id:t användaren har satt som input. Om det hittas så raderar den medlemmen.
            if medlem1 in results:
                return id

        if not results:  # Om inte medlems-id hittas i results
            print('Medlem finns inte i registret.')
            no_match_id = 1
            return no_match_id  # Detta kommer att göra att en if-sats i radera_medlem() funktionen blir sann och som gör ett nytt fönster där den ger ett errormeddelande
            # som säger att medlemen inte hittades

    @classmethod
    def uppdatera(cls, id, avgift):

        while True:

            if avgift == False:
                avgift = 'Betald'
                break
            if avgift == True:
                avgift = 'Inte betald'
                break

        session = Database1.Session()
        update_1 = update(Medlem, values={Medlem.avgift: avgift}).where(Medlem.id == id)  # Uppdaterar attributet Medlem.avgift till antingen Betald eller Inte betald beroende på vad man valde
        session.execute(update_1)
        session.commit()

    @classmethod
    def add(cls, förnamn, efternamn, gatuadress, postnummer, postadress, avgift):

        while True:

            if avgift == 0:
                avgift = 'Betald'
                break
            if avgift == 1:
                avgift = 'Inte betald'
                break

        while True:  # Kontrollerar om något av fälten förnamn eller efternamn är tomma. Isåfall kallar programmet på en klassmetod som ger ett errormeddelande
            if förnamn == '' or efternamn == '':
                sub_windows.error_parametrar()
                return print('')
            else:
                break

        objekt = 0
        medlemmar = []
        for y in medlemmar:  # kollar om objektnamnet är ledigt. Om det redan finns ett objekt i listan med det aktuella namnet så ökar den siffran med ett varje gång.
            if y == objekt:
                objekt += 1
            else:
                medlemmar.append(objekt)
                break
        session = Database1.Session()

        objekt = Medlem(förnamn, efternamn, gatuadress, postnummer, postadress, avgift)  # Skapar en instans i tablet Medlem
        print(f'En ny medlem {förnamn} {efternamn} har lagts till')
        session.add(objekt)
        session.commit()
        session.close()

    @classmethod
    def alla_medlemmar(cls):

        session1 = Database1.Session()
        results = session1.query(Medlem).all()  # Skapar en query med en sql-sökning i som man kan loopa igenom

        for medlem in results:  # Letar fram alla medlemmar i registret och appendar dem till en lista som skrivs ut i GUIN med en for loop
            alla_medlemmar_lista.append(medlem.förnamn)
            alla_medlemmar_lista.append(medlem.efternamn)
            alla_medlemmar_lista.append(medlem.gatuadress)
            alla_medlemmar_lista.append(medlem.postnummer)
            alla_medlemmar_lista.append(medlem.postadress)
            alla_medlemmar_lista.append(medlem.id)
            alla_medlemmar_lista.append(medlem.avgift)

    @classmethod
    def sök_förnamn(cls, förnamn):

        session1 = Database1.Session()
        results = session1.query(Medlem).filter(
            Medlem.förnamn == förnamn).all()  # Skapar en query med en sql-sökning i som man kan loopa igenom

        for medlem in results:
            medlemsök.append(
                medlem.förnamn)  # Alla matchningar med både för och efternamn i medlemsregistret appendas till listan "medlemsök"
            medlemsök.append(medlem.efternamn)
            medlemsök.append(medlem.gatuadress)
            medlemsök.append(medlem.postnummer)
            medlemsök.append(medlem.postadress)
            medlemsök.append(medlem.id)
            medlemsök.append(medlem.avgift)

    @classmethod
    def sök_efternamn(cls, efternamn):

        session1 = Database1.Session()
        results = session1.query(Medlem).filter(Medlem.efternamn == efternamn).all() # Skapar en query med en sql-sökning i som man kan loopa igenom

        for medlem in results:
            medlemsök.append(
                medlem.förnamn)  # Alla matchningar med både för och efternamn i medlemsregistret appendas till listan "medlemsök"
            medlemsök.append(medlem.efternamn)
            medlemsök.append(medlem.gatuadress)
            medlemsök.append(medlem.postnummer)
            medlemsök.append(medlem.postadress)
            medlemsök.append(medlem.id)
            medlemsök.append(medlem.avgift)

    @classmethod
    def sök_gatuadress(cls, gatuadress):

        session1 = Database1.Session()
        results = session1.query(Medlem).filter(Medlem.gatuadress == gatuadress).all() # Skapar en query med en sql-sökning i som man kan loopa igenom

        for medlem in results:
            medlemsök.append(
                medlem.förnamn)  # Alla matchningar med både för och efternamn i medlemsregistret appendas till listan "medlemsök"
            medlemsök.append(medlem.efternamn)
            medlemsök.append(medlem.gatuadress)
            medlemsök.append(medlem.postnummer)
            medlemsök.append(medlem.postadress)
            medlemsök.append(medlem.id)
            medlemsök.append(medlem.avgift)

    @classmethod
    def sök_id(cls, id):

        session1 = Database1.Session()
        results = session1.query(Medlem).filter(Medlem.id == id).all() # Skapar en query med en sql-sökning i som man kan loopa igenom

        for medlem in results:
            medlemsök.append(
                medlem.förnamn)  # Alla matchningar med både för och efternamn i medlemsregistret appendas till listan "medlemsök"
            medlemsök.append(medlem.efternamn)
            medlemsök.append(medlem.gatuadress)
            medlemsök.append(medlem.postnummer)
            medlemsök.append(medlem.postadress)
            medlemsök.append(medlem.id)
            medlemsök.append(medlem.avgift)


class sub_windows:

    @classmethod
    def radera_medlem(cls):
        while True:
            layout3 = [[sg.Text('ID:'), sg.Input(k='-ID-'), sg.Button('Radera')]]  # Skapar ett temporärt subwindow
            window2 = sg.Window('Radera medlemmar', layout3)
            event, values = window2.read()

            if event == sg.WIN_CLOSED:
                window2.close()
                break

            if event == 'Radera':
                result = Funktioner.delete(values['-ID-'])  # Skickar in integer till delete() som tar reda på vilken self.id den tillhör och sparar det i variabeln result
                # som ska avgöra om ett errorfönster ska visas eller inte beroende på om medlems-id:t finns eller inte

                window2['-ID-'].update('')
                window2.close()

                if result != 1:
                    layout5 = [[sg.Text(f'Medlemmen har tagits bort ur registret')]]  # Skapar ett temporärt subwindow
                    window4 = sg.Window('Errormeddelande1', layout5)
                    event, values = window4.read()

                    if event == sg.WIN_CLOSED:
                        window4.close()
                        break

                if result == 1:
                    layout4 = [[sg.Text('Vi hittade ingen match med detta id')]]
                    window3 = sg.Window('Errormeddelande', layout4)
                    event, values = window3.read()

                    if event == sg.WIN_CLOSED:
                        window3.close()
                        break

    @classmethod
    def lägg_till(cls):
        while True:

            layout2 = [[sg.Text('För att kunna lägga till en ny medlem så måste förnamn och efternamn fyllas i.\nResten av attributen är valfria.')],  # Skapar ett temporärt subwindow
                       [sg.Text('Förnamn:', s=15, justification='r'), sg.Input(k='-IN-')],
                       [sg.Text('Efternamn:', s=15, justification='r'), sg.Input(k='-IN1-')],
                       [sg.Text('Gatuadress:', s=15, justification='r'), sg.Input(k='-IN2-')],
                       [sg.Text('Postnummer:', s=15, justification='r'), sg.Input(k='-IN3-')],
                       [sg.Text('Postadress:', s=15, justification='r'), sg.Input(k='-IN4-')],
                       [sg.Text('Betalat avgiften?:', s=15, justification='r')],
                       [sg.Radio('Nej: ', group_id=1, key='-FEE-'), sg.Radio('Ja: ', group_id=1, key='-FEE-')],
                       [sg.Button('Lägg till')]]
            window1 = sg.Window('Lägga till medlemmar', layout2)
            event, values = window1.read()

            if event == sg.WIN_CLOSED:
                window1.close()
                break

            if event == 'Lägg till':
                Funktioner.add(values['-IN-'], values['-IN1-'], values['-IN2-'], values['-IN3-'],
                               values['-IN4-'],
                               values['-FEE-'])  # Skickar in all indata som parametrar till funktionen add()
                window1['-IN-'].update('')  # Nollställer key värden efter att de använts
                window1['-IN1-'].update('')
                window1.close()
                break

    @classmethod
    def error_parametrar(
            cls):  # Öppnar ett fönster med ett errormeddelande om användaren lämnar för eller efternamn tomt
        while True:

            layout5 = [[sg.Text('Förnamn och efternamn måste vara ifyllda')]]  # Skapar ett temporärt subwindow
            window4 = sg.Window('Errormeddelande2', layout5)
            event, values = window4.read()

            if event == sg.WIN_CLOSED:
                window4.close()
                break

    @classmethod
    def uppdatera_betalning(cls):  # Skapar ett temporärt subwindow
        while True:
            layout11 = [[sg.Text('Skriv in ID-numret på medlemmen du vill ända betalinfo på')],
                        [sg.Text('ID:'), sg.Input(k='-ID-'), sg.Button('Uppdatera')]]
            window12 = sg.Window('Uppdatera medlem', layout11)
            event, values = window12.read()

            if event == sg.WIN_CLOSED:
                window12.close()
                break

            if event == 'Uppdatera':
                result = Funktioner.kontroll_id(values['-ID-'])  # Skickar in integer till lägg_int_betalning1() som tar reda på vilken self.id den tillhör
                window12.close()

                if result != 1:  #Om användarens input finns i registret så skickas inputen som en parameter till funktionen uppdatera_betalning1
                    sub_windows.uppdatera_betalning1(values['-ID-'])
                    break

                if result == 1:  #Om avändarens input inte finns i registret över medlemmar så visas ett errormeddelande.
                    layout4 = [[sg.Text('Vi hittade ingen match med detta id')]]
                    window3 = sg.Window('Errormeddelande', layout4)
                    event, values = window3.read()

                    if event == sg.WIN_CLOSED:
                        window3.close()
                        break

    @classmethod
    def uppdatera_betalning1(cls, id):  # Skapar ett temporärt subwindow
        while True:

            session1 = Database1.Session()
            results = session1.query(Medlem).filter(Medlem.id == id).all()  # Skapar en query med en sql-sökning i som man kan loopa igenom

            for medlem in results:
                break

            layout8 = [[sg.Text(f'Förnamn: {medlem.förnamn}')],
                       [sg.Text(f'Efternamn: {medlem.efternamn}')],
                       [sg.Text(f'Gatuadress: {medlem.gatuadress}')],
                       [sg.Text(f'Postnummer: {medlem.postnummer}')],
                       [sg.Text(f'Postadress: {medlem.postadress}')],
                       [sg.Text(f'ID: {medlem.id}')],
                       [sg.Text('Betalat avgiften?:')],
                       [sg.Radio('Nej: ', group_id=1, key='-FEE1-'), sg.Radio('Ja: ', group_id=1, key='-FEE1-')],
                       [sg.Button('Uppdatera')]]
            window9 = sg.Window('Lägga till medlemmar', layout8)
            event, values = window9.read()

            if event == sg.WIN_CLOSED:
                window9.close()
                break

            if event == 'Uppdatera':
                Funktioner.uppdatera(medlem.id, values[
                    '-FEE1-'])  # Skickar in all indata som parametrar till funktionen uppdatera()
                window9.close()
                break
