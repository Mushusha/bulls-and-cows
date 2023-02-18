import random
from tkinter import *

def wenter(event, p):
    clickenter(p)

def wstart(event):
    clickstart()

def wok(event):
    clickok()

def clickexit():
    win.destroy()

def clicknew():
    clickok()
    winc.destroy()
    butnew.destroy()
    butexit.destroy()

def clickok():
    butok.destroy()
    lblrules.destroy()
    global entn, lbln, butstart
    number = IntVar(value = 0)
    lbln = Label(win, text = 'amount of numbers')
    entn = Entry(win, textvariable = number)

    butstart = Button(win, text = 'START', font = (20), command = clickstart)
    
    lbln.place(relx = 0.1,rely = 0.19)
    entn.place(relx = 0.5,rely = 0.2, width = 20)
    butstart.place(relx = 0.36, rely = 0.6, width = 100, height = 60)
    win.bind('<Return>', wstart)
    entn.focus_set()

def cursr(event, i):
    arrent[i + 1].focus_set()

def cursl(event, i):
    arrent[i - 1].focus_set()

def changecurr(i):
    i += 1
    if i != n - 1:
        arrent[i].bind('<Right>', lambda e: cursr(e, i))
        changecurr(i)
    if i != 0:
        arrent[i].bind('<Left>', lambda e: cursl(e, i))

def clickstart():
    global n
    n = int(entn.get())
    if n < 3 or n > 7:
        entn.configure(bg = 'red')
    else:
#    object = [lbln, entn, lblYN, butY, butstart]
        object = [lbln, entn, butstart]
        for i in object:
            i.destroy()
        global lblnum, lblb, lblk
        lblnum = Label(win, text = 'your numbers')
        lblb = Label(win, text = 'bulls')
        lblk = Label(win, text = 'cows')
        lblnum.place(x = 0, y = 0)
        lblb.place(x = 30*n + 40, y = 0)
        lblk.place(x = 30*n + 80, y = 0)
        global a
        a = []*n
        a = [random.randint(0, 9) for i in range(n)]
        for i in range(n):
            a[i] = random.randint(0, 9)
            for j in range(i):
                if a[i] == a[j]:
                    while a[i] == a[j]:
                        a[i] = random.randint(0, 9)
        if a[0] == a[n - 1]:
            while a[0] == a[n - 1]:
                a[n - 1] = random.randint(0, 9)
            
        global arrent
        arrent = []
        global desarr
        desarr = []
        
        for i in range(n):
            ent = Entry(win)
            arrent.append(ent)
            desarr.append(ent)
            ent.place(x = 30*i, y = 40, width = 20)
        
        changecurr(-1)
        arrent[0].focus_set()
        #but.place(x = 30*n + 150, y = 40, height = 20)
    #Доделать
        #scr = Scrollbar(orient="vertical", command = win.yview)
        #scr.pack(side = RIGHT, fill = Y)

        win.bind('<Return>', lambda e: wenter(e, 1))

        
def clickenter(p):
    t = []
    flag = 0
    for i in range(n):
        t.append(int(arrent[i].get()))
        for j in range(i):
            if t[j] == t[i]:
                arrent[i].configure(bg = 'red')
                arrent[j].configure(bg = 'red')
                flag = 1
        if t[i] > 9 or t[i] < 0:
            arrent[i].configure(bg = 'red')
            flag = 1
            
    if flag == 0:
        b = 0
        k = 0
        for i in range (n):
            for j in range (n):
                if t[i] == a[j] and i == j:
                    b += 1
                if t[i] == a[j] and i != j:
                    k += 1
        lblbulls = Label(win, text = b)
        lblbulls.place(x = 30*n + 40, y = 40*p)
        lblcows = Label(win, text = k)
        lblcows.place(x = 30*n + 80, y = 40*p)
        desarr.append(lblbulls)
        desarr.append(lblcows)

        
        if b != n:
            p += 1
            for i in range(n):
                arrent[i].config(state = 'readonly')
            arrent.clear()
            for i in range(n):
                ent = Entry(win)
                arrent.append(ent)
                desarr.append(ent)
                ent.place(x = 30*i, y = 40*(p), width = 20)
            #but1 = Button(win, text = 'Enter', command = lambda: clickenter(p))
            #but1.place(x = 30*n + 150, y = 40*(p), height = 20)
            changecurr(-1)
            arrent[0].focus_set()
            win.bind('<Return>', lambda e: wenter(e, p))
        else:
            desarr.append(lblnum)
            desarr.append(lblb)
            desarr.append(lblk)
            for i in desarr:
                i.destroy()
            global winc, butnew, butexit
            wincat = PhotoImage(file = 'catless.png')
            winc = Label(win, image = wincat)
            winc.image = wincat
            winc.pack()
            butnew = Button(win, text = 'NEW', font = (20), command = clicknew)
            butexit = Button(win, text = 'EXIT', font = (20), command = clickexit)
            butnew.pack()
            butexit.pack()
            #lblwin = Label(win, text = 'WIN', font = (20)).place(x = 30*n + 40, y = 40*(p + 2))
            

win = Tk()
win.title('bulls and cows')
win.geometry('600x400')
lblrules = Label(win, text = 'ПРАВИЛА \n Загадывается последовательность из того количества чисел, \n \
                 которые вы введете (в данной версии числа не могут повторяться). \n \
                 Ваша задача отгадать эту последовательность (она состоит из цифр от 0 до 9). \n \
                 Вы вводите свой вариант - строго по одной цифре в клеточку и нажимаете Enter. \n \
                 Количество быков - это количество цифр, стоящих на правильной позиции, \n \
                 а количество коров - цифры, которые просто присутствуют в этой последовательности.')
lblrules.pack(expand = 1)
butok = Button(win, text = 'OK', command = clickok)
butok.pack(expand = 1)
win.bind('<Return>', wok)

#lblYN = Label(win, text = 'do want you reapiting numbers?')
#butY = Button(win, text = 'yes', command = (lambda YN: YN + 1)(YN))
#butY.place(relx = 0.6, rely = 0.4)
#lblYN.place(relx = 0.1,rely = 0.4)

#...
def clicks():
    print(a)
    
#buts = Button(win, text = 'S', command = clicks)
#buts.place(relx = 0.36, rely = 0.8)

#but = Button(win, text = 'Enter', command = lambda: clickenter(1))
#but.place_forget()

win.mainloop()
