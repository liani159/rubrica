import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rubrica.settings")

import django
django.setup()

from django.core.management import call_command
from faker import Faker
from searcher.models import Utenti,Struttura
fakegen = Faker()

strutture = {"Area Didattica e Servizi alle Studentesse e agli Studenti":{
                "Ripartizione Didattica":
                    ["Ufficio Tutorato", "Unità Rete Manager Didattici", 
                    "Unità Supporto ai Manager Didattici"],
                "Ripartizione Segreterie e Servizi agli Studenti":
                    ["Ufficio Diritto allo Studio Studentesse e Studenti", 
                    "Ufficio Servizio SOS e digitalizzazione didattica", 
                    "Ufficio Orientamento, Welcome e Incoming", 
                    "Ufficio Immatricolazioni e Trasferimenti in ingresso", 
                    "Ufficio Carriere e Uscita"],
                "Ripartizione Tirocini, placement e alta formazione":
                    ["Ufficio Esami di Stato e scuole di specializzazione non sanitarie",
                    "Ufficio Tirocini e placement", "Ufficio Unife Master School"],
                "Ripartizione Tecnologie per la didattica":
                    ["Ufficio Presidi Informatici", 
                    "Ufficio Servizi e-learning e multimediali", 
                    "Ufficio Web"],
                "Ripartizione Didattica della Facoltà di Medicina, farmacia e prevenzione":
                    ["Ufficio Corsi di Studio della Facoltà di Medicina, Farmacia e Prevenzione", 
                    "Ufficio Tirocini sanitari"],

                }
                        }

def populate(strutture, N=5):

    for x, obj in strutture.items():
        #print(x+ '::\n')
        #pop("\t\t\t"+x)
        for j in range(0,5):
            nome, cognome, data_nascita, telefono, titolo, struttura=pop(x)
            Utenti.objects.create(nome=nome, cognome=cognome, data_nascita=data_nascita, telefono=telefono, titolo=titolo, struttura=struttura)
        #print("===============")
    
        for y in obj:
            print("\t"+y + ':\n')
            for j in range(0,5):
                nome, cognome, data_nascita, telefono, titolo, struttura=pop(y)
                Utenti.objects.create(nome=nome, cognome=cognome, data_nascita=data_nascita, telefono=telefono, titolo=titolo, struttura=struttura)
            print("===============")
            for i in obj[y]:
                #print("\t\t"+i)
                for j in range(0,5):
                    nome, cognome, data_nascita, telefono, titolo, struttura= pop(i)
                    Utenti.objects.create(nome=nome, cognome=cognome, data_nascita=data_nascita, telefono=telefono, titolo=titolo, struttura=struttura)
                #print("===============")


def pop(struttur,N=5):
    #for _ in range(N):
    #Create the fake data for that entry
    nome = fakegen.first_name()
    cognome = fakegen.last_name()
    telefono = fakegen.phone_number()
    data_nascita = fakegen.date_of_birth()
    titolo = fakegen.job()
    struttura = Struttura.objects.get(nome_struttura=struttur)
    return nome, cognome, data_nascita, telefono, titolo, struttura
        #print(nome, cognome, data_nascita, telefono, titolo, struttura)


def pop_struttra(strutture):
    for struttura_root, obj in strutture.items():
        #print(struttura_root+ '::\n')
        nome_struttura = struttura_root
        indirizzo = fakegen.address()
        struttura_padre = ""
        #print(nome_struttura+","+ indirizzo,","+ struttura_padre)
        Struttura.objects.create(nome_struttura=nome_struttura, indirizzo=indirizzo, struttura_padre=struttura_padre)

        for y in obj:
            #print("\t"+y + ':\n')
            nome_struttura = y
            indirizzo = fakegen.address()
            struttura_padre = struttura_root
            #print(nome_struttura+","+ indirizzo,","+ struttura_padre)
            Struttura.objects.create(nome_struttura=nome_struttura, indirizzo=indirizzo, struttura_padre=struttura_padre)

            for i in obj[y]:
        	    #print("\t\t"+i)
                nome_struttura = i
                indirizzo = fakegen.address()
                struttura_padre = y
                #print(nome_struttura+","+ indirizzo,","+ struttura_padre)
                Struttura.objects.create(nome_struttura=nome_struttura, indirizzo=indirizzo, struttura_padre=struttura_padre)


if __name__ == '__main__':
    print("populating script!")
    pop_struttra(strutture)
    populate(strutture, 5)
    #s = Struttura.objects.get(nome_struttura="ufficio web")
    #print(s.nome_struttura, s.struttura_padre)



