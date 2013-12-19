import sys
import time
import zmq
import random

context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
#receiver.connect("tcp://127.0.0.1:5557")
receiver.connect("ipc:///tmp/100-01")

# Socket to send messages to
sender = context.socket(zmq.PUSH)
#sender.connect("tcp://127.0.0.1:5558")
sender.connect("ipc:///tmp/100-02")

poller = zmq.Poller()
poller.register(receiver, zmq.POLLIN)

# Process tasks forever
consumer_id = random.randrange(1, 10005)
while True:
    print 'Start recive on'
    #socks = dict(poller.poll())
    print '--'
    #print socks
    #if socks.get(receiver) == zmq.POLLIN:
    if 1:
        s = receiver.recv_json()
        data = s['num']
        print data
        # Simple progress indicator for the viewer
        sys.stdout.write('.')
        sys.stdout.flush()

        # Do the work
        time.sleep(int(data)*0.001)

        # Send results to sink
        result = {'consumer': consumer_id, 'num': data}
        sender.send_json(result)

