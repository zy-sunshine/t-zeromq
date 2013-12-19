import zmq

def main():
    context = zmq.Context(1)

    frontend = context.socket(zmq.XREP)
    frontend.bind("tcp://*:5559")

    backend  = context.socket(zmq.XREQ)
    backend.bind("tcp://*:5560")

    print '------01'
    zmq.device(zmq.QUEUE, frontend, backend)
    print '------02'

    frontend.close()
    backend.close()
    context.term()

if __name__ == "__main__":
     main()
