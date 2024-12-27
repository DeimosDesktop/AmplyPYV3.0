########## AMPLIPY v3.0 ###########
#### Visita https://mirpas.com ####
###################################

### importación de librerías
import numpy as np
import matplotlib.pyplot as plt
import os
import time
#La siguiente clase sirve para mostrar colores del texto en la consola de PYTHON
class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
#print("The output is:" + color.BOLD + "Python Programming !" + color.BLUE)
### Menú de navegación
print(color.BOLD)
print("Bienvenido a AmpliPY. Por favor escoge el tipo de circuito a calcular:")
print(color.BLUE)
print("1- Circuito de polarizador de emisor con dos fuentes de tensión.\n2- Circuito con polarizador de tensión.\n3- Circuito polarizador con realimentación de emisor.")
circuito = int(input("Esperando respuesta: "))
#valores para la ganancia general
corrientes = np.array([0.00002, 0.05])
ganancias = np.array([110,450])
### Funciones
def dosFuentes():
    ##########################################################################
    ########### https://mirpas.com/Lenguajes/4/projects/amplipy.php ##########
    ##########################################################################
    os.system('cls') # Limpio la consola.
    ### Condiciones
    ### Pido los valores
    print("Vamos a configurar el circuito de dos fuentes:")
    img = plt.imread("img/1.png") #ruta relativa o absoluta
    plt.imshow(img)
    plt.title('Esta ventana se cerrará en breve')
    plt.show(block=False)
    plt.pause(5)
    plt.close()
    ### Pido valores de tensión y resistencias.
    VBB = float(input("¿Valor de la tensión de base? "))
    VCC = float(input("¿Valor de la tensión de colector? "))
    RE = float(input("¿Cual es el valor de la resistencia de emisor en óhmios? "))
    RC = float(input("¿Cuál es el valor de la resistencia de colector en óhmios? "))
    ### Constantes para el calculo.
    VE = VBB - 0.7
    IE = VE / RE
    IC = IE
    VC = VCC-(IC*RC)
    VCE = VC - VE
    while True:
        if (VE > VCC):
            print("La tensión de emisor no puede ser mayor que la tensión del circuito!")
            print(f"Tensión de emisor: {VE}.\nTensión de colector: {VC}.")
            return
        elif (RC > RE):
            print("El valor de la resistencia de colector no puede ser tan grande!")
            print(f"Resistencia de emisor: {RE}.\nResistencia de colector: {RC}.\nAyuda: La RE debe ser mayor que la RC.")
            return
        elif (VCE <= 0):
            print("El valor de la tensión de colector no puede ser negativa!")
            print(f"Tensión de colector-emisor: {VCE}.\nIntensidad de colector: {IC}.\nEl transistor está saturando!")
            return
        elif (VBB <=0 or VCC <=0):
            print("El valor de las fuentes no pueden ser negativas:\nVBB = {}\nVCC = {}".format(VBB,VCC))
            return
        else:
            ### Calculando y representando datos.
            print("Calculando...")
            print(f"Valores:\nTensión de emisor: {VE}V\nTensión de colector: {VC}V\nTensión colector-Emisor: {VCE}V"
          f"\nIntensidad de colector: {IC}A")
            ### Pintando la recta de carga y su punto Q
            # Puntos de la recta de carga
            VCE_max = VCC  # Cuando IC = 0, VCE = VCC
            IC_max = VCC / (RC + RE)  # Cuando VCE = 0, IC = VCC / (RC + RE)
            # Coordenadas del punto Q (ajusta según tus valores)
            VCE_Q = VCE
            IC_Q = IE
            # Crear los ejes
            plt.plot([0, VCE_max], [IC_max, 0], label='Recta de Carga')
            # Etiquetas de los ejes
            plt.xlabel('VCE (V)')
            plt.ylabel('IC (mA)')
            # Agregar el punto Q
            plt.plot(VCE_Q, IC_Q, 'ro', label='Punto Q')
            plt.title('Recta de Carga de un Amplificador con Polarización de Emisor Común')
            # Limitar los ejes para una mejor visualización
            plt.xlim(0, VCE_max*1.2)
            plt.ylim(0, IC_max*1.2)
            # Mostrar la cuadrícula
            plt.grid(True)
            # Mostrar la leyenda
            plt.legend()
            # Mostrar el gráfico
            plt.show()
            return()

print(color.RED)   
 
