import TP3_SIM as fn

def menu():
    print("===================Bienvenidos===================")
    print("\nSeleccione la distribución:"
          "\n1 - Uniforme"
          "\n2 - Exponencial"
          "\n3 - Poisson"
          "\n4 - Normal"
          "\n0 - Salir")

def visualizar(numeros):
    print(numeros)

def prueba_chi23(numeros, cant_int):
    paso = (max(numeros)- min(numeros)) / cant_int             # Esta variable me permite generar los intervalos
    inicio = min(numeros)
    intervalos = []
    contador = []
    esperado = len(numeros) / cant_int     # Aqui obtenemos el valor de frecuencia esperado para cada intervalo siguiendo una distribución uniforme.
    frec_esperada = []
    for i in range(cant_int):       # En este ciclo creamos los intervalos, la cantidad de contadores y la columna esperados
        inicio += paso
        intervalos.append(truncate(inicio,4))   # Ver función truncate(numero, cant_decimales)
        contador.append(0)
        frec_esperada.append(esperado)      # Para cada una de las listas agregamos 0 para el contador, y esperado para la frecuenia esperada.

    for i in range(len(numeros)):           # Para cada numero analiza el intervalo en el cual se encuentra
        for j in range(cant_int):           # y acumula 1 al valor. Aqui vemos la frecuencia obtenida.
            if numeros[i] <= intervalos[j]:
                if numeros[i] > intervalos[j]-paso:
                    contador[j]+=1
                    break

    est_prueba = []
    sumatoria = []
    suma = 0
    for i in range(cant_int):                                           # Debido a que los numeros generados tienen demasiados decimales,
        a = ((frec_esperada[i]-contador[i])**2) / frec_esperada[i]      # con este método truncamos a 4 todos los obtenidos.
        a = truncate(a,4)
        est_prueba.append(a)
        suma += a
        sumatoria.append(suma)
    interval = []
    anterior = 0
    for i in range(cant_int):           #Crea un array de string para imprimir de que valor min a max van los intervalos.
        interval.append("De " + str(anterior) + " a " + str(intervalos[i]))
        anterior = intervalos[i]
    resultados = {'Intervalos': interval, 'FO': contador, 'FE': frec_esperada,'C':est_prueba,'C(AC)':sumatoria}
    res = tabulate(resultados, headers=['Intervalos', 'FO', 'FE', 'C','C(AC)'], tablefmt='fancy_grid')     #Creamos la tabla para imprimir con la librería tabulate
    print(res)

    #ES Ordenado, SI LO QUEREMOS POR COMO APARECIERON SOLO HAY QUE SACAR EL SORTED
    num = {'Número': sorted(numeros)}
    num_list = tabulate(num, headers=['Número'], tablefmt='fancy_grid', showindex=True)      #Imprimimos a modo de tabla los valores obtenidos.
    print(num_list)

    aux = [0]
    for i in range(cant_int):
        aux.append(intervalos[i])

    plt.hist(numeros, bins=aux,edgecolor='black')         #Utilizamos la libreria Pandas para crear DataFrames para poder generar los gráficos.
    plt.axhline(y=esperado, xmin=0, xmax=1, color="red")
    plt.xlabel('Intervalos')
    plt.ylabel('Frecuencia')
    plt.legend('EO')
    plt.title('Distribucion de los valores acuerdo a su frecuencia')
    plt.grid()
    plt.show()
    valor_critico = valor_puntual(cant_int-1)              #Obtenemos el valor crítico para comparar con el estadístico de prueba.
    print("El valor crítico con 95% de significancia es: ", valor_critico)
    print("El estadístico de prueba es: ", suma)
    if valor_critico > suma:
        print("No se puede rechazar la hipótesis nula")
    else:
        print("Se rechaza la hipóteis nula")
    print("\n")




def main():
    op = -1
    while op != 0:
        menu()
        op = int(input("Ingrese su opción: "))
        if op == 1: #Uniforme

            cant_num = int(input("\nIngrese la cantidad de Valores: "))
            inter = int(input("Ingrese la cantidad de invervalos: "))
            lim_inf = float(input("Ingrese el límite inferior: "))
            lim_sup = float(input("Ingrese el límite superior: "))
            numeros = fn.aleatoria_uniforme(cant_num,lim_inf,lim_sup)

            ver = "n"
            ver = input("Desea ver los numeros generados (S/N): ")
            if ver in "sS":
                visualizar(numeros)
            fn.prueba_chi2(numeros, inter, 0, 0, 0)


        if op == 2: #Exponencial

            cant_num = int(input("\nIngrese la cantidad de Valores: "))
            inter = int(input("Ingrese la cantidad de invervalos: "))
            l = float(input("Ingrese lambda (0 si desea ingresar u): "))
            u = 0
            if l == 0:
                u = float(input("Ingrese u: "))
                numeros = fn.aleatoria_exponencial(cant_num,0,u)
            else:
                numeros = fn.aleatoria_exponencial(cant_num, l, 0)

            ver = "n"
            ver = input("Desea ver los numeros generados (S/N): ")
            if ver in "sS":
                visualizar(numeros)
            print("\n======================== Prueba Chi de los numeros ========================")
            fn.prueba_chi2(numeros,inter,1,l,u)

        if op == 3: #Poisson

            cant_num = int(input("\nIngrese la cantidad de Valores: "))
            inter = int(input("Ingrese la cantidad de invervalos: "))
            media = float(input("Ingrese lambda: "))
            numeros = fn.aleatoria_poisson(cant_num,media)

            ver = "n"
            ver = input("Desea ver los numeros generados (S/N): ")
            if ver in "sS":
                visualizar(numeros)
            fn.prueba_chi2(numeros, inter, 1, media, 0)

        if op == 4: #Normal
            op2 = -1
            op2 = int(input("\nIngrese el método que desee: "
                            "\n1 - Box - Muller"
                            "\n2 - Convolución"))
            if op2 == 1:
                #Muller
                cant_num = int(input("\nIngrese la cantidad de Valores: "))
                inter = int(input("Ingrese la cantidad de invervalos: "))
                media = float(input("Ingrese la media (0 por defecto): "))
                des = float(input("Ingrese la desviación estándar (1 por defecto): "))
                numeros = fn.aleatoria_normal_muller(cant_num, media, des)
            if op2 == 2:
                cant_n41um = int(input("\nIngrese la cantidad de Valores: "))
                inter = int(input("Ingrese la cantidad de invervalos: "))
                inter = int(input("Ingrese la cantidad de invervalos: "))
                media = float(input("Ingrese la media (0.5 por defecto): "))
                des = float(input("Ingrese la desviación estándar (0.083 por defecto): "))
                numeros = fn.aleatoria_normal_convolucion(cant_num, media, des)

            ver = "n"
            ver = input("Desea ver los numeros generados (S/N): ")
            if ver in "sS":
                visualizar(numeros)
            fn.prueba_chi2(numeros, inter, 2, 0, 0)

if __name__ == '__main__':
    main()


