import random
from tkinter import *


def clickbutn():
    global n
    n = int(entn.get())
    if n < 3 or n > 7:
        entn.configure(bg = 'red')
    if n >= 3 and n <= 7:
        entn.configure(bg = 'green')
        
def clickstart():
#    object = [lbln, entn, butn, lblYN, butY, butstart]
    object = [lbln, entn, butn, butstart]
    for i in object:
        i.destroy()
    lblnum.place(x = 0, y = 0)
    lblb.place(x = 30*n + 40, y = 0)
    lblk.place(x = 30*n + 80, y = 0)
    global a
    a = []*n
    a = [random.randint(0, 9) for i in range(n)]
    for i in range(n):
        a[i] = random.randint(0, 9)
        if YN == 0:
            for j in range(i):
                if a[i] == a[j]:
                    while a[i] == a[j]:
                        a[i] = random.randint(0, 9)
    if a[0] == a[n - 1]:
        while a[0] == a[n - 1]:
            a[n - 1] = random.randint(0, 9)
            
    global arrent
    arrent = []        
    for i in range(n):
        ent = Entry(win)
        arrent.append(ent)
        ent.place(x = 30*i, y = 40, width = 20)
    but.place(x = 30*n + 150, y = 40, height = 20)

        
def clickenter(p):
    t = []
    for i in range(n):
        t.append(int(arrent[i].get()))
    b = 0
    k = 0
    for i in range (n):
        for j in range (n):
            if t[i] == a[j] and i == j:
                b += 1
            if t[i] == a[j] and i != j:
                k += 1
    lblbulls = Label(win, text = b).place(x = 30*n + 40, y = 40*p)
    lblcows = Label(win, text = k).place(x = 30*n + 80, y = 40*p)   
    if b != n:
        p += 1
        for i in range(n):
            arrent[i].config(state = 'readonly')
        arrent.clear()
        for i in range(n):
            ent = Entry(win)
            arrent.append(ent)
            ent.place(x = 30*i, y = 40*(p), width = 20)
        but1 = Button(win, text = 'Enter', command = lambda: clickenter(p))
        but1.place(x = 30*n + 150, y = 40*(p), height = 20)
    else:
        lblwin = Label(win, text = 'WIN', font = (20)).place(x = 30*n + 40, y = 40*(p + 2))
    

win = Tk()
win.title('bulls and cows')
win.geometry('400x300')

#ПРАВИЛА
YN = 0
number = IntVar(value = 0)
lbln = Label(win, text = 'amount of numbers')
entn = Entry(win, textvariable = number)
lbln.place(relx = 0.1,rely = 0.19)
entn.place(relx = 0.5,rely = 0.2, width = 20)
butn = Button(win, text = 'enter', command = clickbutn)
butn.place(relx = 0.6, rely = 0.19, width = 60)

#lblYN = Label(win, text = 'do want you reapiting numbers?')
#butY = Button(win, text = 'yes', command = (lambda YN: YN + 1)(YN))
#butY.place(relx = 0.6, rely = 0.4)
#lblYN.place(relx = 0.1,rely = 0.4)

butstart = Button(win, text = 'START', font = (20), command = clickstart)
butstart.place(relx = 0.36, rely = 0.6, width = 100, height = 60)

#...
def clicks():
    print(a)
    
#buts = Button(win, text = 'S', command = clicks)
#buts.place(relx = 0.36, rely = 0.8)

    
lblnum = Label(win, text = 'your numbers')
lblb = Label(win, text = 'bulls')
lblk = Label(win, text = 'cows')
lblnum.place_forget()
lblb.place_forget()
lblk.place_forget()

but = Button(win, text = 'Enter', command = lambda: clickenter(1))
but.place_forget()

win.mainloop()

    
print('WIN')


