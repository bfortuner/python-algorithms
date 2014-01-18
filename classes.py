#### Python OOP Review ####

from __future__ import division




# Return greatest common denominator of two numbers (the largest number that can be divided evenly into each)
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n
        

# Fraction class
class Fraction(object):
    # Construtor which tells what data we need to create an object
    def __init__(self, top, bottom):
        # Self is a formal parameter that is used to reference the object
        # Self must always be the first parameter in Class methods + attributes
        self.num = top
        self.den = bottom

    # Returns a string representation of the object
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # Override default add method in Python
    def __add__(self, otherfraction):
        new_den = self.den * otherfraction.den
        new_num = (self.num * otherfraction.den) + (otherfraction.num * self.den)
        return Fraction(new_num, new_den).lowestTerms()

    # Override default subtraction method in Python
    def __sub__(self,otherfraction):
        new_den = self.den * otherfraction.den
        new_num = (self.num * otherfraction.den) - (otherfraction.num * self.den)
        common = gcd(new_num,new_den)
        return Fraction(new_num//common, new_den//common)


    def __truediv__(self,otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    
    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common, newden//common)

    # Reduce fraction to lowest terms
    def lowestTerms(self):
        i = 1
        GCD = 1
        while i < min(self.num,self.den):
            if self.num % i == 0 and self.den % i == 0:
                GCD = i
            i += 1
        return Fraction(self.num / GCD, self.den / GCD)

    def __eq__(self,otherfraction):
        first_num = self.num * otherfraction.den
        second_num = otherfraction.num * self.den
        return first_num == second_num

    

f1 = Fraction(3,6)
f2 = Fraction(2,4)
#print f1 + f2
#print f1 - f2
#print f1 * f2
print f1 / f2

# Python multiplication function
def multiply(a,b):
    sum = 0
    i = 0
    while i < b:
        sum += a
        i += 1
    return sum

#print multiply(5,6) 


def division(num,den):
    count = 0
    while num * count < den:
        count += 1
    if num * count > den:
        return count - 1
    return count


#print division(4,21)


def subtraction(a,b):
    count = 0
    if b < a:
        while b < a:
            count += 1
            b += 1
        return count
    else:
        while a < b:
            count += 1
            a += 1
        return int('-'+str(count))


#print subtraction(30,12)
#print subtraction(30,32)


# Parent class of a digital circuit
class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    # Calls a function here only defined by its Child classes
    def getOutput(self):
        # Writing a method that does not exist yet
        self.output = self.performGateLogic()
        return self.output
        

# Child class of LogicGate that holds AND and OR classes
class BinaryGate(LogicGate):
    def __init__(self, n):
        # Instantiate relationship with Parent Class
        LogicGate.__init__(self,n)

        # Instantiate child-only attributes
        self.pinA = None
        self.pinB = None

    # Ask user to provide label for each Pin (1 or 0)
    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


# Child class of BinaryGate that holds AND gate
class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
        
    def performGateLogic(self):
        # You can call functions from the parent class directly
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

# Child class of Binary Gate that holds OR gate
class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0
    
#ag = AndGate("A1")
#og = OrGate("O1")
#print ag.getOutput()
#print og.getOutput()


# Child class of LogicGate that holds NOT class
class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

    

# Child class of UnaryGate that holds NOT class
class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)
    
    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

#ng = NotGate("N1")
#print ng.performGateLogic(ag.getOutput())




# Connector class to connect two Gates
# HAS-A relationship with LogicGate
class Connector:
    def __init__(self, fgate, tgate):
        # Requires two Gate instances
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


 

'''
g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1,g3)
c2 = Connector(g2,g3)
c3 = Connector(g3,g4)

print g4.getOutput()
'''
