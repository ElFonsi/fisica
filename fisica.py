import math
from tkinter import E
q1=int(input("Ingrese el valor de la primera carga en micro culomb : "))
q2=int(input("Ingrese el valor de la segundo carga en micro culomb : "))
q3=int(input("Ingrese el valor de la tercero carga en micro culomb : "))
angulo=float(input("Ingrese el angulo: "))
distancia=float(input("Ingrese la distancia entre q2 y q3: "))
distanciaC=distancia/2
angulofaltante=180-(angulo+90)
k=9*10**9
ang=math.radians(angulo)
d13=distanciaC/math.cos(ang)
print("Distancia entre q1 y q3",d13,"m")

F13=(k)*(q1*10**-6)*(q2*10**-6)
F13P2=F13/(d13*d13)
print("Fuerza entre q1 y q3: ",F13P2)


#fuerza entre q1 y q2

d12 = d13
F12=(k)*(q1*10**-6)*(q3*10**-6)
F12P2=F12/(d12*d12)
print("Fuerza entre q1 y q2: ",F12P2)


#Fuerza entre q2 y q3

F23=(k)*(q2*10**-6)*(q3*10**-6)
F23P2=F23/(distancia*distancia)
print("Fuerza entre q2 y q3: ",F23P2)

#Fuerza total en x , y carga 3
F13X=F23P2
FTX3=F13X+F23P2

anguloA=90-angulo
math.radians(anguloA) #sacar fuerza carga 3
FTY3= (F13P2*math.sin(angulo))/math.sin(90)

Ft3=(FTX3*FTX3)+(FTY3*FTY3)
Ft3P2=math.sqrt(Ft3)

print("Fuerza total en la carga 3: ", Ft3P2)


#Fuerza total en x , y carga 2

F12X=F23P2
FTX2=F12X+F23P2

anguloB=90-angulo
math.radians(anguloB) #sacar fuerza carga 3
FTY2= (F12P2*math.sin(angulo))/math.sin(90)

Ft2=(FTX2*FTX2)+(FTY2*FTY2)
Ft2P2=math.sqrt(Ft2)

print("Fuerza total en la carga 2: ", Ft2P2)

#fuerza total carga 1



#Fuerza total suma de todo

fuerzatotal = (F13P2 + F12P2 + F23P2)

print("La fuerza total es: ", fuerzatotal)

