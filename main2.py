import itertools
import datetime
from datetime import time
import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import *

conn=sqlite3.connect('Apdrosinasana.db')
cursor=conn.cursor()

def pievienot_klientu():
    def saglabat_klientu():
        vards = vards_entry.get()
        uzvards = uzvards_entry.get()
        p_k = p_k_entry.get()
        tel_nr = tel_nr_entry.get()
        id_klienta = id_klienta_entry.get()

        if vards and uzvards and p_k and tel_nr and id_klienta.isdigit():
            cursor.execute(
                "INSERT INTO Klients (vards, uzvards,p_k, tel_nr, id_klienta) VALUES (?, ?, ?, ?, ?)",
                (vards, uzvards, p_k, tel_nr, id_klienta)
            )
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Klients pievienots!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    logs = tk.Toplevel()
    logs.title("Pievienot klientu")
    logs.geometry("300x300")

    tk.Label(logs, text="Vārds:").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    tk.Label(logs, text="Uzvārds:").pack()
    uzvards_entry = tk.Entry(logs)
    uzvards_entry.pack()

    tk.Label(logs, text="Personas kods:").pack()
    p_k_entry = tk.Entry(logs)
    p_k_entry.pack()

    tk.Label(logs, text="Tālrunis:").pack()
    tel_nr_entry = tk.Entry(logs)
    tel_nr_entry.pack()

    tk.Label(logs, text="ID:").pack()
    id_klienta_entry = tk.Entry(logs)
    id_klienta_entry.pack()

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_klientu)
    saglabat_btn.pack(pady=10)

def meklet_klientu():
    def atrast_klientu():
        vards = vards_entry.get()
        if vards:
            cursor.execute("SELECT * FROM Klients WHERE vards LIKE ?", (f"%{vards}%",))
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}, {r[4]}, {r[5]}\n"
            else:
                messagebox.showinfo("Rezultāti", "Netika atrasts neviens klients.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet klienta vārdu!")

    logs = tk.Toplevel()
    logs.title("Meklēt klientu")
    logs.geometry("300x200")

    tk.Label(logs, text="Klienta vārds:").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atrast_klientu)
    meklēt_btn.pack(pady=10)    

def dzest_klientu():
    def dzest_klientu_no_db():
        id_klienta = id_klienta_entry.get()
        if id_klienta.isdigit():
            cursor.execute("DELETE FROM Klients WHERE id_klienta = ?", (id_klienta,))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", f"Klients ar ID {id_klienta} tika izdzēsts!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet derīgu ID!")

    logs = tk.Toplevel()
    logs.title("Dzēst klientu")
    logs.geometry("300x150")

    tk.Label(logs, text="klienta ID:").pack()
    id_klienta_entry = tk.Entry(logs)
    id_klienta_entry.pack()

    dzēst_btn = tk.Button(logs, text="Dzēst", command=dzest_klientu_no_db)
    dzēst_btn.pack(pady=10)    

def klienta_logs():
    transporta_logs = tk.Toplevel()
    transporta_logs.title("Klientu saraksts")
    transporta_logs.geometry("300x250")

    pievienot_btn = tk.Button(transporta_logs, text="Pievienot klientu", command=pievienot_klientu, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(transporta_logs, text="Meklēt klientu pēc ID", command=meklet_klientu, width=25, height=2, bg="lightgreen")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(transporta_logs, text="Dzēst KLIENTU", command=dzest_klientu, width=25, height=2, bg="lightyellow")
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(transporta_logs, text="Iziet", command=transporta_logs.destroy, width=25, height=2, bg="red", fg="white")
    iziet_btn.pack(pady=10)        

def pievienot_transportu():
    def saglabat_Transports():
        id_transports = id_transports_entry.get()
        auto_reg_num = auto_reg_num_entry.get()
        modelis = modelis_entry.get()

        if id_transports and auto_reg_num and modelis:
            cursor.execute(
                "INSERT INTO Transports (id_transports, auto_reg_num, modelis) VALUES (?, ?, ?)",
                (id_transports, auto_reg_num, modelis))
            
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Transportss pievienots!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    logs = tk.Toplevel()
    logs.title("Pievienot Transportu")
    logs.geometry("300x300")

    tk.Label(logs, text="id transporta:").pack()
    id_transports_entry = tk.Entry(logs)
    id_transports_entry.pack()

    tk.Label(logs, text="Auto registracijas num:").pack()
    auto_reg_num_entry = tk.Entry(logs)
    auto_reg_num_entry.pack()

    tk.Label(logs, text="modelis:").pack()
    modelis_entry = tk.Entry(logs)
    modelis_entry.pack()

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_Transports)
    saglabat_btn.pack(pady=10)


