#!/usr/bin/python3

import time
import serial

POWER_SUPPLY_ID = "TENMA72-2550V2.0"
GAUGE_SUPPLY_ID = "TENMA 72-2540 V2.1" """FIX ME"""
BENCH_POWER_SUPPLY = "TENMA 72-2710 V2.5"
RESPONSE_TIME = 0.1
ACCURANCY = 0.05

tty = serial.Serial(
   baudrate=9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)


def port_open(port):
    tty.port = port
    if tty.isOpen() is False:
        tty.open()


def port_close(port):
    tty.port = port
    if tty.isOpen() is True:
        tty.close()


def check_connection(port, supply):
    tty.port = port
    tty.write("*IDN?".encode())
    while tty.inWaiting() is 0:
        ()
    supply_id = tty.readline().decode('utf8', 'ignore')
    if supply_id != POWER_SUPPLY_ID and supply_id != GAUGE_SUPPLY_ID:
        print("Unreconized Power Supply, get ", supply_id, sep="")
        return -1
    else:
        if (supply_id == POWER_SUPPLY_ID and supply == "power" or
                supply_id == GAUGE_SUPPLY_ID and supply == "gauge"):
            return 0
        else:
            print("Wrong Power Supply! ", port, " is ", supply_id)
            return -1


def power_on(port):
    tty.port = port
    tty.write('OUT1'.encode())


def power_on_set(port, voltage):
    VPreSet(port, voltage)
    power_on(port)


def power_off(port):
    tty.port = port
    tty.write('OUT0'.encode())


def power_reboot(port):
    power_off(port)
    time.sleep(1)
    power_on(port)


def PowerStatus(port):
    tty.port = port
    print('Port ', port, ':' + "\n" + 'U =', Vget(port), 'V'
          + "\nI =", Iget(port), 'A')


def power_loop(port, cycles, Ton, Toff):
    tty.port = port
    while cycles > 0:
        power_on(port)
        time.sleep(Ton)
        power_off(port)
        time.sleep(Toff)
        cycles -= 1


def VgetMv(port):
    return Vget(port) * 1000


def Vset(port, voltage):
    tty.port = port
    voltage = round(voltage, 2)
    tty.write(('VSET1:' + str(voltage)).encode())
    vset_read = Vget(port)
    diff = abs(voltage - vset_read)
    if diff > ACCURANCY:
        print('Setting Power supply voltage and VOUT are too different,\
              wanted =', voltage, 'V', 'get =', vset_read, 'V')
        return -1
    return 0


def VPreSet(port, voltage):
    tty.port = port
    voltage = round(voltage, 2)
    tty.write(('VSET1:' + str(voltage)).encode())
    time.sleep(RESPONSE_TIME)
    vset_read = VPreGet(port)
    diff = abs(voltage - vset_read)
    if diff > ACCURANCY:
        print('Setting Power supply voltage and VSET are too different,\
              wanted =', voltage, 'V', 'get =', vset_read, 'V')
        return -1
    return 0


def VsetMv(port, voltage):
    return Vset(port, voltage / 1000)


def Vget(port):
    tty.port = port
    tty.write('VOUT1?'.encode())
    while tty.inWaiting() is 0:
        ()
    vget_read = float(tty.readline())
    return vget_read


def VPreGet(port):
    tty.port = port
    tty.write('VSET1?'.encode())
    while tty.inWaiting() is 0:
        ()
    vget_read = float(tty.readline())
    return vget_read


def Iget(port):
    tty.port = port
    tty.write('IOUT1?'.encode())
    while tty.inWaiting() is 0:
        ()
    iget_read = float(tty.readline())
    return iget_read


def Iset(port, amperage):
    tty.port = port
    tty.write(('ISET1:' + str(amperage)).encode())
    iset_read = Iget(port)
    diff = abs(float(amperage) - float(iset_read))
    if diff > ACCURANCY:
        print('Setting Power supply amperage and ISET are too different:\
              want=', amperage, 'A', 'get =', iset_read, 'A')
        return -1
    return 0
