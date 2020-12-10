import time
import pyautogui as p
import random

cant_facturas = 50
arreglos = ["Reparaciones Varias"]
time.sleep(3)
for i in range(cant_facturas):
    #---------------------- 0 ----------     -----
    p.moveTo(944,361)
    p.click()
    time.sleep(1)
    # ---------------------- 1 ---------------
    p.moveTo(984,348)
    p.click()
    time.sleep(0.5)
    # ---------------------- 2 ---------------
    p.moveTo(1013,398)
    p.click()
    time.sleep(0.2)
    # ---------------------- 3 ---------------
    p.moveTo(983,395)
    p.click()
    time.sleep(0.2)
    # ---------------------- 4 ---------------
    p.moveTo(973,527)
    p.click()
    # ---------------------- 5 ---------------
    p.moveTo(998,474)
    p.click()

    # Carga fecha
    time.sleep(12)
    p.moveTo(998,916)
    p.click()
    time.sleep(2)

    # ---------------------- 6 ---------------
    p.moveTo(909,346)
    p.click()
    time.sleep(0.5)
    # ---------------------- 7 ---------------
    p.moveTo(924,426)
    p.click()
    time.sleep(0.2)
    # ---------------------- 8 ---------------
    p.moveTo(905,389)
    p.click()
    time.sleep(0.2)
    # ---------------------- 9 ---------------
    p.moveTo(862,533)
    p.click()
    time.sleep(0.2)
    # ---------------------- 12 --   -------------
    p.moveTo(1042,386)
    p.click()
    p.moveTo(1078,438)
    p.click()
    time.sleep(2.5)
    # Tab + espacio + roll abajo
    p.typewrite("\t")
    p.typewrite(" ")

    # ---------------------- 13 ---------------
    p.moveTo(602,628)
    p.click()
    p.scroll(-500)
    p.moveTo(996,854)
    p.click()
    time.sleep(1.5)
    # ---------------------- 14 ---------------
    p.moveTo(485,401)
    p.click()
    p.typewrite(random.choice(arreglos))
    p.typewrite("\t\tu\t")
    time.sleep(3)
    p.typewrite("\t\t\t21")
    # ---------------------- 15 ---------------
    p.moveTo(990,799)
    p.click()
    time.sleep(3)

    # ---------------------- 16 ---------------
    p.scroll(-700)
    p.moveTo(976,855)
    p.click()
    time.sleep(0.2)
    p.typewrite("\n")
    time.sleep(1.5)
    p.moveTo(954,983)
    p.click()
    time.sleep(1.5)
