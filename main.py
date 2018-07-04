#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PowerSupplyFunctions import *

p = "/dev/ttyUSB0"
port_open(p)

while 1:
    power_off(p)
    time.sleep(2)
    power_on(p)
    time.sleep(2)
