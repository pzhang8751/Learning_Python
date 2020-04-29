from matplotlib import pyplot
from random import seed
from random import randint
from numpy import sin
from numpy.random import seed
from numpy.random import randn
import math

def lineplot():
    x = [x*0.1 for x in range(100)]
    y = sin(x)
    pyplot.plot(x, y)
    pyplot.show()

def bargraph():
    seed(1)
    x = ['red', 'green', 'blue']
    y = [randint(0, 100), randint(0, 100), randint(0, 100)]
    pyplot.bar(x,y)
    pyplot.show()

def histogram():
    seed(2)
    x = randn(1000)
    pyplot.hist(x, bins=200)
    pyplot.show()



def bargraph2():
    seed(1)
    list1 = []
    list2 = []
    for i in range(1,500):
        if (math.sqrt(i)).is_integer() == True:
            list1.append(i)

    for x in range(len(list1)):
        list2.append(x)

    pyplot.bar(list1,list2)
    pyplot.show()

def bargraph3():
    seed(1)
    x = ['apple', 'orange', 'banana', 'kiwi', 'blueberry', 'grapes']
    y = [35, 30, 10, 25, 40, 5]
    pyplot.bar(x,y, color=['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
    pyplot.show()

    pyplot.barh(x,y, color=['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
    pyplot.yticks(x)
    pyplot.show()

    print('The most eaten fruit is ' + x[y.index(max(y))] + ' at ' + str(max(y)) + ' people.')

    z = (sum(y))/(len(y))

    print('The average amount of fruit eaten is ' + str(z))


bargraph3()