'''
Kuemmerlng Clock 

Run this script to start the clock. 

Programmed by Sebastian Thiems

Februar 2017
'''
from clock import Clock
import time

from udpserver import UdpServer

clock = Clock()
clock.clear()

time.sleep(2)

clock.nextMode()

udpServer = UdpServer(clock)
udpServer.run()
