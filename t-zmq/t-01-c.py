import zmq

c = zmq.Context()
s = c.socket(zmq.REQ)
s.connect('ipc:///tmp/zmq')
s.send_pyobj('hello')
msg = s.recv_pyobj()
print msg

