import itertools
import datetime
from datetime import time
import sqlite3
import tkinter as tk
from tkinter import messagebox

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
            cursor.execute("DELETE FROM Sportisti WHERE id_klienta = ?", (id_klienta,))
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
    trenera_logs = tk.Toplevel()
    trenera_logs.title("Klientu saraksts")
    trenera_logs.geometry("300x250")

    pievienot_btn = tk.Button(trenera_logs, text="Pievienot klientu", command=pievienot_klientu, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(trenera_logs, text="Meklēt klientu pēc ID", command=meklet_klientu, width=25, height=2, bg="lightgreen")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(trenera_logs, text="Dzēst KLIENTU", command=dzest_klientu, width=25, height=2, bg="lightyellow")
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(trenera_logs, text="Iziet", command=trenera_logs.destroy, width=25, height=2, bg="red", fg="white")
    iziet_btn.pack(pady=10)        

def izveidot_galveno_logu():
    def Klients_poga():
        klienta_logs()
        messagebox.showinfo("Klienti", "Atvērta klientu pārvaldība.")

    def treneri_poga():
        #trenera_logs()
        messagebox.showinfo("Treneri", "Atvērta treneru pārvaldība.")

    def apmeklejumi_poga():
        messagebox.showinfo("Apmeklējumi", "Atvērta apmeklējumu pārvaldība.")

    logs = tk.Tk()
    logs.title("Trenažieru zāles pārvaldība")
    logs.geometry("300x200")

    Klients_btn = tk.Button(logs, text="Klients", command=Klients_poga, width=20, height=2, bg="lightblue")
    Klients_btn.pack(pady=10)

    treneri_btn = tk.Button(logs, text="Treneri", command=treneri_poga, width=20, height=2, bg="lightgreen")
    treneri_btn.pack(pady=10)

    apmeklejumi_btn = tk.Button(logs, text="Apmeklējumi", command=apmeklejumi_poga, width=20, height=2, bg="lightyellow")
    apmeklejumi_btn.pack(pady=10)

    logs.mainloop()

if __name__ == "__main__":
    izveidot_galveno_logu()