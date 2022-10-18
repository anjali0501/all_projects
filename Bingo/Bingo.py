from tkinter import *

import random
global coml,cl,butlist,nownumber
coml=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
random.shuffle(coml)
cl=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
from tkinter import font

win=Tk()
win.title("Bingo")
#win.iconbitmap('imageb.ico')
win.maxsize(width=600,height=500)
win.minsize(width=600,height=500)
lbl1=Label(win,text="B",bg="red",fg="white",width=2,font=('Helvetica',50,'bold'))
#lbl1.grid(row=4,column=3)
lbl1.place(x=30,y=10)
lbl2=Label(win,text="I",bg="blue",fg="white",width=2,font=('Helvetica',50,'bold'))
lbl2.place(x=130,y=10)
lbl3=Label(win,text="N",bg="green",fg="white",width=2,font=('Helvetica',50,'bold'))
lbl3.place(x=230,y=10)
lbl4=Label(win,text="G",bg="yellow",fg="white",width=2,font=('Helvetica',50,'bold'))
lbl4.place(x=340,y=10)
lbl5=Label(win,text="O",bg="purple",fg="white",width=2,font=('Helvetica',50,'bold'))
lbl5.place(x=440,y=10)

#entry
#ent=Entry(win)
#ent.place(x=30,y=200)

#button
#btn=Button(win,text="submit",bg='green')
#btn.place(x=10,y=150)
myfont=font.Font(family="arial",size=20)
but1_1=Button(win,text='',height=2,width=4,command=lambda:game(win,but1_1))
but1_1["font"]=myfont
but1_2=Button(win,text='',height=2,width=4,command=lambda:game(win,but1_2))
but1_2["font"]=myfont
but1_3=Button(win,text='',height=2,width=4,command=lambda:game(win,but1_3))
but1_3["font"]=myfont
but1_4=Button(win,text='',height=2,width=4,command=lambda:game(win,but1_4))
but1_4["font"]=myfont
but1_5=Button(win,text='',height=2,width=4,command=lambda:game(win,but1_5))
but1_5["font"]=myfont
but2_1=Button(win,text='',height=2,width=4,command=lambda:game(win,but2_1))
but2_1["font"]=myfont
but2_2=Button(win,text='',height=2,width=4,command=lambda:game(win,but2_2))
but2_2["font"]=myfont
but2_3=Button(win,text='',height=2,width=4,command=lambda:game(win,but2_3))
but2_3["font"]=myfont
but2_4=Button(win,text='',height=2,width=4,command=lambda:game(win,but2_4))
but2_4["font"]=myfont
but2_5=Button(win,text='',height=2,width=4,command=lambda:game(win,but2_5))
but2_5["font"]=myfont
but3_1=Button(win,text='',height=2,width=4,command=lambda:game(win,but3_1))
but3_1["font"]=myfont
but3_2=Button(win,text='',height=2,width=4,command=lambda:game(win,but3_2))
but3_2["font"]=myfont
but3_3=Button(win,text='',height=2,width=4,command=lambda:game(win,but3_3))
but3_3["font"]=myfont
but3_4=Button(win,text='',height=2,width=4,command=lambda:game(win,but3_4))
but3_4["font"]=myfont
but3_5=Button(win,text='',height=2,width=4,command=lambda:game(win,but3_5))
but3_5["font"]=myfont
but4_1=Button(win,text='',height=2,width=4,command=lambda:game(win,but4_1))
but4_1["font"]=myfont
but4_2=Button(win,text='',height=2,width=4,command=lambda:game(win,but4_2))
but4_2["font"]=myfont
but4_3=Button(win,text='',height=2,width=4,command=lambda:game(win,but4_3))
but4_3["font"]=myfont
but4_4=Button(win,text='',height=2,width=4,command=lambda:game(win,but4_4))
but4_4["font"]=myfont
but4_5=Button(win,text='',height=2,width=4,command=lambda:game(win,but4_5))
but4_5["font"]=myfont
but5_1=Button(win,text='',height=2,width=4,command=lambda:game(win,but5_1))
but5_1["font"]=myfont
but5_2=Button(win,text='',height=2,width=4,command=lambda:game(win,but5_2))
but5_2["font"]=myfont
but5_3=Button(win,text='',height=2,width=4,command=lambda:game(win,but5_3))
but5_3["font"]=myfont
but5_4=Button(win,text='',height=2,width=4,command=lambda:game(win,but5_4))
but5_4["font"]=myfont
but5_5=Button(win,text='',height=2,width=4,command=lambda:game(win,but5_5))
but5_5["font"]=myfont
butlist=[but1_1,but1_2,but1_3,but1_4,but1_5,
        but2_1,but2_2,but2_3,but2_4,but2_5,
        but3_1,but3_2,but3_3,but3_4,but3_5,
        but4_1,but4_2,but4_3,but4_4,but4_5,
        but5_1,but5_2,but5_3,but5_4,but5_5]
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
random.shuffle(l)
for i in range(25):
    butlist[i]['text']=l[i]
