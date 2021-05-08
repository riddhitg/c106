import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Size of TV", y = "Average time")
        fig.show()

def getDataSource(data_path):
    size_of_tv = []
    average_time = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            average_time.append(float(row["Average time"]))
    return {"x":size_of_tv,"y":average_time}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("corelation between size of tv V/S average time is ",corelation[0,1])

def setup ():
    data_path = "Sizetv.csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)
    plotFigure(data_path)

setup()