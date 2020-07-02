import csv
import matplotlib.pyplot as plt

dataX = open('C:/Users/balto/OneDrive/Desktop/AbornSchool/Intro to Python final/dataX.csv')
dataY = open('C:/Users/balto/OneDrive/Desktop/AbornSchool/Intro to Python final/dataY.csv')

dataX = csv.reader(dataX, delimiter = ' ')
dataY = csv.reader(dataY, delimeter = ' ')
X = []
Y = []

for rows in dataX:
    if(len(rows)>0):
        X.append(rows[0])
    