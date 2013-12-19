import time
import threading
import zmq

def worker_routine(worker_url, context):

    socket = context.socket(zmq.REP)

    socket.connect(worker_url)

    while True:
        string  = socket.recv()
        print("Received request: [%s]\n" % (string))
        time.sleep(1)

        socket.send("World")

def main():
    url_worker = "inproc://workers"
    url_client = "tcp://*:5555"

    context = zmq.Context(1)

    clients = context.socket(zmq.XREP)
    clients.bind(url_client)

    workers = context.socket(zmq.XREQ)
    workers.bind(url_worker)

    for i in range(5):
        thread = threading.Thread(target=worker_routine, args=(url_worker, context, ))
        thread.start()

    print 'Running...'
    zmq.device(zmq.QUEUE, clients, workers)
    print 'Stoping...'

    clients.close()
    workers.close()
    context.term()

if __name__ == "__main__":
    main()

