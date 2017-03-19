#!/bin/sh

'''
Kuemmerlng Clock 

Run this script to start the clock. 

Programmed by Sebastian Thiems

Februar 2017
'''
from clock import Clock
import time

from udpserver import UdpServer

'''
Start the drawing.
'''
clock = Clock()
clock.clear()
time.sleep(2)
clock.nextMode()

'''
Start the upd server.
'''
udpServer = UdpServer(clock)
udpServer.run()