def polarizador():
    ##########################################################################
    ################ https://mirpas.com/Lenguajes/4/6p.php ###################
    ##########################################################################
    os.system('cls')
    print("Vamos a configurar los componentes del circuito polarizador:")
    img = plt.imread("img/2.png") #ruta relativa o absoluta
    plt.imshow(img)
    plt.title('Esta ventana se cerrará en breve')
    plt.show(block=False)
    plt.pause(5)
    plt.close()
    print("Configuremos los valores del divisor de tensión:")
    R1 = int(input("Escribe el valor de la resistencia R1: "))
    R2 = int(input("Escribe el valor de la resistencia R2: "))
    RE = int(input("Escribe el valor de la resistencia de emisor: "))
    RC = int(input("Escribe el valor de la resistencia de colector: "))
    VCC = int(input("Escribe el valor de la tensión de alimentación: "))
    VBB = (R2/(R1+R2))*VCC
    VE = VBB-0.7
    IE = VE / RE
    IC = IE
    VC = VCC - (IC * RC)
    VCE = VC - VE
    VCE_max = VCC #Para pintar la recta de carga
    IC_max = VCC / (RE + RC)#Para pintar la recta de carga
    #Para pintar el punto Q
    VCE_Q = VCE
    IC_Q = IC
    

    #Escogemos el transistor de trabajo
    tr = ['BC546','BC546B','BC547A','BC547B','BC547C','BC548A','BC548B','BC548C']
    for indice, lista in enumerate(tr):
        print(f"Escoge el número {indice} para el transistor {lista}")
    transistor = int(input("Escoge el transistor a utilizar:"))
    print(f"La tensión de emisor es de {VE}V.\nLa tensión de colector es de {VC}V.\nLa tensión de colector-emisor es de {VCE}V\nLa corriente de colector es de {IC}A")
    #Calculamos la ganancia respecto a la elección del transistor
    if transistor == 0 or transistor == 1: #BC546,BC546B
        if (IC >0.00002) & (IC < 0.05):
            ganancia_estimada = ganancia(IC)
            print("Ganancia estimada con esta intensidad:", ganancia_estimada)
            impedancia= ganancia_estimada * RE * 0.1
            Thevenin_divisor= (R1*R2) / (R1+R2)
            if Thevenin_divisor < impedancia:
                print("El divisor de tensión es practicamente constante!")
        elif (IC<0.00001) or (IC>0.1):
            print("La ganancia es de 110")
    if transistor == 3 or transistor==4 or transistor==5 or transistor==6 or transistor==7:# BC547 y BC548
        if (IC >0.00001) & (IC < 0.036):
            ganancia_estimada = ganancia(IC)
            print("Ganancia estimada con esta intensidad:", ganancia_estimada)
            impedancia= ganancia_estimada * RE * 0.1
            Thevenin_divisor= (R1*R2) / (R1+R2)
            if Thevenin_divisor < impedancia:
                print("El divisor de tensión es practicamente constante!")
        elif (IC<0.00001) or (IC>0.1):
            print("La ganancia es de 120")
    plt.plot([0,VCE_max],[IC_max,0], label='recta de Carga')
    plt.xlabel('VCE (V)')
    plt.ylabel('IC (mA)')
    plt.plot(VCE_Q,IC_Q, 'ro', label='Punto Q')
    plt.title('Recta de carga de un amplificador con polarizador de tensión y emisor común')
    plt.xlim(0,VCE_max * 1.2)
    plt.ylim(0,IC_max * 1.2)
    plt.grid(True)
    plt.legend()
    plt.show()
    return()
    #Calculamos la ganancia para cierta corriente
print(color.GREEN)   
def ganancia(corriente):
    if corriente<corrientes[0] or corriente > corrientes[-1]:
        return "Corriente fuera de rango"
    else:
        indice=np.searchsorted(corrientes,corriente, side='right') -1
        x1, x2 = corrientes[indice:indice+2]
        y1,y2 = ganancias[indice:indice + 2]
        return y1 + (corriente - x1)*(y2-y1) / (x2-x1)

def realimentador():
    ##########################################################################
    ###### https://mirpas.com/Lenguajes/4/projects/amplipy_final.php #########
    ##########################################################################
    os.system('cls')
    print("Vamos a configurar el circuito de realimentación de emisor.")
    print("Escribe los valores del circuito:")
    img = plt.imread("img/3.png") #ruta relativa o absoluta
    plt.imshow(img)
    plt.title('Esta ventana se cerrará en breve')
    plt.show(block=False)
    plt.pause(5)
    plt.close()
    RE = int(input("Escribe el valor de la resistencia de emisor RE: "))
    RC = int(input("Escribe el valor de la resistencia colector RC: "))
    RB = int(input("Escribe el valor de la resistencia de base RB: "))
    VCC = int(input("Escribe el valor de la tensión de alimentación: "))
    ganancia= int(input("Introduce el valor de la ganancia: "))
    Re = RE + (RB/ganancia)
    IE = (VCC-0.7) / Re
    IC = IE
    IB = IC / ganancia
    VC = IC * RC
    Vtransistor = VCC - VC
    VE = IC * RE
    VCE = Vtransistor - VE
    VCE_max = VCC #Para pintar la recta de carga
    IC_max = VCC / (RE + RC)#Para pintar la recta de carga
    #Para pintar el punto Q
    VCE_Q = VCE
    IC_Q = IC
    print(f"La tensión de emisor es de {VE}V.\nLa tensión de colector es de {VC}V.\nLa tensión de colector-emisor es de {VCE}V\nLa corriente de colector es de {IC}A\nLa corriente de base es de {IB}A")
    plt.plot([0,VCE_max],[IC_max, 0], label="Recta de carga")
    plt.xlabel('VCE (V)')
    plt.ylabel('IC (mA)')
    plt.plot(VCE_Q, IC_Q, 'ro', label="Punto Q")
    plt.title('Polarización con realimentación de emisor')
    plt.xlim(0,VCE_max*1.2)
    plt.ylim(0, IC_max*1.2)
    plt.grid(True)
    plt.legend()
    plt.show()
    return()
print(color.DARKCYAN)   
if circuito==1:dosFuentes()
elif circuito==2:polarizador()
elif circuito==3:realimentador()
else: print("Opción no válida!")