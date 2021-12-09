import time
from tkinter import *
import psutil
#import matplotlib.pyplot as plt
import numpy as np

def palindrom():
    Button1.destroy()
    rootZahl = 1
    Fehler = []
    e = time.time()
    liste = []
    auslastung = []
    zeitliste = []
    for x in range(200):
        Zahl = rootZahl
        versuche = 0
        label.config(text='Zahl wird berechnet: '+str(rootZahl))
        tk.update()
        temp = []
        while True:
            zahl_rev = int(str(Zahl)[::-1])
            versuche += 1
            label2.config(text='Versuche: '+str(versuche))
            tk.update()

    #        print(rootZahl, zahl_rev, Zahl, versuche)
            if int(zahl_rev) == int(Zahl):
                print('Zahl: ' + str(rootZahl) + '. Versuche: ' + str(versuche))
                break
            if versuche > 10000:
                print('Timeout. len of trys to high.')
                Fehler.append(rootZahl)
                stri = ''
                for x in Fehler:
                    stri = stri + str(x) + ', ' 
                label4.config(text=str('Timeout bei: ' + str(stri)))
                break
            Zahl = Zahl + int(str(Zahl)[::-1])
            label3.config(text='Hochgerechnete Zahl: '+str(Zahl)[:70])
            label5.config(text='Größe der berechneten Zahl: '+str(len(str(Zahl))))
            print('Auslastung: '+str(psutil.cpu_percent()))
            auslastung.append(psutil.cpu_percent())
            zeitliste.append(str(float(time.time())-float(e)))
            tk.update()

        temp.append(rootZahl)
        temp.append(versuche)
        liste.append(temp)
        
        rootZahl += 1
    print('-------Auswertung-------')
    print('Zahlen: Versuche zu hoch', Fehler)
#    print(str(float(e-time.time)))
    root = Tk()
    listbox = Listbox(root)
    listbox.pack(side = LEFT, fill = BOTH)
    scrollbar = Scrollbar(root)
    scrollbar.pack(side = RIGHT, fill = BOTH)
    listbox.insert(END, 'Zahl      Versuche')
    # Insert elements into the listbox
    for values in range(len(liste)):
        temp = str(liste[values][0]) + ': ' + str(liste[values][1])
        listbox.insert(END, temp)
    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)
#    xpoints = np.array(zeitliste)
#    ypoints = np.array(auslastung)
#    plt.plot(xpoints, ypoints)
#    plt.show()



tk = Tk()
tk.geometry('600x600+200+200')
label = Label(tk, text=str('Zahl wird berechnet: None'), font=('Arial', 20))
label.place(x=10, y=50)
label2 = Label(tk, text=str('Versuche: None'), font=('Arial', 20))
label2.place(x=10, y=150)
label3 = Label(tk, text=str('Hochgerechnete Zahl: None'), font=('Arial', 20))
label3.place(x=10, y=250)
label4 = Label(tk, text=str('Timeout bei: None'))
label4.place(x=10, y=350)
label5 = Label(tk, text=str('Größe der berechneten Zahl: None'), font=('Arial', 20))
label5.place(x=10, y=450)
label6 = Label(tk, text=str('Auslastung: None'), font=('Arial', 20))
label6.place(x=10, y=550)
Button1 = Button(tk, text='Start', command=palindrom, font=('Arial', 20))
Button1.place(x=10, y=400)
tk.update()
tk.mainloop()
