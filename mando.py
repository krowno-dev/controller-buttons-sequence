#
 # This file is part of the controller_buttons_sequence distribution (https://github.com/krowno-dev/controller-buttons-sequence).
 # Copyright (c) 2021 Roberto Rodriguez.
 # 
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, version 3.
 #
 # This program is distributed in the hope that it will be useful, but 
 # WITHOUT ANY WARRANTY; without even the implied warranty of 
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
 # General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License 
 # along with this program. If not, see http://www.gnu.org/licenses/.
 #


from PIL import Image,ImageFilter 

#declaracion de funciones
def botones(lista,listaBotones,modelo):
    for p in listaBotones:
        lista.append(Image.open(direccion(modelo,p)))

    return lista

def direccion(modelo,boton):
    direccion = ('Botones/'+modelo+'/'+modelo+'_'+boton+'.png')
    return direccion



#declaracion de variables
listaBotones = ["A","B","X","Y","Dpad_Down","Dpad_Left","Dpad_Right","Dpad_Up","LB","RB","LT","RT","Right_Stick","Left_Stick","Right_Stick_Click","Left_Stick_Click","flecha"]
botonesPulsados = []
mando = 'XBoxOne'
combo = []
numero = 0
numero2 = 0
numero3 = 0
salir = 0
compruebaMando = 0


#lectura del mando
#while (compruebaMando == 0):
#    mandoIn = int(input("introduce un numero;\n1->Xbox One 2->PS4 3->Switch \n"))
#    if (mandoIn >= 1 and mandoIn <= 3): compruebaMando = 1
#    else: print("valor incorrecto, intentelo de nuevo")

combo = botones(combo,listaBotones,mando)

#lectura de los botones
print("Botones disponibles:")
print("[",end=""),
print(*listaBotones,sep='] [',end=']\n')

while (salir!=1):
    numero3 = numero
    botonIn = input("Introduce los botones --> ")
    if(botonIn == "0"):
            salir = 1
    else: 
        for bots in listaBotones:        
            if(botonIn == bots):
                botonesPulsados.append(botonIn)
                numero += 1
    if (numero3 == numero and salir !=1): print("X - boton incorrecto - X")
            

#generacion de la imagen
result = Image.new('RGBA',(numero*100, 100),(255, 0, 0, 0))

for elemento in botonesPulsados:  
    result.paste(combo[listaBotones.index(elemento)],(numero2*100,0))
    numero2 +=1


nombre = input("Introduzca el nombre del archivo final\n")
result.save("Final/"+nombre+".png","PNG")
result.show()