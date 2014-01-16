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

wait_times, planes_remaining = airport_simulation(10000)
i = 0
#for time in wait_times:
#    i += 1
#    print "Wait time %d: %d minutes" % (i, time)

print "%d total planes landed" % len(wait_times)
print "%d planes remaining" % planes_remaining
print "Average wait time: %d minutes" % average(wait_times)
    
