"""
Consider a real life situation. Formulate a question and then design a simulation that can help to answer it. Possible situations include:

    Cars lined up at a car wash
    Customers at a grocery store check-out
    Airplanes taking off and landing on a runway
    A bank teller

Be sure to state any assumptions that you make and provide any probabilistic data that must be considered as part of the scenario.
"""

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



# Radix Sorting Machine
def radixSorting(base, num):
    main = Queue()
    sub_bins = [Queue() for i in range(base)]
    int_str = ''
    while num > 0:
        n = num % base
        sub_bins[n].enqueue(n)
        num = num // 10
    for q in sub_bins:
        while q.size() > 0:
            int_str = int_str + str(q.dequeue())
    return int_str

#print radixSorting(10, 9342354)        



# Airplanes landing simulation

# New plane arrives in airspace on average every 10 minutes
# It takes 7 minutes to land the plane before another plance can land
# Planes must wait their turn to land


import random

class Plane(object):
    def __init__(self, num, current_time):
        self.arrive_time = current_time
        self.num = num

    def getArriveTime(self):
        return self.arrive_time

    def getPlaneNum(self):
        return self.num


class Airport(object):
    def __init__(self):
        self.arrivals = Queue()
        self.wait_times = []
        self.plane_count = 1
        self.busy = False
        self.runwayTimer = 1

    def addPlane(self, current_time):
        self.arrivals.enqueue(Plane(self.plane_count, current_time))
        self.plane_count += 1

    def landPlane(self, current_time):
        p = self.arrivals.dequeue()
        self.addWaitTime(current_time, p.getArriveTime())
        self.busy = True

    def addWaitTime(self, current_time, arrive_time):
        self.wait_times.append(current_time - arrive_time)

    def isRunwayBusy(self):
        return self.busy

    def clearRunway(self):
        if self.runwayTimer == 7:
            self.busy = False
            self.runwayTimer = 1
        self.runwayTimer += 1

    def waitingToLand(self):
        return self.arrivals.size()


def randomArrival(arrival_num):
    chance = random.randrange(1,arrival_num+1)
    return chance == 10
        

def airport_simulation(time):
    a = Airport()
    current_time = 0
    while current_time < time:
        current_time += 1
        if randomArrival(10):
            a.addPlane(current_time)
        if a.waitingToLand() > 0:
            if not a.isRunwayBusy():
                a.landPlane(current_time)
            else:
                a.clearRunway()
    return a.wait_times, a.waitingToLand()


def average(num_list):
    return float(sum(num_list)) / len(num_list)

#wait_times, planes_remaining = airport_simulation(10000)
#i = 0
#for time in wait_times:
#    i += 1
#    print "Wait time %d: %d minutes" % (i, time)

#print "%d total planes landed" % len(wait_times)
#print "%d planes remaining" % planes_remaining
#print "Average wait time: %d minutes" % average(wait_times)
    


# Deque Class Implementation
class Deque(object):
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    # Add item to left side of list
    def addFront(self, item):
        self.items.append(item)

    # Add item to RIGHT side of list
    def addRear(self, item):
        self.items = self.items.insert(0,item)

    # Remove and return item on the RIGHT side of list
    def removeFront(self):
        return self.items.pop()

    # Remove and return item on the LEFT side of list
    def removeRear(self):
        return self.items.pop(0)


html_doc = """
<html>
   <head>
      <title>
         Example
      </title>
   </head>

   <body>
      <h1>Hello, world</h1>
   </body>
</html>
"""

# Returns True if string is valid HTML 
def validHTML(html):
    d = Deque()
    i = 0
    # < == 'o'
    # > == 'c'
    # </ == 'e'
    # Add bracket elements to Deque
    while i < len(html):
        if html[i:i+2] == '</':
            print "adding close tag"
            d.addFront('e')
            i += 2
        elif html[i] == '<':
            d.addFront('o')
            i += 1
        elif html[i] == '>':
            d.addFront('c')
            i += 1
        else:
            i += 1

    # Analyze Deque brackets
    open_count = 0
    close_count = 0
    while d.size() > 1:
        next_str = d.removeRear() + d.removeRear()
        print next_str
        if close_count > open_count:
            print "close count greater than open count"
            return False
        elif next_str not in ['oc','ec']:
            print "bracket not valid HTML"
            return False
        elif next_str == 'oc':
            open_count += 1
        elif next_str == 'ec':
            close_count += 1
    print open_count
    print close_count
    return open_count == close_count


#print validHTML(html_doc)



# Returns deque filled with HTML brackets
def extractBrackets(html):
    d = Deque()
    # < == 'o'
    # > == 'c'
    # </ == 'e'
    # Add bracket elements to Deque    
    i = 0
    while i < len(html):
        print i
        if html[i:i+2] == '</':
            d.addRear('e')
            i += 2
        elif html[i] == '<':
            d.addRear('o')
            i += 1
        elif html[i] == '>':
            d.addFront('c')
            i += 1
        else:
            i += 1
    return d

tmp = extractBrackets(html_doc)
while tmp.size() > 1:
    print tmp.removeRear()
    print tmp.removeFront()

#def validHTML2(html):
#    d = extractBrackets(html)
    
