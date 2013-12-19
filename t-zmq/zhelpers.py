from random import randint
import binascii
import os

import zmq

if not hasattr(zmq, 'ROUTER'):
    zmq.ROUTER = zmq.XREP
if not hasattr(zmq, 'DEALER'):
    zmq.DEALER = zmq.XREQ

# Receives all message parts from socket, prints neatly
def dump(msg_or_socket):
    if isinstance(msg_or_socket, zmq.Socket):
        return dump(msg_or_socket.recv_multipart())
    else:
        msg = msg_or_socket
    print "----------------------------------------"
    for part in msg:
         print "[%03d]" % len(part),
         if all(31 < ord(c) < 128 for c in part):
             print '[TEXT]',
             print part
         else:
             print '[BIN]',
             print "".join("%x" % ord(c) for c in part)


# Set simple random printable identity on socket
def set_id(zsocket):
    identity = "%04x-%04x" % (randint(0, 0x10000), randint(0, 0x10000))

    zsocket.setsockopt(zmq.IDENTITY, identity)
    return identity

