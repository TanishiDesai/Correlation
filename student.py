import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Marks In Percentage", y="Days Present")
        fig.show()

def getDataSource(data_path):
    marks = []
    attendence = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            attendence.append(float(row["Days Present"]))

    return {"x" : marks, "y": attendence}   

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between students' marks and students' attendence :-  \n--->",correlation[0,1])

def setup():
    data_path  = "data2.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()