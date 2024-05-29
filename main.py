import customtkinter as tk
from turtle import *
from random import *
import numpy as np

window = tk.CTk(className="Test")
window.configure(bg="#4c5844")
window.geometry("300x600")
window.resizable(width=False, height=False)
space = tk.CTkLabel(window,text="   Number of Nodes   ")
space4 = tk.CTkLabel(window,text="",)
space5 = tk.CTkLabel(window,text="   Type of Graphic   ")
space6 = tk.CTkEntry(window)
space7 = tk.CTkLabel(window,text="   Starting IP [Optional]   ")
space8= tk.CTkEntry(window)
space9 = tk.CTkLabel(window,text="   Ending IP [Optional]   ")
space10 = tk.CTkEntry(window)
space11 = tk.CTkLabel(window,text = "  Distance to end node   ")
space12 = tk.CTkEntry(window)
nodenumber = tk.CTkOptionMenu(window,width=25,values=['1','2','3','4','5','6','7','8','9','10'])
logLabel = tk.CTkLabel(window,text = "  Output   ")
logBox = tk.CTkTextbox(window)
confirm = tk.CTkButton(window,text="Confirm")

def generate_IP():
    first,second,third,fourth = str(randint(10,255)),str(randint(0,255)),str(randint(0,255)),str(randint(0,255))
    final_ip = '' + first + '.' + second + '.' + third + '.' + fourth
    return final_ip
def create_Node(t,x,y,ip):
    t.color('#6FA8DC')
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(x,y -25)
    t.write(ip,align = "Center", font =("Comic Sans", 6, "normal"))
    t.goto(x,y)
    
ipAnterior = None
t = Turtle()
t.getscreen().bgcolor('#1F1F1F')
t.getscreen().screensize(600,800)

def handleclick(stuff):
    global ipAnterior
    if str.lower(space6.get()) == "datagrama" or str.lower(space6.get()) == "virtual":
        listnodes = nodenumber.get()
        numerodenodes = int(listnodes)
        print(numerodenodes)  
        incrementX,incrementY = 0,0
        ips_ja_utilizados = []
        nodes_in_the_middle = []
        t.clear()
        
        t.goto(0,0)
        finalpos, startpos = choice(list(set(range(-int(space12.get()) or -400, int(space12.get()) or 400)) - set(np.linspace(-int(space12.get()) or -400, int(space12.get()) or 400)))),0
        startIP, endIP = (space8.get() or generate_IP()),(space10.get() or generate_IP())
        create_Node(t, startpos,0,startIP)
        create_Node(t, finalpos,0,endIP)
        t.goto(startpos,startpos)
        for i in range(0,numerodenodes):
            ip_a_ser_utilizado = generate_IP()
            oldpos = (t.xcor(),t.ycor())
            t.speed(randint(1,10))
            if str.lower(space6.get()) == "datagrama": 
              incrementX,incrementY = 0,0
              incrementX = incrementX + choice(list(set(range(-200, 200)) - set(np.linspace(-200,200)))) 
              incrementY = incrementY + choice(list(set(range(-200, 200)) - set(np.linspace(-200,200))))
            else: 
              incrementX = incrementX + choice(list(set(range(-80, 80)) - set(np.linspace(-80,80)))) # o codigo antigo era capaz de generar distancias demasiado pequenas, ao ponto de haver 2 nodes que estavam juntos
              incrementY = incrementY + choice(list(set(range(-80, 80)) - set(np.linspace(-80,80)))) # com este codigo, o minimo é -80 ou 80 unidades
            create_Node(t, t.xcor() + incrementX,t.ycor() + incrementY,ip_a_ser_utilizado)
            newpos = (t.xcor(),t.ycor())
            t.color('#eaeded')
            t.penup()
            t.goto(oldpos)
            t.pendown()
            t.goto(newpos)
            t.penup()
           # if ipAnterior == None:
                # logBox.insert(index = "1",text="Starting node:" + startIP)
           # else:
                # logBox.insert(index = "1", text=ipAnterior + "->" + ip_a_ser_utilizado)
            ipAnterior = ip_a_ser_utilizado
            if str.lower(space6.get()) == "datagrama": # cria multiplos caminhos
              t.goto(startpos,startpos)
              nodes_in_the_middle.append(newpos)
            ips_ja_utilizados.append(ip_a_ser_utilizado)
        if str.lower(space6.get()) == "datagrama":  
            for i in range(0,len(nodes_in_the_middle)):
               t.color('#FF0000')
               t.penup()
               t.goto(nodes_in_the_middle[i])
               t.pendown()
               t.goto(finalpos,0)
               t.penup()
               # logBox.insert(index = 0, text=ips_ja_utilizados[i] + "->" + endIP)


space.pack()
nodenumber.pack()
space5.pack()
space6.pack()
space7.pack()
space8.pack()
space9.pack()
space10.pack()
space11.pack()
space12.pack()
logLabel.pack()
logBox.pack()
space4.pack()
confirm.pack()
confirm.bind("<Button-1>", handleclick)
window.mainloop()


