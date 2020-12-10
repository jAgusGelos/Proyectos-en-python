from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
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

pyautogui.keyDown('ctrl')
pyautogui.keyDown("t")
pyautogui.keyUp("ctrl")
pyautogui.keyUp("t")



for i in range(len(groups)):
    link = "https://www.facebook.com/groups/"+groups[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')
    time.sleep(3)
    pyautogui.moveTo(875,470)
    pyautogui.click()
    time.sleep(3)
    pyautogui.typewrite(publics[i][0])

    pyautogui.moveTo(1004, 659)
    pyautogui.click()
    time.sleep(3)
    pyautogui.typewrite(publics[i][1].replace("/", "\\"))
    pyautogui.typewrite("\n")
    time.sleep(2)
    for j in range(len(publics[i])-2):
        pyautogui.moveTo(1005,811)
        pyautogui.click()
        time.sleep(3)
        pyautogui.typewrite(publics[i][2+j].replace("/","\\"))
        pyautogui.typewrite("\n")
        time.sleep(2)
    time.sleep(3)
    pyautogui.moveTo(888,887)
    pyautogui.click()