def find_transport():
    def atrast_transportu():
        auto_reg_num = auto_reg_num_entry.get()
        if auto_reg_num:
            cursor.execute("SELECT * FROM Transports WHERE auto_reg_num LIKE ?", (f"%{auto_reg_num}%",))
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}\n"
                    messagebox.showinfo("Rezultāti", f"ID:{r[0]}, Auto registracijas numurs:{r[1]}, modelis:{r[2]}\n")
            else:
                messagebox.showinfo("Rezultāti", "Netika atrasts neviens transports.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet trenera vārdu!")

    logs = tk.Toplevel()
    logs.title("Meklēt transportu")
    logs.geometry("300x200")

    tk.Label(logs, text="Trenera vārds:").pack()
    auto_reg_num_entry = tk.Entry(logs)
    auto_reg_num_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atrast_transportu)
    meklēt_btn.pack(pady=10)


def delete_transport():
    def delete_transport_no_db():
        id_transports = id_transports_entry.get()
        if id_transports.isdigit():
            cursor.execute("DELETE FROM Transports WHERE id_transports = ?", (id_transports,))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", f"Transportss ar ID {id_transports} tika izdzēsts!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet derīgu ID!")

    logs = tk.Toplevel()
    logs.title("Dzēst Transports")
    logs.geometry("300x150")

    tk.Label(logs, text="Transporta ID:").pack()
    id_transports_entry = tk.Entry(logs)
    id_transports_entry.pack()

    dzēst_btn = tk.Button(logs, text="Dzēst", command=delete_transport_no_db)
    dzēst_btn.pack(pady=10)


def transporta_logs():
    transporta_logs = tk.Toplevel()
    transporta_logs.title("Transports")
    transporta_logs.geometry("300x250")

    pievienot_btn = tk.Button(transporta_logs, text="Pievienot transportu", command=pievienot_transportu, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(transporta_logs, text="Meklēt transportu", command=find_transport, width=25, height=2, bg="lightgreen")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(transporta_logs, text="Dzēst transportu", command=delete_transport, width=25, height=2, bg="lightyellow")
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(transporta_logs, text="Iziet", command=transporta_logs.destroy, width=25, height=2, bg="red", fg="white")
    iziet_btn.pack(pady=10)

def meklēt_pakalpojumu():
    def atrast_pakalpojumu():
        id_klienta = id_klienta_entry.get()
        if id_klienta:
            cursor.execute("SELECT vards, uzvards, auto_reg_num FROM Klients INNER JOIN Pakalpojums ON Klients.id_klienta=Pakalpojums.id_klienta INNER JOIN Transports ON Pakalpojums.id_transports=Transports.id_transports WHERE Klients.id_klienta LIKE ?", (f"%{id_klienta}%",))
            rezultati = cursor.fetchall()
            
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}\n"
                    messagebox.showinfo("Meklēšanas rezultāti", f"{r[0]} {r[1]}, transporta numurs: {r[2]}\n")
            else:
                messagebox.showinfo("Rezultāti", "Netika atrasts neviens klients.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet Klienta vārdu!")

    logs = tk.Toplevel()
    logs.title("Meklēt klienta apmeklējumu")
    logs.geometry("300x200")

    tk.Label(logs, text="Klienta id:").pack()
    id_klienta_entry = tk.Entry(logs)
    id_klienta_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atrast_pakalpojumu)
    meklēt_btn.pack(pady=10)

def izveidot_galveno_logu():
    def Klients_poga():
        klienta_logs()
        messagebox.showinfo("Klienti", "Atvērta klientu pārvaldība.")

    def Transports_poga():
        transporta_logs()
        messagebox.showinfo("Transports", "Atvērta transporta pārvaldība.")

    def pakalpojums_poga():
        meklēt_pakalpojumu()
        messagebox.showinfo("Pakalpojumi", "Atvērta pakalpojumu pārvaldība.")

    logs = tk.Tk()
    logs.title("Apdošināšanas kompanijas pārvaldība")
    logs.geometry("300x280")
    image = PhotoImage(file="balta.png")
    img = Label(image=image)
    img.pack()

    Klients_btn = tk.Button(logs, text="Klients", command=Klients_poga, width=20, height=2, bg="aquamarine2")
    Klients_btn.pack(pady=10)

    Transports_btn = tk.Button(logs, text="Transports", command=Transports_poga, width=20, height=2, bg="gray80")
    Transports_btn.pack(pady=10)

    pakalpojums_btn = tk.Button(logs, text="Pakalpojumi", command=pakalpojums_poga, width=20, height=2, bg="LightGoldenrod2")
    pakalpojums_btn.pack(pady=10)


    logs.mainloop()

if __name__ == "__main__":
    izveidot_galveno_logu()