import zmq
import random
import time

context = zmq.Context()

sender = context.socket(zmq.PUSH)
#sender.bind("tcp://127.0.0.1:5577")
sender.bind("ipc:///tmp/100-01")
#print "Please Enter when the workers are ready: "
#_ = raw_input()

print "Sending tasks to workers ..."

#sender.send('0')

random.seed()

total_msec = 0
for task_nbr in range(100):
    workload = random.randint(1, 100)
    total_msec += workload
    #sender.send(str(workload))
    work_message = {'num':task_nbr}
    print "------------ %s" % task_nbr
    sender.send_json(work_message)
    print "-----END------- %s" % task_nbr

print "Total expected cost: %s msec" % total_msec

