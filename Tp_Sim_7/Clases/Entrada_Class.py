class Entrada:
    def __init__(self, sim, evento,reloj,

                 #Entrada Informe
                 rnd_i,t_i,t_fin_i,

                 #Llegada Informe
                 rnd_li,t_li,t_fin_li,

                 #Colas informes
                 col_actual, col_atend, max_cola,

                 #Atención Informes
                 rnd_ai, t_ai, t_fin_ai,

                 #Informes
                 informe,

                 #Reservas
                 rnd_res, se_queda,

                 # Entrada Reserva
                 rnd_r, t_r, t_fin_r,

                 # Llegada Reserva
                 rnd_lr, t_lr, t_fin_lr,

                 # Colas Reservas
                 col_actual_r, col_atend_r, max_cola_r,

                 #Cola max total
                 max_tota_cola,

                 # Atención Reservas
                 rnd_ar, t_ar, t_fin_ar,

                 # Reservas
                 reserva,

                #Interrupciones
                 rnd_int, t_int, prox_int, t_fin_int,

                 #Est interrup
                 acum_t_int
                 ):
        self.sim = sim
        self.evento = evento
        self.reloj = reloj
        #Entrada Infomes
        self.rnd_i = rnd_i
        self.t_i = t_i
        self.t_fin_i = t_fin_i
        #Llegada informe
        self.rnd_li = rnd_li
        self.t_li = t_li
        if t_fin_li != 99999:
            self.t_fin_li = t_fin_li
        else:
            self.t_fin_li = 0
        #Colas
        self.cola_actual = col_actual
        self.atendidos_i =  col_atend
        self.cola_max = max_cola
        #Atencion Informes
        self.rnd_ai = rnd_ai
        self.t_ai = t_ai
        if t_fin_ai != 99999:
            self.t_fin_ai = t_fin_ai
        else:
            self.t_fin_ai = 0
        #Informes
        self.inf_estado = informe.estado
        self.inf_t_libre = informe.t_libre
        self.inf_t_fin = informe.t_fin
        self.inf_t_ac   = informe.t_ac
        # Pasa reserva
        self.rnd_res = rnd_res
        self.se_queda = se_queda
        # Entrada Reservas
        self.rnd_r = rnd_r
        self.t_r = t_r
        self.t_fin_r = t_fin_r
        # Llegada Reserva
        self.rnd_lr = rnd_lr
        self.t_lr = t_lr
        if t_fin_lr != 99999:
            self.t_fin_lr = t_fin_lr
        else:
            self.t_fin_lr =0
        # Colas
        self.cola_actual_r = col_actual_r
        self.atendidos_r = col_atend_r
        self.cola_max_r = max_cola_r
        # Atencion Reservas
        self.rnd_ar = rnd_ar
        self.t_ar = t_ar
        if t_fin_ar != 99999:
            self.t_fin_ar = t_fin_ar
        else:
            self.t_fin_ar = 0
        # Reservas
        self.res_estado = reserva.estado
        self.res_t_libre = reserva.t_libre
        self.res_t_fin = reserva.t_fin
        self.res_t_ac = reserva.t_ac
        #Cola max:
        self.cola_max_total = max_tota_cola
        self.atend_total = self.atendidos_i + self.atendidos_r
        #Interrupciones
        self.rnd_int = rnd_int
        self.t_int = t_int
        if prox_int!= 99999:
            self.prox_int = prox_int
        else:
            self.prox_int = 0
        self.t_fin_int = t_fin_int
        #Est interrup
        self.acum_t_int = acum_t_int
        if reloj!= 0:
            self.porcentaje =acum_t_int/reloj
        else:
            self.porcentaje = 0
    def tolist(self):
        a = ["Evento","Reloj","Rnd Entrada I","T Prox Ent I","Prox Entrada I","Rnd Mesa I","T Mesa I","T Llegada Mesa I","Cola Actual I","Atendidos I",
             "Max cola I","Rnd Atención I","T Atención I","T Fin Atención I","Estado Inf","Inicio TL Inf","Fin TL Inf","Acum TL Inf","Rnd Se queda","Se queda?",
              "Rnd Entrada R","T Entrada R","T Fin Entrada R","Rnd Mesa R","T Mesa R","T Fin Mesa R","Cola Actual R","Atendidos R","Max cola R","Rnd Atención R", "T Atención R",
             "T Fin Atención R","Estado Res","Inicio TL Res","Fin TL Res","Acum TL Res","MAX Colas","Atendidos Tot","Rnd Int","T Prox Int", "Prox Int",
             "T Fin Int","Acum T Int","% T Int"]

        return [self.sim,self.evento,round(self.reloj,2), round(self.rnd_i,2),round(self.t_i,2), round(self.t_fin_i,2), round(self.rnd_li,2), round(self.t_li,2), round(self.t_fin_li,2),self.cola_actual,self.atendidos_i,
                self.cola_max,round(self.rnd_ai,2),round(self.t_ai,2),round(self.t_fin_ai,2),self.inf_estado,round(self.inf_t_libre,2),round(self.inf_t_fin,2),round(self.inf_t_ac,2),round(self.rnd_res,2),self.se_queda,
                round(self.rnd_r,2),round(self.t_r,2), round(self.t_fin_r,2), round(self.rnd_li,2), round(self.t_lr,2), round(self.t_fin_lr,2),self.cola_actual_r,self.atendidos_r,self.cola_max_r,round(self.rnd_ar,2), round(self.t_ar,2),
                round(self.t_fin_ar,2),self.res_estado,round(self.res_t_libre,2),round(self.res_t_fin,2),round(self.res_t_ac,2), self.cola_max_total,self.atend_total,round(self.rnd_int,2),round(self.t_int,2), round(self.prox_int,2),
                round(self.t_fin_int,2), round(self.acum_t_int,2),round(self.porcentaje,2)]

