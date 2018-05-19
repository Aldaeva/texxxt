from tkinter import *
import random
 
print('ДОБРО ПОЖАЛОВАТЬ В ИГРУ!'+'\n') 
width = 800   
height = 300
speedUP = 1 
speedMAX = 40  
speedSTART = 20
speedA = speedSTART
speedB = speedSTART
score1 = 0    
score2 = 0
rightd = 780   
scoreAchange = 20 
scoreBchange = 0   
ps = 20 
ls = 0 
rs = 0
racketW = 20  
a = int(input('Выберите уровнеь сложности'+ '\n'+ '1 - Лёгкий'+'\n'+'2 - Средний'+'\n'+'3 - Сложный'+'\n')) 
if a == 1:
    racketH = 150
    ballR = 50
if a == 2:
    racketH = 100
    ballR = 30
if a == 3:
    racketH = 50
    ballR = 20


root = Tk()
root.title('PIN-PONG')
c = Canvas(root, width=width, height=height, background='#E6E6FA') 
c.pack()
c.create_line(racketW, 0, racketW, height, fill='white') 
c.create_line(width-racketW, 0, width-racketW, height, fill='white') 
c.create_line(width/2, 0, width/2, height, fill='white') 
ball = c.create_oval(width/2-ballR/2, height/2-ballR/2, width/2+ballR/2, height/2+ballR/2, fill='#7B68EE')
left = c.create_line(racketW/2, 0, racketW/2, racketH, width=racketW, fill='#4B0082') 
right = c.create_line(width-racketW/2, 0, width-racketW/2,racketH, width=racketW, fill='#4B0082')
text1 = c.create_text(width-width/6, racketH/4, text=score1, font='Arial 30', fill='#191970')
text2 = c.create_text(width/6, racketH/4,text=score2,font='Arial 30',fill='#191970')



def ballstart():
    global speedA
    c.coords(ball, width/2-ballR/2, height/2-ballR/2, width/2+ballR/2, height/2+ballR/2)
    speedA = -(speedA * -speedSTART) / abs(speedA)  

def hit(action):  
    global speedA, speedB
    if action == 'strike':     
        speedB = random.randrange(-10, 10)
        if abs(speedA) < speedMAX :
            speedA *= -speedUP
        else:
            speedA = -speedA
    else:
        speedB = -speedB

def scoreplayers(player):
    global score1, score2
    if player == 'right':
        score1 += 1
        c.itemconfig(text1, text=score1)
    else:
        score2 += 1
        c.itemconfig(text2, text=score2)

def start_ball():
    bl, bt, br, bb = c.coords(ball)  
    bc = (bt + bb) / 2
    if br + speedA < rightd and bl + speedA > racketW:  
        c.move(ball, speedA, speedB)
    elif br == rightd or bl == racketW:  
        if br > width / 2:  
            if c.coords(right)[1] < bc < c.coords(right)[3]:
                hit('strike')
            else:
                scoreplayers('left')
                ballstart()
        else:
            if c.coords(left)[1] < bc < c.coords(left)[3]:
                hit('strike')
            else:
                scoreplayers('right')
                ballstart()
    else:
        if br > width / 2:
            c.move(ball, rightd-br, speedB)
        else:
            c.move(ball, -bl+racketW, speedB)
    if bt + speedB < 0 or bb + speedB > height: 
        hit('ricochet')

def _get():  
    dict_ = {left: ls, right: rs}
    for i in dict_:
        c.move(i, 0, dict_[i]) 
        if c.coords(i)[1] < 0:           
            c.move(i, 0, -c.coords(i)[1])
        elif c.coords(i)[3] > height:
            c.move(i, 0, height - c.coords(i)[3])
def start():
    start_ball()
    _get()
    root.after(30, start)     
c.focus_set() 

def clisk(w):  
    global ls, rs
    if w.keysym == 'w':
        ls = -ps
    elif w.keysym == 's':
        ls = ps
    elif w.keysym == 'Up':
        rs = -ps
    elif w.keysym == 'Down':
        rs = ps

def unclisk(w):      
    global ls, rs
    if w.keysym in 'ws':
        ls = 0
    elif w.keysym in ('Up', 'Down'):
        rs = 0
c.bind('<KeyPress>', clisk)        
c.bind('<KeyRelease>', unclisk) 
start()
root.mainloop()
