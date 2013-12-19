import threading
import zmq

def step1(context):
    print "In step1"
    sender = context.socket(zmq.PAIR)
    sender.connect("inproc://step2")
    sender.send("")

def step2(context):
    receiver = context.socket(zmq.PAIR)
    receiver.bind("inproc://step2")

    thread = threading.Thread(target=step1, args=(context, ))
    thread.start()

    string = receiver.recv()

    print "In step2"
    sender = context.socket(zmq.PAIR)
    sender.connect("inproc://step3")
    sender.send("")

    return

def main():
    context = zmq.Context(1)

    receiver = context.socket(zmq.PAIR)
    receiver.bind("inproc://step3")

    thread = threading.Thread(target=step2, args=(context, ))
    thread.start()

    string = receiver.recv()
    print "In step3"

    print("Test successful!\n")

    receiver.close()
    context.term()

    return

if __name__ == "__main__":
    main()

