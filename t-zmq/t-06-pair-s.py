#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zmq
import time

p = 5556
c = zmq.Context()
s = c.socket(zmq.PAIR)
s.bind('tcp://*:%d' % p)

while 1:
    #s.send('Server message to client')
    msg = s.recv()
    print msg
    time.sleep(1)
