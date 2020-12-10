import pandas as pd
from scipy.stats import chisquare
from scipy import stats
from scipy.stats import chi2_contingency
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import random

import math

style = 'MacOSX'


def prueba_chi2(numeros, intervalos):
    if len(numeros) < 30:
        return -1

    if intervalos <= 0:
        intervalos = int(round(pow(len(numeros),0.5),0))   #Modifica los intervalos para cuando no se pasa el parámetro, o es un parámetro inválido

    add = 1 / intervalos
    inter = [0] * (intervalos + 1)
    inter[-1] = 1.0
    i = 0
    x = 0
    while inter[i] != 1:
        inter[i] = x
        x = x + add
        i += 1

    count = [0] * intervalos
    for x in range(len(numeros)):
        for i in range(1, intervalos + 1):
            if numeros[x] < inter[i]:
                count[i - 1] += 1
                break

    inter = np.array(inter)
    count = np.array(count)

    esperado = [len(numeros) / intervalos] * len(count)
    # Aca tenemos los intervalos y los contadores inter y count

    matriz = [count, esperado]

    stat, p, dof, expected = chi2_contingency(matriz)
    # seleccionar el valor de significancia
    alpha = 0.05
    # Deternminar si la hipotesis es rechazada o no
    print('\nsignificance=%.3f, p=%.3f' % (alpha, p),'\n')
    if p <= alpha:
        print('Las variables estan ascociadas (se rechaza la hipotesis)\n')
    else:
        print('Las variables no estan asociadas(no se rechaza la hipotesis)\n')

    df = pd.DataFrame({"Numeros": numeros})
    df.Numeros.plot.hist(bins=intervalos)
    plt.axhline(y=esperado[0], xmin=0, xmax=1, color="red")
    plt.xlabel('Intervalos')
    plt.ylabel('Frecuencia')
    plt.legend('EO')
    plt.title('Distribucion de los valores acuerdo a su frecuencia')
    plt.grid()

    plt.show()


def func_aleatoria_lineal(x, a, m, c):
    resultado = (a * x + c) / m
    decimal, entero = math.modf(resultado)
    return decimal * m


def generador_aleatorio_lineal(x, k, g, c):
    a = 1 + 4 * k
    m = pow(2, g)
    xi = func_aleatoria_lineal(x, a, abs(m), c)
    ri = xi / (m - 1)
    return xi, ri


def funcion_aleatoria_multiplicativa(a, x, m):
    return func_aleatoria_lineal(x, a, m, 0)


def generador_aleatorio_multiplicativo(x, k, g):
    a = 3 + 8 * k
    m = pow(2, g)
    xi = funcion_aleatoria_multiplicativa(x, a, abs(m))
    ri = xi / (m - 1)
    return xi, ri

def check_primo(a,b):
    if (a == 0 or b == 0): return 0

    if (a == b): return a

    if (a > b):
        return check_primo(a - b, b)

    return check_primo(a, b - a)

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def coprime(a, b):
    if (check_primo(a, b) == 1):
        return True
    else:
        return False

def validar_1(x,k,g):
    bandera = True
    if isinstance(g, int) and isinstance(k, int) and k >= 0 and x // 2 != 0:
        return bandera
    else:
        bandera = False
        return bandera

def validar_2(g,k,c):
    bandera = False
    if isinstance(g, int) and isinstance(k, int) and coprime(c, pow(2,g)):
        bandera = True
        return bandera
    else:
        return bandera

def metodo_multiplicativo():
    x = int(input('\nIngrese el primer valor: '))
    k = int(input('Ingrese el valor de k: '))
    g = int(input('Igrese el valor de g: '))

    validacion = validar_1(x,k,g)
    if validacion:
        numeros = []
        xs = []

        for i in range(20):
            xs.append(x)
            xi, ri = generador_aleatorio_multiplicativo(x, k, g)
            numeros.append(ri)

            x = xi

        print('\n     RESULTADOS')
        for i in range(len(numeros)):
            numeros[i] = truncate(numeros[i],4)
        print(numeros)
        print('\nPresione ENTER para ir pasando de numero (detener con 0): ')
        continuar = input(" ")
        while continuar != 0:
            xs.append(x)
            xi, ri = generador_aleatorio_multiplicativo(x, k, g)
            numeros.append(ri)
            x = xi
            print(truncate(ri,4))
            continuar = input('')
            if continuar == "0":
                break
        print('\n Fin de la serie.')
        print('\n     RESULTADOS')
        for i in range(len(numeros)):
            numeros[i] = truncate(numeros[i], 4)
        print(numeros)

    else:
        print('Algun valor fue mal cargado, intente de nuevo. \n')


