import zmq

c = zmq.Context()
s = c.socket(zmq.REP)
s.bind('ipc:///tmp/zmq')

while True:
    msg = s.recv_pyobj()
    s.send_pyobj(msg)

s.close()
