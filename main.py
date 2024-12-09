import itertools
import datetime
from datetime import time
import sqlite3

conn=sqlite3.connect('Apdrosinasana.db')
cursor=conn.cursor()

class Pakalpojums:
    Pakalpojuma_kategorija=''
    Pakalpojuma_nosaukums=''
    Pakalpojuma_cena=''
    id_iter=itertools.count()

    def __init__(self, pak_kat=None, pak_nos=None, pak_atl=None, pak_cena=10):
        self.Pakalpojuma_id=next(self.id_iter)+1
        self.Pakalpojuma_kategorija=pak_kat
        self.Pakalpojuma_nosaukums=pak_nos
        self.Pakalpojuma_atlaide=pak_atl
        self.Pakalpojuma_cena_stunda=pak_cena
        self.Laiks_pieejams=True

    def Pakalpojuma_info(self):
        return[
            self.Pakalpojuma_kategorija, self.Pakalpojuma_nosaukums,
            self.Pakalpojuma_atlaide, self.Pakalpojuma_cena_stunda
        ]
    
    def Pakalpojuma_info_print(self):
        print('Pakalpojuma kategorija: ' +str(self.Pakalpojuma_kategorija))
        print('Pakalpojuma nosaukums: ' +str(self.Pakalpojuma_nosaukums))
        print('Pakalpojuma atlaide: ' +str(self.Pakalpojuma_atlaide))
        print('Pakalpojuma cena par stundu: ' +str(self.Pakalpojuma_cena_stunda))
        print('Laiks pieejams: '+str(self.Laiks_pieejams)+'\n')

class Klients:
    Klienta_vaards=''
    Klienta_uzvaards=''
    Klienta_PK=''
    #Klienta_auto_reg_num=''
    Klienta_tel_numurs=0

    id_iter_kl=itertools.count()

    def __init__(self,_klienta_id,_vaards, _uzvaards,_pk,_reg_num,_tel_numurs):
        #self.Klienta_id=next(self.id_iter_kl)+1
        self.Klienta_id=_klienta_id
        self.Klienta_vaards=_vaards
        self.Klienta_uzvaards=_uzvaards
        self.Klienta_PK=_pk
        #self.Klienta_auto_reg_num=_reg_num
        self.Klienta_tel_numurs=_tel_numurs
    def info():
        _klienta_id=int(input('Ievadiet klienta id: '))
        _vaards=input('Ievadi klienta vardu: ')
        _uzvaards=input('Ievadi klienta uzvardu: ')
        _pk=input('Ievadi klienta personas kodu: ')
        _tel_numurs=input('Ievadi klienta telefona numuru: ')

        cursor.execute('''INSERT INTO Klients (id_persona, vards, uzvards, p_k, tel_nr)VALUES (?,?,?,?,?)''',(_klienta_id,_vaards, _uzvaards,_pk,_tel_numurs) )
        print('Klients pievienots!')
        #cursor.execute('''INSERT INTO Transports (id_transports, auto_reg_num, modelis)VALUES (?,?,?)''', (14, '12.06', 14) )
        #print('Transports pievienots!')
        conn.commit()

    def klienta_info(self):
        return[
            self.Klienta_vaards, self.Klienta_uzvaards,self.Klienta_PK,self.Klienta_auto_reg_num,
            self.Klienta_tel_numurs 
        ]

    def Klienta_info_print():
        print('asdasd')
        cursor.execute('SELECT * FROM Klients')
        klienti=cursor.fetchall()
        print('Klienti:')
        for klienti in klienti:
            print(klienti)

    def find_klient_by_id():
        f=input('Ieraksti klienta ID kuru jus gribat atrast: ')
        cursor.execute(f"""SELECT * FROM Klients WHERE id_persona={f}""")
        conn.commit()
        klient=cursor.fetchall()
        for klients in klient:
            print(klients)
        c=input('Gribat atjaunot klienta telefonu?(y/n)')
        if c=='y':
            t=input('Ievadiet jauno telefonu: ')
            cursor.execute(f'''UPDATE Klients SET tel_nr={t}''')

        else:
            pass


    def delete_klient_by_id():
        d=input('Ieraksti klienta ID kuru jus gribat izdzēst: ')
        cursor.execute(f"""DELETE FROM Klients WHERE id_persona={d}""")
        conn.commit()
        print('Udalil')
'''        cursor.execute('SELECT id_persona FROM Klients')
        klienti=cursor.fetchall()
        for klienti in klienti:
            print(klienti)'''



         




class Izmantosana:
    Pakalpojuma_saakuma_laiks=0
    Pakalpojuma_beigu_laiks=0
    Pakalpojuma_datums=0
    Izmantosana_cena_stunda=10
    id_Pakalpojums=0
    id_Klients=0

    id_iter_izmantosana=itertools.count()

    def Cena_kopa(self):
        kopeeja_cena=self.Izmantosana_cena_stunda*((
            (self.Pakalpojuma_beigu_laiks - self.Pakalpojuma_saakuma_laiks)
        ))
        return kopeeja_cena
    
    
    def Izmantosana_imfo_print(self):
        print("Pakalpojuma sakuma laiks: " + str(self.Pakalpojuma_saakuma_laiks))
        print("Pakalpojuma beigu laiks: " + str(self.Pakalpojuma_beigu_laiks))
        print("Pakalpojums id: " + str(self.id_Pakalpojums))
        print("Klienta id: " + str(self.id_Klients))
        print("Pakalpojuma cena stunda, EUR: " + str(self.Izmantosana_cena_stunda) + "\n")

def main():
    #load_data()
    #find_organization_by_id()
    #count_organization()
   # list_organization_ids()
   #delete_organization_by_id()
    while (True):
        response=input('(1) Pievienot klientu (2) Izprentēt visus klientus (3)izdzēst klientu (4)Atrast klienta ar ID (5)Exit')
        if response=='1':
            Klients.info()         
        elif response=='2':
            Klients.Klienta_info_print()
            
        elif response=='3':
            Klients.delete_klient_by_id()
        
        elif response=='4':
            Klients.find_klient_by_id()

        elif response=='5':
            #save_data()
            print('Bye bye!')
            exit()
        else:
            print('Choose a number between 1-3')
            continue


main()


'''pak1=Pakalpojums("Auto apdrošināšana","Sudraba KASKO","10%",200) 
pak2=Pakalpojums("Moto apdrošināšana","OCTA","10%", 165)
pak3=Pakalpojums("Auto apdrošināšana","Platīna KASKO",'0%', 320)

print(pak1.Pakalpojuma_id)
pak1.Pakalpojuma_info()
pak1.Pakalpojuma_info_print()
print(pak2.Pakalpojuma_id)
pak2.Pakalpojuma_info()
pak2.Pakalpojuma_info_print()
print(pak3.Pakalpojuma_id)
pak3.Pakalpojuma_info()
pak3.Pakalpojuma_info_print()

Klients1=Klients('Aija','Zālīte','190490-11490','UL-8686', 29800789)   
Klients2=Klients('Janis','Ozols','030589-11430','AA-0101', 24852789)  
Klients3=Klients('Sintija','Molocko','260998-12215','VV-4444', 20898777)  

print(Klients1.Klienta_id)
Klients1.klienta_info()
Klients1.Klienta_info_print()
print(Klients2.Klienta_id)
Klients2.klienta_info()
Klients2.Klienta_info_print()
print(Klients3.Klienta_id)
Klients3.klienta_info()
Klients3.Klienta_info_print()'''