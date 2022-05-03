#coding:utf-8
# Auto-Clique
# Auteur: Eric Chabot
# Date de création: 2021-06-11
# Version: 1.0

import pyautogui
import time

print("Auto-Clique\n")

print("Positionnez votre souris à l'endroit voulu. et attendre 5 seconde.")

time.sleep(5)

position = pyautogui.position()

positiona = position.x
positionb = position.y

print("La position de votre souris est {} sur l'axe des X et {} sur l'axe des Y".format(positiona, positionb))

nombreClique = input("\nIndiquez le nombre de cliques voulus: ")
nombreClique = int(nombreClique)

intervale = input("\nIndiquer l'intervale voulue entre les cliques (en seconde):")
intervale = int(intervale)

x = 0
while x < nombreClique:
    pyautogui.click(positiona, positionb)
    time.sleep(intervale)
    x += 1   
    

