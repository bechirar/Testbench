#!/usr/bin/python3
# -*- coding: utf-8 -*-

from threading import Thread
from wifi import Cell, Scheme
from wireless import Wireless
import wifi
import iperf3
import logging
import socket
import os
import sys
import datetime
import time
import iperf3

def Search():
    wifilist = []
    cells = wifi.Cell.all('wlp2s0b1')
    for cell in cells:
        wifilist.append(cell)
    return wifilist

def FindFromSearchList():
    ssid ='UnistellarBench'
    wifilist = Search()
    for cell in wifilist:
        if cell.ssid == ssid:
            return ("Successfully find ssid" ,{cell.ssid})
    return False

def connect():
    x = ' '
    ssid1 = 'UnistellarBench'
    password1 = ' '
    wireless = Wireless()
    x = wireless.connect(ssid=ssid1, password=password1)
    return x

def ping():
    #hostname = "192.168.220.1"
    hostname = "google.fr"
    if os.system("ping -c1 " + hostname):
        return False
    else:
        return True
 

def RunningClient():
    client = iperf3.Client()
    client.duration = 1
    client.server_hostname = '192.168.0.185'
    client.port = 5201

    print('Connecting to {0}:{1}'.format(client.server_hostname, client.port))
    result = client.run() 
    
    if result.error:
        #print(result.error)
        return False

    else:
        print('')
        print('Test bandwidth completed:')
        print('  started at         {0}'.format(result.time))
        print('  bytes transmitted  {0}'.format(result.sent_bytes))
        print('  retransmits        {0}'.format(result.retransmits))
        print('  avg cpu load       {0}%\n'.format(result.local_cpu_total))
        print('Average transmitted data in all sorts of networky formats:')
        print('  bits per second      (bps)   {0}'.format(result.sent_bps))
        print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
        return True
    
def main():

    print (Search())
    print (FindFromSearchList())
    print (connect())
    print (ping())
    print (RunningClient())

if __name__ == "__main__":
    main()

logging.basicConfig(filename='Test_Wifi.log',level=logging.DEBUG,\
      format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')
logging.info('Start of the program ...!')
if Search () == ' ':
    logging.error('Interface doesnt support scanning')
else:
    logging.info('Display the list of SSID')
if FindFromSearchList() == False:
    logging.warning('The network does not exist')
else:
    logging.info('The network exist')
if connect() == True:
    logging.warning('Your are connected to the network')
else:
    logging.error('Error accessing this network')
'''
if RunningClient() == False:
    logging.error('Error Test BandWidh')
else: 
    logging.info('Test bandwidh completed')'''
'''if ping() == False:
    logging.error('Error Ping to Raspberry')'''
logging.info('End of the program.')
    






