import numpy as np
from matplotlib import pyplot
import pandas as pd

df = pd.read_csv("electricity19.csv")


a = (sum(df['tau1'])/10000)
b = (sum(df['tau2'])/10000)
c = (sum(df['tau3'])/10000)
d = (sum(df['tau4'])/10000)
e = (sum(df['p2'])/10000)
f = (sum(df['p3'])/10000)
g = (sum(df['p4'])/10000)
h = (sum(df['g1'])/10000)
i = (sum(df['g2'])/10000)
j = (sum(df['g3'])/10000)
k = (sum(df['g4'])/10000)

mean = [a, b, c, d, e, f, g, h, j, k]
#print("The mean for each column in their respected orders" + str(mean))

def original():
    list1 = []
    for i in range(0,10000):
        list1.append(i)
    pyplot.plot(list1, df['tau1'], color='r')
    pyplot.plot(list1, df['tau2'], color='orange')
    pyplot.plot(list1, df['tau3'], color='gold')
    pyplot.plot(list1, df['tau4'], color='yellow')
    pyplot.plot(list1, df['p2'], color='green')
    pyplot.plot(list1, df['p3'], color='turquoise')
    pyplot.plot(list1, df['p4'], color='blue')
    pyplot.plot(list1, df['g1'], color='darkviolet')
    pyplot.plot(list1, df['g2'], color='purple')
    pyplot.plot(list1, df['g3'], color='magenta')
    pyplot.plot(list1, df['g4'], color='pink')
    pyplot.xlabel('Day')
    pyplot.ylabel('Electricity')
    pyplot.title('Electricity19.csv')
    pyplot.show()


#print(dataframe.info())

def sum_of_lists():
    df = pd.read_csv("electricity19.csv")

    a = df['tau1'].sum()
    b = df['tau2'].sum()
    c = df['tau3'].sum()
    d = df['tau4'].sum()
    e = df['p2'].sum()
    f = df['p3'].sum()
    g = df['p4'].sum()
    h = df['g1'].sum()
    i = df['g2'].sum()
    j = df['g3'].sum()
    k = df['g4'].sum()

    sum = [a, b, c, d, e, f, g, h, i, j, k]
    labels = ['tau1', 'tau2', 'tau3', 'tau4', 'p2', 'p3', 'p4', 'g1', 'g2', 'g3', 'g4']
    colors = ['r', 'orange', 'gold', 'yellow', 'green', 'turquoise', 'darkviolet', 'purple', 'magenta', 'pink']
    pyplot.bar(labels, sum, color=colors)
    pyplot.title('Sum of Electricity')
    pyplot.show()


def stable_or_unstable():
    df = pd.read_csv("electricity19.csv")
    stable = (df['stabf'].value_counts()['stable'])
    unstable = (df['stabf'].value_counts()['unstable'])

    c = [stable, unstable]

    labels = ['Stable Count', 'Unstable Count']
    pyplot.bar(labels, c, color=['red', 'blue'])
    pyplot.show()


def highest_value():
    df = pd.read_csv("electricity19.csv")
    a = []

    for i in range(len(df['stabf'])):
        print(df.iloc[i:1])
        #if df.iloc[i:1] > df.iloc[(i-1):1]:
            #a.append(df.iloc[i:1])


    #a2 = a[len(a)]
    #print(a2)
highest_value()