but1_1.grid(row=1,column=1)
but1_1.place(x=30,y=100)
but1_2.grid(row=1,column=2)
but1_2.place(x=130,y=100)
but1_3.grid(row=1,column=3)
but1_3.place(x=230,y=100)
but1_4.grid(row=1,column=4)
but1_4.place(x=340,y=100)
but1_5.grid(row=1,column=5)
but1_5.place(x=440,y=100)
but2_1.grid(row=2,column=1)
but2_1.place(x=30,y=170)
but2_2.grid(row=2,column=2)
but2_2.place(x=130,y=170)
but2_3.grid(row=2,column=3)
but2_3.place(x=230,y=170)
but2_4.grid(row=2,column=4)
but2_4.place(x=340,y=170)
but2_5.grid(row=2,column=5)
but2_5.place(x=440,y=170)
but3_1.grid(row=3,column=1)
but3_1.place(x=30,y=250)
but3_2.grid(row=3,column=2)
but3_2.place(x=130,y=250)
but3_3.grid(row=3,column=3)
but3_3.place(x=230,y=250)
but3_4.grid(row=3,column=4)
but3_4.place(x=340,y=250)
but3_5.grid(row=3,column=5)
but3_5.place(x=440,y=250)
but4_1.grid(row=4,column=1)
but4_1.place(x=30,y=330)
but4_2.grid(row=4,column=2)
but4_2.place(x=130,y=330)
but4_3.grid(row=4,column=3)
but4_3.place(x=230,y=330)
but4_4.grid(row=4,column=4)
but4_4.place(x=340,y=330)
but4_5.grid(row=4,column=5)
but4_5.place(x=440,y=330)
but5_1.grid(row=5,column=1)
but5_1.place(x=30,y=410)
but5_2.grid(row=5,column=2)
but5_2.place(x=130,y=410)
but5_3.grid(row=5,column=3)
but5_3.place(x=230,y=410)
but5_4.grid(row=5,column=4)
but5_4.place(x=340,y=410)
but5_5.grid(row=5,column=5)
but5_5.place(x=440,y=410)
def game(t,b):
    n=b['text']
    if b['text']!='*':
        b['text']='*'
        compplay(t,n)
def compplay(t,n):
    global coml,cl,butlist,l
    l[l.index(int(n))]='*'
    coml[coml.index(int(n))]='*'
    cl.pop(cl.index(int(n)))
    if statement(t)== False:
        a=random.choice(cl)
        cl.pop(cl.index(a))
        coml[coml.index(a)]='*'
        butlist[l.index(a)]['text']='*'
        l[l.index(a)]='*'
        statement(t)
def plcheck():
    global l
    s=0
    if l[0]==l[1]==l[2]==l[3]==l[4]:
        s+=1
    if l[5]==l[6]==l[7]==l[8]==l[9]:
        s+=1
    if l[10]==l[11]==l[12]==l[13]==l[14]:
        s+=1
    if l[15]==l[16]==l[17]==l[18]==l[19]:
        s+=1
    if l[20]==l[21]==l[22]==l[23]==l[24]:
        s+=1
    if l[0]==l[5]==l[10]==l[15]==l[20]:
        s+=1
    if l[1]==l[6]==l[11]==l[16]==l[21]:
        s+=1
    if l[2]==l[7]==l[12]==l[17]==l[22]:
        s+=1
    if l[3]==l[8]==l[13]==l[18]==l[23]:
        s+=1
    if l[4]==l[9]==l[14]==l[19]==l[24]:
        s+=1
    if l[0]==l[6]==l[12]==l[18]==l[24]:
        s+=1
    if l[4]==l[8]==l[12]==l[16]==l[20]:
        s+=1
    if s>=5:
        return True
    else:
        return False
def compcheck():
    global coml
    s=0
    if coml[0]==coml[1]==coml[2]==coml[3]==coml[4]:
        s+=1
    if coml[5]==coml[6]==coml[7]==coml[8]==coml[9]:
        s+=1
    if coml[10]==coml[11]==coml[12]==coml[13]==coml[14]:
        s+=1
    if coml[15]==coml[16]==coml[17]==coml[18]==coml[19]:
        s+=1
    if coml[20]==coml[21]==coml[22]==coml[23]==coml[24]:
        s+=1
    if coml[0]==coml[5]==coml[10]==coml[15]==coml[20]:
        s+=1
    if coml[1]==coml[6]==coml[11]==coml[16]==coml[21]:
        s+=1
    if coml[2]==coml[7]==coml[12]==coml[17]==coml[22]:
        s+=1
    if coml[3]==coml[8]==coml[13]==coml[18]==coml[23]:
        s+=1
    if coml[4]==coml[9]==coml[14]==coml[19]==coml[24]:
        s+=1
    if coml[0]==coml[6]==coml[12]==coml[18]==coml[24]:
        s+=1
    if coml[4]==coml[8]==coml[12]==coml[16]==coml[20]:
        s+=1
    if s>=5:
        return True
    else:
        return False
def statement(t):
    if plcheck()==True and compcheck()==True:
        t.destroy()
        tk=Tk()
        Label(tk,text='draw').pack()
        Label(tk,text=compboard()).pack()
        Label(tk,text=plboard()).pack()
    elif plcheck()==True and compcheck()==False:
        t.destroy()
        tk=Tk()
        Label(tk,text='win').pack()
        Label(tk,text=compboard()).pack()
        Label(tk,text=plboard()).pack()
    elif plcheck()==False and compcheck()==True:
        t.destroy()
        tk=Tk()
        Label(tk,text='lose').pack()
        Label(tk,text=compboard()).pack()
        Label(tk,text=plboard()).pack()
    else:
        return False
def compboard():
    global coml
    x=0
    s='''com board
'''
    for i in range(5):
        s+='| '
        for j in range(5):
            s+=str(coml[x])+' | '
            x+=1
        s+='\n'
    return s
def plboard():
    global l
    x=0
    s='''player board
'''
    for i in range(5):
        s+='| '
        for j in range(5):
            s+=str(l[x])+' | '
            x+=1
        s+='\n'
    return s  
win.mainloop() 