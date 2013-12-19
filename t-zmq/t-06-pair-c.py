#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zmq
import time

p = 5556
c = zmq.Context()
s = c.socket(zmq.PAIR)
s.connect('tcp://127.0.0.1:%d' % p)

while 1:
    #msg = s.recv()
    #print msg
    s.send("Client message to server")
    time.sleep(1)
