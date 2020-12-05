import plotly.figure_factory as ff 
import csv
import plotly.graph_objects as go 
import statistics
import random 
import pandas as pd 

df=pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()
datamean = statistics.mean(data)
datastd = statistics.stdev(data)
#fig = ff.create_distplot([data],["Math_score"],show_hist=False)
#fig.show()

def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
for i in range(0,1000):
    setofmeans = randomsetofmean(100)
    mean_list.append(setofmeans)
standarddeviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("std: ", standarddeviation)
print("standard deviation of data is: ", datastd)
print("mean of the data is:", datamean)
print("mean: ", mean)

marks1stdstart,marks1stdend = mean-standarddeviation,mean+standarddeviation
marks2stdstart,marks2stdend = mean-(2*standarddeviation),mean+(2*standarddeviation)
marks3stdstart,marks3stdend = mean-(3*standarddeviation),mean+(3*standarddeviation)
fig = ff.create_distplot([mean_list],["Student_marks"],show_hist=False)


fig.add_trace(go.Scatter(x=[mean,mean],y=[0 , 0.17],mode="lines",name="means"))

fig.add_trace(go.Scatter(x=[marks1stdstart,marks1stdstart],y=[0 , 0.17],mode="lines",name="1ststdstart"))

fig.add_trace(go.Scatter(x=[marks2stdstart,marks2stdstart],y=[0 , 0.17],mode="lines",name="2stdstart"))

fig.add_trace(go.Scatter(x=[marks3stdstart,marks3stdstart],y=[0 , 0.17],mode="lines",name="3stdstart"))

fig.add_trace(go.Scatter(x=[marks1stdend,marks1stdend],y=[0 , 0.17],mode="lines",name="1stdend"))

fig.add_trace(go.Scatter(x=[marks2stdend,marks2stdend],y=[0 , 0.17],mode="lines",name="2stdend"))

fig.add_trace(go.Scatter(x=[marks3stdend,marks3stdend],y=[0 , 0.17],mode="lines",name="3stdend"))


df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
print("mean of sample3:- ",mean_of_sample3)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT FUNSHEETS"))
fig.add_trace(go.Scatter(x=[marks2stdend, marks2stdend], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[marks3stdend, marks3stdend], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()
zscore = (mean_of_sample3-mean)/standarddeviation
print("Z score: ", zscore)