def metodo_lineal():
    x = int(input('\nIngrese el valor de Xo: '))
    k = int(input('Ingrese el valor de k: '))
    g = int(input('Ingrese el valor de g: '))
    c = int(input('Ingrese el valor de c: '))

    validacion = validar_2(g,k,c)

    if validacion:
        numeros = []
        xs = []

        for i in range(20):
            xs.append(x)
            xi, ri = generador_aleatorio_lineal(x, k, g, c)
            numeros.append(ri)

            x = xi

        print('\n     RESULTADOS')
        for i in range(len(numeros)):
            numeros[i] = truncate(numeros[i], 4)
        print(numeros)
        print('\nPresione ENTER para ir pasando de numero (detener con 0): ')
        continuar = input(" ")
        while continuar != 0:
            xs.append(x)
            xi, ri = generador_aleatorio_lineal(x, k, g, c)
            numeros.append(ri)
            x = xi
            print(truncate(ri, 4))
            continuar = input('')
            if continuar == "0":
                break
        print('\n Fin de la serie.')
        print('\n     RESULTADOS')
        for i in range(len(numeros)):
            numeros[i] = truncate(numeros[i], 4)
        print(numeros)

    else:
        print('Algun valor fue mal cargado, intente de nuevo. \n')


def metodo_lineal_2(cant):
    x = int(input('\nIngrese el primer valor: '))
    k = int(input('Ingrese el valor de k: '))
    g = int(input('Ingrese el valor de g: '))
    c = int(input('Ingrese el valor de c: '))

    validacion = validar_2(g,k,c)

    if validacion:
        numeros = []
        for i in range(cant):
            xi, ri = generador_aleatorio_lineal(x, k, g, c)
            numeros.append(ri)
            x = xi
    return numeros



def main():
    print("-----------------Bienvenido-----------------\n"
          "          Generador de números aleatorios."

          )
    while True:
        print("\n------------------------------------------------------------------\n"
                   "Presione 1 para generar una lista de 20 numeros aleatorios.\n"
                   "Presione 2 para evaluar el método math.random.\n"
                   "Presione 3 para evaluarel método congruencial multiplicativo.\n"
                   "Utilice 0 para salir.\n")
        op = int(input("Introduzca la opcion solicitdad: "))

        if op in (1,2,3,0):
            if op == 1:
                op1()           #Puede elegir entre ambos métodos.

            if op == 2:
                op2()

            if op == 3:
                op3()

            if op == 0:
                break

        else:
            print('Opcion incorrecta, intentelo de nuevo.\n')


def op1():
    metodo = int(input('\nPresione 1 si desea utilizar el metodo congruencial multiplicativo\n'
                   'Presione 2 si desea utilizar el metodo congruencial lineal\n'
                       '\nIntroduzca la opcion solicitdad: '))

    if metodo in (1,2):
        if metodo == 1:
            metodo_multiplicativo()

        if metodo == 2:
            metodo_lineal()
    else:
        print('Opcion incorrecta, intentelo de nuevo.\n')

def op2():
    cant = int(input('Ingrese la cantidad de numeros que quiere generar: '))
    intervalos = int(input('Ingrese la cantidad de intervalos: '))
    if (cant/intervalos) < 5:
        print("\nError al cargar datos, los intervalos tienen frecuencia esperada menor a 5\n")
    else:

        numeros = [random.uniform(0, 1) for x in range(cant)]
        prueba_chi2(numeros, intervalos)

def op3():
    cant = int(input('Ingrese la cantidad de numeros que quiere generar: '))
    intervalos = int(input('Ingrese la cantidad de intervalos: '))
    if (cant/intervalos) < 5:
        print("\nError al cargar datos, los intervalos tienen frecuencia esperada menor a 5\n")
    else:
        significancia = int(input('Ingrese el valor de significancia: '))
        numeros = metodo_lineal_2(cant)
        prueba_chi2(numeros, intervalos, significancia)



main()