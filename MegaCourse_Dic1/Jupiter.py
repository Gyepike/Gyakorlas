import os
import pandas
print(os.listdir())

#df = pandas.read_csv("supermarkets.csv")
#df = pandas.read_json("supermarkets.json")
#df = pandas.read_excel("supermarkets.xlsx")
#df = pandas.read_csv("supermarkets-commas.txt",sep=",")
df = pandas.read_csv("supermarkets-semi-colons.txt",sep=";", header=None)
#df = pandas.read_json("http://pythonhow.com/supermarkets.json")
#df.columns = ["Alma","korte","dinnye","eper","málna","szolo","citrom"]
print(df)
print(df.sum( "szolo"))