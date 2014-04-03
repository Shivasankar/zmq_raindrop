import sys
import time
import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:8888")
script = ['aple', 'goog', 'msft', 'mzam']
while True:
    scrip = random.choice(script)
    price = random.randrange(70,700)
    msg = "%s:%s" %(scrip,price)
    print msg
    socket.send(msg)
    time.sleep(0.5)
