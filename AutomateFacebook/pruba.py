import time
import pyautogui
import easygui as eg

for i in range(10):
    print("-------------------"+str(i+10)+"--------------------------")
    eg.msgbox(msg='Apunta en 3 a donde',
              title='Control: msgbox',
              ok_button='Continuar'
            )
    time.sleep(3)
    print(pyautogui.position())