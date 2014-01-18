#### Queues ####



# Queue class implementation
class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# Queue class implementation - Rear of Queue at end of List
class QueueRear(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)



# Python timit module                                                                                                            
from timeit import *

q1 = Queue()
q2 = QueueRear()
def q1_enqueue():
    q1.enqueue('hey')
    q1.enqueue(3)
    q1.enqueue(True)

def q2_enqueue():
    q2.enqueue('hey')
    q2.enqueue(3)
    q2.enqueue(True)

def q1_dequeue():
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()

def q2_dequeue():
    q2.dequeue()
    q2.dequeue()
    q2.dequeue()
    

t1 = Timer("q1_enqueue()", "from __main__ import q1_enqueue")
print ("q1 enqueue:",t1.timeit(number=1000), "milliseconds")                                                                        

t2 = Timer("q2_enqueue()", "from __main__ import q2_enqueue")
print("q2 enqueue",t2.timeit(number=1000), "milliseconds")                                                                          

t3 = Timer("q1_dequeue()", "from __main__ import q1_dequeue")
print("q1 dequeue",t3.timeit(number=1000), "milliseconds")                                                                          

t4 = Timer("q2_dequeue()", "from __main__ import q2_dequeue")
print("q2 dequeue",t4.timeit(number=1000), "milliseconds")                                                                          


def test_dict_del(l, num):
    rand_index = random.randrange(num)
    #del x[rand_index]                                                                                                               


# Compare del with list vs dict                                                                                                
"""                                                                                                                          
for i in range(1000,1000000,20000):                                                                                           
    x_list = list(range(i))                                                                                                   
    list_t = Timer("test_list_del(%s, %d)" % (x_list, i),"from __main__ import random, x_list, test_list_del")                
    list_time = list_t.timeit(number=1000)                                                                                    
    x_dict = {j:None for j in range(i)}                                                                                      
    dict_t = Timer("test_dict_del(%s, %d)" % (x_dict, i),"from __main__ import random, x_dict, test_dict_del")                  
    dict_time = dict_t.timeit(number=1000)                                                                                      
    print "i: %d, list: %.9f, dict: %.9f" % (i, list_time, dict_time)                                                             
"""


# Hot Potato Simulation
def hot_potato_sim(num, people):
    circle = Queue()
    for person in people:
        print "Added new person to circle: %s" % person
        circle.enqueue(person)
    print "Circle size: %d" % circle.size()

    while circle.size() > 1:
        i = 1
        while i < num:
            print i
            p = circle.dequeue()
            circle.enqueue(p)
            i += 1
        removed = circle.dequeue()
        print removed
    winner = circle.dequeue()
    print "Winner is %s" % winner
    return winner
    
import random
#print hot_potato_sim(random.randrange(10),['brendan','colin','liam','mom','dad'])




# Printer Queue Simulation
class Task(object):
    def __init__(self, creationTime):
        self.pages = random.randrange(1,20)
        self.creationTime = creationTime



class Printer(object):
    def __init__(self, seconds_per_page):
        self.is_busy = False
        self.time_required = 0
        self.seconds_per_page = seconds_per_page

    def isBusy(self):
        return self.is_busy

    def continuePrinting(self):
        self.time_required -= 1
        if self.time_required == 0:
            self.is_busy = False



class PrintQueue(object):
    def __init__(self):
        self.jobs = Queue()
        self.waiting_times = []
        
    def add_job(self, job):
        self.jobs.enqueue(job)
        
    def remove_job(self, currentTime):
        job = self.jobs.dequeue()
        self.add_waiting_time(job.creationTime, currentTime) 
        return job

    def add_waiting_time(self, creationTime, currentTime):
        self.waiting_times.append(currentTime - creationTime)

    def getSize(self):
        return self.jobs.size()


def average(num_list):
    return sum(num_list) / float(len(num_list))


def simulation(runtime_seconds, printer, print_queue, seconds_per_task):
    for current_second in range(1, runtime_seconds + 1):
        chance = random.randrange(seconds_per_task + 1)
        if chance == 180:
            new_task = Task(current_second)
            print_queue.add_job(new_task)
        elif (not printer.isBusy()) and (print_queue.getSize() > 0):
            job = print_queue.remove_job(current_second)
            printer.is_busy = True
            printer.time_required = job.pages * printer.seconds_per_page
        elif printer.isBusy():
            printer.continuePrinting()
        else:
            pass
    return average(print_queue.waiting_times), print_queue.getSize()


'''
for i in range(10):
    sim_results = simulation(3600, Printer(12), PrintQueue(), 180)
    print "Average Wait %6.2f seconds %3d tasks remaining" % (sim_results[0], sim_results[1])
'''

def run_simulation(num_times):
    avg_waiting_times = []
    for i in range(num_times):
        avg_time = "Average Wait %6.2f: %3d seconds" % (i, simulation(3600, Printer(6), PrintQueue(), 180))
        avg_waiting_times.append(avg_time)
    

#run_simulation(10)

