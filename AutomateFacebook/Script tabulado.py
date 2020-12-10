import time
import pyautogui




time.sleep(5)
arch_group = open("groups.txt","r")
groups = []

for linea in arch_group.readlines():
    groups.append(linea)
arch_group.close()

publics = []
for i in range(len(groups)):
    name = "publicacion"+str(i+1)+".txt"
    archivo = open(name,"r")
    publicacion =[]
    for linea in archivo.readlines():

        publicacion.append(linea.strip("\n"))
    publics.append(publicacion)



for i in range(len(groups)):
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown("t")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("t")
    link = "https://www.facebook.com/groups/"+groups[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')
    time.sleep(8)

    ##Tabs para llegar ¿a que estas pensando?
    for k in range(20):
        pyautogui.typewrite("\t")
        time.sleep(0.33)
    pyautogui.typewrite("\n")
    time.sleep(4)
    pyautogui.typewrite(publics[i][0])


    ##Tabs para llegar a fotos
    for k in range(5):
        pyautogui.typewrite("\t")
    pyautogui.typewrite("\n")
    time.sleep(5)
    pyautogui.typewrite(publics[i][1].replace("/", "\\"))
    pyautogui.typewrite("\n")
    time.sleep(3)


    pyautogui.typewrite("\t")
    for j in range(len(publics[i])-2):
        pyautogui.typewrite("\n")
        time.sleep(4)
        pyautogui.typewrite(publics[i][2+j].replace("/","\\"))
        pyautogui.typewrite("\n")
        time.sleep(3)
    time.sleep(4)

    #Llegar hasta el boton publicar
    for k in range(5):
        pyautogui.typewrite("\t")
    #pyautogui.typewrite("\n")
