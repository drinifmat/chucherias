# Sierpinskis modulo n
# Python 3.3
 
from itertools import *
import turtle
import time
 
size=256
mod=6
dx = 4
 
turtle.setup(   width=1204,height=700)
def Pascal(size,mod):
    L=[ [0]*size for k in range(size)]
    for k in range(size):
        L[0][k]= 1
        L[k][0]=1
 
    for i in range(1,size):
        for j in range(1,size):
            L[i][j] = (L[i-1][j] + L[i][j-1]) % mod
 
    #for l in L:
    #    print(l)
    return L
 
def clr(c,mod):
    c = mod-c-1
    t = (c)/(mod-1)
    return (t,t,t)
 
 
   
def Sierpinsmod(size,mod,alto=1024,ancho=700,dx=4):
    r=1.0*dx  
    pp=dx  # Grueso de los puntos
    turtle.colormode(1)
    turtle.ht()
   
    turtle.speed("fastest")
    turtle.tracer(False)
    turtle.penup()
    turtle.home()
    ox = -(turtle.window_width()/2)+2*dx
    oy = (turtle.window_height()/2)-2*dx
 
    P=Pascal(size,mod)

    turtle.setpos(ox,oy)
   
    turtle.dot(pp,clr(P[0][0],mod))
    turtle.seth(90)
   
    for d in range(1,2*size-1):
        print("iniciando diagonal ",d),
        if d< size:
            initx=0  # Posiciones iniciales
            inity=d
        else:
            initx = d-size+1
            inity = size-1
       
        turtle.setpos(ox+initx*dx-dx,oy-inity*dx-dx)
 
        for k in range(initx,inity+1):  
            # Recorremos la diagonal de suma d
            # Los puntos corresponden a (k, d-k)
            turtle.right(90)
            turtle.forward(dx)
            turtle.left(90)
            turtle.forward(dx)
            t=P[k][d-k]
            if t > 0:
                turtle.dot(pp, clr(t,mod))
        if d % 20 ==0: turtle.update()        
   
start=time.clock()
Sierpinsmod(size,mod,dx)
fin = time.clock()
turtle.update()
print("::" ,fin-start,"::")
