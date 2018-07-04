#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
from PowerSupplyFunctions import *


p = "/dev/ttyUSB0"
port_open(p)
i =0 
epoch_time =0
x =0
tab= [0]
tab2= [0]
while i<10:
    x = Iget(p)
    time.sleep(3)
    tab.append(x)
    date = time.time()
    epoch_time = (date)
    t =time.strftime("%Hh:%Mm:%Ss ", time.localtime(epoch_time))
    tab2.append(t)
    i = i+1
print ("la valeur de la courant est ",tab)
print ("la date d'aujoud'hui est ",tab2)  
plt.plot(tab2, tab)
plt.xlabel('Temps T')
plt.ylabel('Courant I (A)')
plt.title("Consommation de courant / Temps")
plt.show() # affiche la figure a l'ecran



