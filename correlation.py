import plotly.express as px
import csv
import numpy as np


def getDataSource(data_path):
    marksOfStudents =[]
    daysPresent=[]
    with open(data_path) as csv_file:
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
            marksOfStudents.append(float(row["Roll No"]))
            daysPresent.append(float(row["Days Present"]))
        return {"x":marksOfStudents,"y":daysPresent}
def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation=",correlation[0,1])
def setup():
    data_path = "marksOfStudents.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
setup()
