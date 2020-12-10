import math
import random
from numpy import log as ln

from Clase import Buffer

media = 0.5
desv = 0.1

def aleatoria_normal_muller( media, desviacion):
    rnd1 = random.uniform(0,1)
    rnd2 = random.uniform(0,1)
    n1 = (pow((-2*ln(rnd1)),0.5)*math.cos(2*math.pi*rnd2))*desviacion + media
   #n2 =  (pow((-2*ln(rnd1)),0.5)*math.sin(2*math.pi*rnd2))*desviacion + media

    return rnd1,rnd2,n1

def principal (cantSim, simDesde, simHasta):

    b1 = Buffer("Libre", 99999, 0, 0)
    b2 = Buffer("Libre", 99999, 0, 0)
    b3 = Buffer("Libre", 99999, 0, 0)

    colaAn = 0
    colaNoAn = 0
    reloj = 0
    rnd1, rnd2, tLlegada = aleatoria_normal_muller(media,desv)
    tProxLlegada = reloj + tLlegada
    evento = "Inicialización"
    primero = False

    for i in range (cantSim):

        rndTipo = " "
        tipo = " "
        rndExpNeg = " "
        tAnalisis = " "
        finAnalisis = " "

        if primero:
