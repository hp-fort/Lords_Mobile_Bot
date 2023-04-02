import pyautogui as py
import time

#input
coordonne = input("coordonné : ")
rss = input("ressouce demander (8m/10m/7m/85k/5m) : ")
rep = int(input("repetition : "))

#coordonné points
def one():
    py.click(1605, 260)
def two():
    py.click(1670, 260)
def tree():
    py.click(1740, 260)
def four():
    py.click(1605, 310)
def five():
    py.click(1670, 310)
def six():
    py.click(1740, 310)
def seven():
    py.click(1605, 340)
def height():
    py.click(1670, 340)
def nine():
    py.click(1740, 340)
def zero():
    py.click(1620, 400)
def clear():
    py.click(1720, 400)


#aller au coordonné
r = 1
py.click(1448, 108)
time.sleep(0.7)
py.click(1448, 239)
time.sleep(0.7)
for nb in coordonne:
    if nb == "1":
        one()
    if nb == "2":
        two()
    if nb == "3":
        tree()
    if nb == "4":
        four()
    if nb == "5":
        five()
    if nb == "6":
        six()
    if nb == "7":
        seven()
    if nb == "8":
        height()
    if nb == "9":
        nine()
    if nb == "0":
        zero()
    time.sleep(0.7)
    time.sleep(5)
    
    if r == 2:
        clear()
        time.sleep(0.7)
        py.click(1543, 239)
        time.sleep(0.7)
    r+=1
clear()
time.sleep(2)
"""
time.sleep(10)
#selectionner les rss
rss = rss.split("/")
food = rss[0]
stone = rss[1]
wood = rss[2]
ore = rss[3]
gold = rss[4]


if food.endswith("k"):
    food = food.split("k")
    food = float(food[0])
    food *= 1000
    food = round(food)
elif food.endswith("m"):
    food = food.split("m")
    food = float(food[0])
    food *= 1000000
    food = round(food)
elif food.endswith("b"):
    food = food.split("b")
    food = float(food[0])
    food *= 1000000000
    food = round(food)

if stone.endswith("k"):
    stone = stone.split("k")
    stone = float(stone[0])
    stone *= 1000
    stone = round(stone)
elif stone.endswith("m"):
    stone = stone.split("m")
    stone = float(stone[0])
    stone *= 1000000
    stone = round(stone)
elif stone.endswith("b"):
    stone = stone.split("b")
    stone = float(stone[0])
    stone *= 1000000000
    stone = round(stone)

if wood.endswith("k"):
    wood = wood.split("k")
    wood = float(wood[0])
    wood *= 1000
    wood = round(wood)
elif wood.endswith("m"):
    wood = wood.split("m")
    wood = float(wood[0])
    wood *= 1000000
    wood = round(wood)
elif wood.endswith("b"):
    wood = wood.split("b")
    wood = float(wood[0])
    wood *= 1000000000
    wood = round(wood)

if ore.endswith("k"):
    ore = ore.split("k")
    ore = float(ore[0])
    ore *= 1000
    ore = round(ore)
elif ore.endswith("m"):
    ore = ore.split("m")
    ore = float(ore[0])
    ore *= 1000000
    ore = round(ore)
elif ore.endswith("b"):
    ore = ore.split("b")
    ore = float(ore[0])
    ore *= 1000000000
    ore = round(ore)

if gold.endswith("k"):
    gold = gold.split("k")
    gold = float(gold[0])
    gold *= 1000
    gold = round(gold)
elif gold.endswith("m"):
    gold = gold.split("m")
    gold = float(gold[0])
    gold *= 1000000
    gold = round(gold)
elif gold.endswith("b"):
    gold = gold.split("b")
    gold = float(gold[0])
    gold *= 1000000000
    gold = round(gold)


#envoyer les rss
time.sleep(5)
for i in range(rep):
    py.click(1423, 322)
    time.sleep(0.7)

    py.click(1349, 389)
    time.sleep(0.7)

    py.click(1445, 286)
    time.sleep(0.7)
#
#    ^^ selectionner la bonne rss, refaire les points ^^
#    
    py.click(1672, 504)
    time.sleep(0.7)

    py.click(1492, 282)
    time.sleep(1)

    py.click(1437, 396)
    time.sleep(5)
#    time.sleep(5) --> ajuster le temps en fonction du temps de déplacement du chariot
    print(i+1)
"""