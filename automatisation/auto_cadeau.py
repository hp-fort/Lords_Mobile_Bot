import pyautogui as py
import time

nb_kdo = int(input("nombre de cadeau : "))

if nb_kdo%4 == 1:
    nb_kdo += 3
if nb_kdo%4==2:
    nb_kdo+=1
if nb_kdo%4==3:
    nb_kdo+=1

print(nb_kdo)

if nb_kdo%4==0:
    nb_kdo = nb_kdo / 4
    print(nb_kdo)
    for i in range(round(nb_kdo)):
        py.click(1784, 265)
        time.sleep(0.5)
        py.click(1784, 348)
        time.sleep(0.5)
        py.click(1784, 431)
        time.sleep(0.5)
        py.click(1784, 517)
        time.sleep(0.5)
        py.click(1707, 152)
        time.sleep(0.5)