import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
print "collecting updates from stock server"
socket.connect("tcp://localhost:8888")
scrip_filter = sys.argv[1:] if len(sys.argv) > 1 else ['aple']
for scrip in scrip_filter:
    socket.setsockopt(zmq.SUBSCRIBE, scrip)

while True:
    string = socket.recv()
    print string
