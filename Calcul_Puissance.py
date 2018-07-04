#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, platform
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import logging
import syslog
from PowerSupplyFunctions import *

p = "/dev/ttyUSB0"
port_open(p)
i =0 
epoch_time =0
x =0
puissance =0

tab =[0]
tab2 =[0]
v = Vget(p)
while i<10:
    x = Iget(p) # Calcul de courant 
    puissance = v * x # Calcul de puissance
    time.sleep(2) # pause de 2 secondes
    tab.append(puissance) # remplir le premier tableau (puissance)
    date = time.time()
    epoch_time = (date)
    t = time.strftime("%Hh:%Mm:%Ss", time.localtime(epoch_time))
    tab2.append(t)
    i = i + 1

# Création de fichier log 
logging.basicConfig(filename='log_calcul_puissance.log',level=logging.DEBUG,\
      format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')
logging.info('Start of the program ...')
logging.info('Power calculation')
time.sleep(3)
logging.info('Display the graph')
logging.warning('End of the program')
##############################################################################

print ("la valeur de puissance est ",tab)
print ("la date d'aujoud'hui est ",tab2)
plt.plot(tab2, tab)
plt.xlabel('Temps (t)')
plt.ylabel('Puissance P (Watt)')
plt.title("Consommation de Puissance / Temps")
plt.show() 

