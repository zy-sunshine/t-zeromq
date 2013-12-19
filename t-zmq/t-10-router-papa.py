import time
import zmq
import zhelpers

context = zmq.Context()
#client = context.socket(zmq.XREP)
client = context.socket(zmq.DEALER)
client.bind("ipc:///tmp/routing.ipc")

worker = context.socket(zmq.REP)
worker.setsockopt(zmq.IDENTITY, "A")
worker.connect("ipc:///tmp/routing.ipc")

print '---------------011'
#worker.send("")

print '---------------012'
# Wait for sockets to stabilize
time.sleep(0.3)

#client.recv()
client.send("A", zmq.SNDMORE)
client.send("address 3", zmq.SNDMORE)
client.send("address 2", zmq.SNDMORE)
client.send("address 1", zmq.SNDMORE)
client.send("", zmq.SNDMORE)
client.send("This is the workload")

print '---------------01'
# Worker should get just the workload
#poller = zmq.Poller()
#poller.register(worker, zmq.POLLIN)

print '---------------010000'
#socks = dict(poller.poll())
#if socks.get(worker) == zmq.POLLIN:
if 1:
    zhelpers.dump(worker)
print '---------------02'

# We don't play with envelopes in the worker
worker.send("This is the reply")

# Now dump what we got off the XREP socket...
print '---------------03'
zhelpers.dump(client)
print '---------------04'

