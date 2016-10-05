#All ideas that I am testing out I place into this file. 
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests 
import csv
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime
from urllib.request import urlopen

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), 'lxml')
print(bsObj.h1)

#### Web Scraping ####



#Site I will be using:
#https://en.wikipedia.org/wiki/Executive_order

# response = requests.get('https://en.wikipedia.org/wiki/Executive_order')
# soup = BeautifulSoup(response.content, 'lxml')
# print(soup.prettify())
# print(soup.find_all('a'))
# print(page.find('table', {'class': 'wikitable sortable'}))
#print(page.select('table.wikitable.sortable'))
#table = soup.select('table.wikitable.sortable')
# print(page.select('tr'))
# print(table)

#43 names 


# orders = pd.read_csv("executive_orders.csv")
#data = pd.read_csv('executive_orders.csv', error_bad_lines=False)

#### WAY ONE 
# executive_orders = pd.read_csv('executive_orders.csv')
# names = []
# orders = []

# count = 0 
# while count <= 43:
#   name = executive_orders.iat[count, 0]
#   order = executive_orders.iat[count, 1]
#   names.append(name)
#   orders.append(order)
#   count += 1

#   fig = plt.figure(dpi=128, figsize=(10,6))
#   plt.plot(names, orders, linewidth=2, c="red")
#   plt.title("Executive Orders By President", fontsize=24)
#   plt.xlabel('President', fontsize=16)
#   fig.autofmt_xdate()
#   plt.ylabel("Executive Orders", fontsize=16)
#   plt.show()

# print(orders)

#### WAY TWO
# executive_orders = pd.read_csv('executive_orders.csv', usecols=["President", "Orders"], index_col=["President"])
# orders = executive_orders[["Orders"]]
# orders.plot(kind='bar', title = "Executive Orders", figsize=(12,8), bottom=0.34)
# plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.34)
# plt.show()







########## PROOF OF CONCEPT ###########

#This function will establish the connection to the Mongo DB, create a DB as well as a collection. 
# def database_setup():
#     print("\033c")
#     client = MongoClient() #Setting up the connection to mongo DB
#     db = client.practice #Creating a practice DB
#     coll = db.test #Creating a winners collection within the practice DB
#     input("Database now set up! Enter to continue! ")
#     enter_data(coll)

# #This function is where the user will inter in data into the data base. 
# def enter_data(coll):
#     print("\033c")
#     info = []

#     name = input("What is your name: ")
#     age = int(input("What is your age: "))

#     new_info = {'name': name, 'age': age}
#     info.append(new_info)
#     coll.insert(info) #Inserting the info dictionary into the collection. 