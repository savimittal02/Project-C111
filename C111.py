import csv
import statistics
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import random
import pandas as pd

df = pd.read_csv("medium_data.csv")

def randomSetOfMean(counter):
    dataSet =[]
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

def showFig(meanList):
    df = meanlist
    fig = ff.create_distplot([df], ["temp"], show_hist= False) 
    fig.show()   

def setup():
    meanList = []
    for i in range(0,100):
        setOfMeans = randomSetOfMean(30)
        meanList.append(setOfMeans)
    showFig(meanList)
    

meanList = []
for i in range(0,100):
    setOfMeans = randomSetOfMean(30)
    meanList.append(setOfMeans)

s_std = statistics.stdev(meanlist)
print(s_std)
s_mean = statistics.mean(meanlist)
print(s_mean)

fstds,fstde = s_mean - s_std , s_mean + s_std
sstds,sstde = s_mean - (2*s_std), s_mean + (2*s_std)
tstds,tstde = s_mean - (3*s_std) , s_mean + (3*s_std)

print("fstds,fstde",fstds,fstde)
print("sstds,sstde",sstds,sstde)
print("tstds,tstde",tstds,tstde)

fig = ff.create_distplot([meanlist],["publication"],show_hist= False)

fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines" , name = "mean"))
fig.add_trace(go.Scatter(x = [s_mean,s_mean],y = [0,0.17],mode = "lines" , name = "funSheet"))
fig.add_trace(go.Scatter(x = [sstde,sstde],y = [0,0.17],mode = "lines" , name = "secondstde"))
fig.add_trace(go.Scatter(x = [tstde,tstde],y = [0,0.17],mode = "lines" , name = "thirdstde"))

fig.show()

zScore = (s_mean - mean)/std
print(zScore)

   


    
