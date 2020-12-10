import random
from Clases import Entrada_Class
from Clases import Server_Class
import pandas as pd
import numpy as np

from Clases.Entrada_Class import Entrada


def uniforme(lim_inf,lim_sup):
    rnd = random.random()
    t = lim_inf + rnd*(lim_sup-lim_inf)
    return rnd,t

def generar_miles(cant_sim,desde,hasta):
    tabla = []
    aux = 0

    ############################################################# PARAMETROS ########################################################333

    dist_llegada_i = 10
    desv_llegada_i = 2
    dist_entrada_i = 0.085
    desv_entrada_i = 0.035
    dist_atencion_i = 9
    desv_atencion_i = 5

    dist_llegada_r = 15
    desv_llegada_r = 3
    dist_entrada_r = 0.25
    desv_entrada_r = 0.05
    dist_atencion_r = 7
    desv_atencion_r = 2

    dist_interr = 180
    desv_int = 20
    tiempo_int = 1.03 * 60

    ###################################### Parametrización ####################

    d_inf_li = dist_llegada_i - desv_llegada_i
    d_sup_li = dist_llegada_i + desv_llegada_i
    d_inf_ei = dist_entrada_i - desv_entrada_i
    d_sup_ei = dist_entrada_i + desv_entrada_i
    d_inf_ai = dist_atencion_i - desv_atencion_i
    d_sup_ai = dist_atencion_i + desv_atencion_i

    d_inf_lr = dist_llegada_r - desv_llegada_r
    d_sup_lr = dist_llegada_r + desv_llegada_r
    d_inf_er = dist_entrada_r - desv_entrada_r
    d_sup_er = dist_entrada_r + desv_entrada_r
    d_inf_ar = dist_atencion_r - desv_atencion_r
    d_sup_ar = dist_atencion_r + desv_atencion_r

    d_inf_int = dist_interr - desv_int
    d_sup_int = dist_interr + desv_int


    informes = Server_Class.Server("Libre",0,0,0)
    reservas = Server_Class.Server("Libre",0,0,0)

    reloj = 0
    evento = "Inicio"
    #Llegadas
    t_fin_li, t_fin_lr = 99999,99999
    #Atencion
    t_fin_ai, t_fin_ar = 99999, 99999
    #Interrupcion
    fin_int = 99999
    #Colas
    cola_actual, cola_actual_r = 0,0
    atendidos_i, atendidos_r = 0,0
    max_cola_i , max_cola_r = 0,0
    cola_max = 0
    acum_t_int = 0


    t_fin_i = uniforme(d_inf_li,d_sup_li)[1]
    t_fin_r = uniforme(d_inf_lr,d_sup_lr)[1]
    prox_int = uniforme(d_inf_int,d_sup_int)[1]

    t_int = 1.03        #Faltan unidades de integración

    columns = ["Nro Sim","Evento","Reloj","Rnd Entrada I","T Prox Ent I","Prox Entrada I","Rnd Mesa I","T Mesa I","T Llegada Mesa I","Cola Actual I","Atendidos I",
             "Max cola I","Rnd Atención I","T Atención I","T Fin Atención I","Estado Inf","Inicio TL Inf","Fin TL Inf","Acum TL Inf","Rnd Se queda","Se queda?",
              "Rnd Entrada R","T Entrada R","T Prox Entrada R","Rnd Mesa R","T Mesa R","T Fin Mesa R","Cola Actual R","Atendidos R","Max cola R","Rnd Atención R", "T Atención R",
             "T Fin Atención R","Estado Res","Inicio TL Res","Fin TL Res","Acum TL Res","MAX Colas","Atendidos Tot","Rnd Int","T Prox Int", "Prox Int",
             "T Fin Int","Acum T Int","% T Int"]


    df = pd.DataFrame(columns=columns)
    primero = False
    t_fin_int = 0



    for i in range(cant_sim):
        # Entrada Informe
        rnd_i, t_i = 0,0

        # Llegada Informe
        rnd_li, t_li = 0,0

        # Atención Informes
        rnd_ai, t_ai = 0,0

        # Entrada Reservas
        rnd_r, t_r = 0, 0

        # Llegada Reservas
        rnd_lr, t_lr = 0, 0

        # Atención  Reservas
        rnd_ar, t_ar = 0, 0

        # Se queda
        rnd_res = 0
        se_queda = ""

        #Interrupciones
        rnd_int = 0

        t_int = 0

        if primero:
            opcion = min(t_fin_i,t_fin_ai,t_fin_li,t_fin_r,t_fin_ar,t_fin_lr, prox_int,fin_int)

            ########################## Entra para informes #############################
            if opcion == t_fin_i:
                reloj = t_fin_i
                evento = "Entrada Persona a Informes"
                rnd_i,t_i = uniforme(d_inf_li,d_sup_li)
                t_fin_i = t_i + reloj
                rnd_li, t_li = uniforme(d_inf_ei,d_sup_ei)
                t_fin_li = reloj + t_li

            ########################## Finalmente llega  a informes
            elif opcion == t_fin_li:
                reloj = t_fin_li
                t_fin_li = 99999
                evento = "Llegada Persona a Mesa I"
                if informes.estado == "Libre":
                    rnd_ai,t_ai = uniforme(d_inf_ai,d_sup_ai)
                    t_fin_ai = t_ai + reloj
                    informes.estado = "Ocupado"
                    informes.t_fin = reloj
                    informes.t_ac += informes.t_fin - informes.t_libre
                else:
                    cola_actual += 1
                    if cola_actual > max_cola_i:
                        max_cola_i = cola_actual

            ########################### Termina de atender a informes
            elif opcion == t_fin_ai:
                reloj = t_fin_ai
                t_fin_ai = 99999
                atendidos_i +=1
                evento = "Fin Atención Informes"
                if cola_actual != 0:
                    cola_actual -= 1
                    rnd_ai, t_ai = uniforme(d_inf_ai, d_sup_ai)
                    t_fin_ai = t_ai + reloj
                    informes.estado = "Ocupado"
                else:
                    informes.estado = "Libre"
                    informes.t_libre = reloj
                    informes.t_fin = 0
                rnd_res = random.random()
                se_queda = "NO"
                if rnd_res > 0.6:
                    se_queda = "SI"
                    if reservas.estado == "Libre":
                        rnd_ar, t_ar = uniforme(d_inf_ar, d_sup_ar)
                        t_fin_ar = t_ar + reloj
                        reservas.estado = "Ocupado"
                        reservas.t_fin = reloj
                        reservas.t_ac += reservas.t_fin - reservas.t_libre
                    else:
                        cola_actual_r += 1
                        if cola_actual_r > max_cola_r:
                            max_cola_r = cola_actual_r
            ########################## Entra para Reservas #############################
            elif opcion == t_fin_r:
                reloj = t_fin_r
                evento = "Entrada Persona a Reservas"
                rnd_r, t_r = uniforme(d_inf_lr, d_sup_lr)
                t_fin_r = t_r + reloj
                rnd_lr, t_lr = uniforme(d_inf_er, d_sup_er)
                t_fin_lr = reloj + t_lr
            ########################## Finalmente llega  a Reservas
            elif opcion == t_fin_lr:
                reloj = t_fin_lr
                t_fin_lr = 99999
                evento = "Llegada Persona a  Mesa R"
                if reservas.estado == "Libre":
                    rnd_ar, t_ar = uniforme(d_inf_ar, d_sup_ar)
                    t_fin_ar = t_ar + reloj
                    reservas.estado = "Ocupado"
                    reservas.t_fin = reloj
                    reservas.t_ac += reservas.t_fin - reservas.t_libre
                else:
                    cola_actual_r += 1
                    if cola_actual_r > max_cola_r:
                        max_cola_r = cola_actual_r
            ########################### Termina de atender a Reservas
            elif opcion == t_fin_ar:
                reloj = t_fin_ar
                t_fin_ar = 99999
                atendidos_r += 1
                evento = "Fin Atención Reservas"
                if cola_actual_r != 0:
                    cola_actual_r -= 1
                    rnd_ar, t_ar = uniforme(d_inf_ar, d_sup_ar)
                    t_fin_ar = t_ar + reloj
                    reservas.estado = "Ocupado"
                else:
                    reservas.estado = "Libre"
                    reservas.t_libre = reloj
                    reservas.t_fin = 0
            ########################### Nueva interrupcion
            elif opcion == prox_int:

                evento = "Inicio interrupción"
                reloj = prox_int
                prox_int = 99999
                t_int = tiempo_int
                t_fin_int = reloj + tiempo_int

                fin_int = reloj + tiempo_int
                ant_inf = informes.estado
                ant_res = reservas.estado
                informes.estado = "Interrumpido"
                reservas.estado = "Interrumpido"
                if t_fin_ai != 99999:
                    t_fin_ai += tiempo_int
                if t_fin_ar != 99999:
                    t_fin_ar += tiempo_int

            elif opcion == fin_int:
                evento = "Fin Interrupción"
                reloj = fin_int
                fin_int = 99999
                t_fin_int = 0
                acum_t_int += tiempo_int
                informes.estado = ant_inf
                reservas.estado = ant_res
                rnd_int, t_int = uniforme(d_inf_int, d_sup_int)
                prox_int = reloj + t_int

            a = cola_actual_r + cola_actual
            if a > cola_max:
                cola_max = a
        primero = True
        aux = Entrada(i,evento,reloj,
            #Entrada Informe
                 rnd_i,t_i,t_fin_i,
                 #Llegada Informe
                 rnd_li,t_li,t_fin_li,
                 #Colas informes
                 cola_actual, atendidos_i, max_cola_i,
                 #Atención Informes
                 rnd_ai, t_ai, t_fin_ai,
                 #Informes
                 informes,
                 #Reservas
                 rnd_res, se_queda,
                 # Entrada Reserva
                 rnd_r, t_r, t_fin_r,
                 # Llegada Reserva
                 rnd_lr, t_lr, t_fin_lr,
                 # Colas Reservas
                 cola_actual_r, atendidos_r, max_cola_r,
                 #Cola max total
                 cola_max,
                 # Atención Reservas
                 rnd_ar, t_ar, t_fin_ar,
                 # Reservas
                 reservas,
                #Interrupciones
                 rnd_int, t_int, prox_int, t_fin_int,
                 #Est interrup
                 acum_t_int)

        if (i >= desde and i<=hasta) or (i == cant_sim-1):
            df_new = pd.DataFrame([aux.tolist()],columns=columns)
            df = df.append(df_new)

    return (df)





generar_miles(1000,0,200)
