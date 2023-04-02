import pyautogui as py
import time

rep = int(input("repetiton : "))

py.click(1013, 107)
time.sleep(0.7)
py.click(1651, 354)
time.sleep(0.7)
py.click(1703, 247)
time.sleep(0.7)
py.click(1848, 74)
time.sleep(0.7)

for i in range(rep):
    py.click(1126, 513)
    time.sleep(0.9)
    py.click(1741, 498)
    time.sleep(0.5)
    py.click(1542, 481)
    time.sleep(0.6)
    py.click(1247, 169)
    time.sleep(0.6)
    py.click(1126, 513)
    time.sleep(1.1)
    py.click(1594, 497)
    time.sleep(0.6)
    py.click(1496, 341)
    time.sleep(1.1)
    print(i+1)
