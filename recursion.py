#### Recursion ####



# Iterative sum
def iterativeSum(l):
    total = 0
    for e in l:
        total += e
    return total


# Recursive sum
def recursiveSum(l):
    if len(l) == 1:
        return l[0]
    return l[0] + recursiveSum(l[1:])

 


#l1 = [1,2,3,4,5]
#print iterativeSum(l1)
#print recursiveSum(l1)


# Recursive Factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)



# Recursive Int to Str of any Base
def intToStr(base, n):
    basestr = '0123456789ABCDEF'
    if n < base:
        return basestr[n]
    else:
        return intToStr(base, n/base) + basestr[n % base]


#print intToStr(2, 1453)
 

# Recursive reverse a string
def reverseStr(s):
    if len(s) == 1:
        return s[0]
    else:
        return reverseStr(s[1:]) + s[0]



def isPalindrome(s):
    return s == reverseStr(s)


# Reverse String Using Stack Frame
from stacks import Stack

def stackRevStr(s, stack):
    if len(s) == 0:
        return ''
    elif len(s) == 1:
        result = s
        while not stack.isEmpty():
            result += stack.pop()
        return result
    else:
        stack.push(s[0])
        return stackRevStr(s[1:], stack)

#s1 = Stack()
#print stackRevStr('h',s1)



### Visualizing Recursion ###


import turtle

#myTurtle = turtle.Turtle()
#myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

#drawSpiral(myTurtle,100)
#myWin.exitonclick()




# Fractal Tree Visualization

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

#main()



# Sierpinski Triangle

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()

#main()
from turtle import *

# Exploring a Maze

class Maze:
    def __init__(self,mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName,'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = Turtle(shape='turtle')
        setup(width=600,height=600)
        setworldcoordinates(-(columnsInMaze-1)/2-.5,
                            -(rowsInMaze-1)/2-.5,
                            (columnsInMaze-1)/2+.5,
                            (rowsInMaze-1)/2+.5)

    def drawMaze(self):
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x+self.xTranslate,
                                         -y+self.yTranslate,
                                         'tan')
        self.t.color('black','blue')

    def drawCenteredBox(self,x,y,color):
        tracer(0)
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color('black',color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        update()
        tracer(1)

    def moveTurtle(self,x,y):
        self.t.up()
        self.t.setheading(self.t.towards(x+self.xTranslate,
                                         -y+self.yTranslate))
        self.t.goto(x+self.xTranslate,-y+self.yTranslate)

    def dropBreadcrumb(self,color):
        self.t.dot(color)

    def updatePosition(self,row,col,val=None):
        if val:
            self.mazelist[row][col] = val
        self.moveTurtle(col,row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    def isExit(self,row,col):
         return (row == 0 or
                 row == self.rowsInMaze-1 or
                 col == 0 or
                 col == self.columnsInMaze-1 )

    def __getitem__(self,idx):
         return self.mazelist[idx]



#m = Maze("maze.txt")
#m.drawMaze()





# Greedy Optimization - Make Change w Fewest Coins
def changeCoins(change, coin_list):
    sorted_coins = sorted(coin_list, reverse=True)
    required_coins = dict((coin,0) for coin in sorted_coins)
    i = 0
    while change > 0:
        coin = sorted_coins[i]
        if change - coin >= 0:
            required_coins[coin] += 1
            change -= coin
        else:
            i += 1
    return required_coins


#print changeCoins(67, [25,1,5,10])


# Naive Recursive Solution - Super slow!
def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

#print(recMC([1,5,10,25],63))


# Dynamic Programming Solution - Fast!
def dpMakeChange(coinValueList,change,minCoins):
   for cents in range(change+1):
      coinCount = cents
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
      minCoins[cents] = coinCount
   return minCoins[change]


