#This is the main file where the heart of my program will reside. 
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests 
import csv
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from valid import *

#Goals: 
    #Build a connection to mongo DB -DONE 
    #Find site to scrape information off of -DONE
    #Enter information in DB -DONE
    #I need to convert the orders format from string to int. 
    #Pull information from DB and build a graph from the information 
    

#This function greets the user and starts the entire program.
def main():
    print("\033c")
    print("---------------------------")
    print("Welcome to Py Mongo Project")
    print("---------------------------")
    input("Press Enter to continue ")
    options_menu()

#This function is where the user will choose to look at a graph of the data or use Mongo DB to search through 
#the data.
def options_menu():
    print("\033c")
    print("1. Look at a graph of the data.")
    print("2. Search through the data")
    choice = int(input("What is your option? "))
    while not options_menu_Valid(choice):
        print("That was not a correct selection!")
        choice = int(input("What is your option? "))
    if choice == 1:
        plotting_data()
    elif choice == 2:
        database_setup()

#This function will establish the connection to the Mongo DB, create a DB as well as a collection. 
def database_setup():
    print("\033c")
    #client = MongoClient() #Setting up the connection to mongo DB
    #db = client.executive_orders #Creating a practice DB
    #coll = db.orders #Creating a winners collection within the practice DB
    coll = "Mike"
    input("Database now set up! Enter to continue! ")
    scrape_data(coll)

#This function will go out to the wikipedia site, pull the data and place it into the mongo DB. Since this will really
#only need to happen once, then this function is not 100% critical to the program. I leave it here for the simple
#reason that I want to see how I did this in future projects as well as let others see.
def scrape_data(coll):
    print("\033c")
    response = requests.get('https://en.wikipedia.org/wiki/Executive_order')
    soup = BeautifulSoup(response.content, 'lxml')
    executive_orders = []
    #This for loop will find the data that I need and pull it into the mongo DB.
    for tr in soup.find_all('tr')[1:45]:
        tds = tr.find_all('td')
        name = tds[0].text
        order = tds[1].text
        order = int(order.replace(',', ''))
        orders = {'President': name, 'Orders': order}
        executive_orders.append(orders)
    #coll.insert(executive_orders) #Inserting the executive orders dictionary into the collection.
    input('Data entered into data base! Hit enter to continue') 
    create_csv(executive_orders)

#This function will take my dictionary and create a CSV out of it. I want to have my data placed both into a CSV 
#as well as the db so that I get more practice using both. 
def create_csv(executive_orders):
    print("\033c")
    f = open('executive_orders.csv', 'w')
    #This line gets the data columns from the keys of the dictionary.
    cols = executive_orders[0].keys()
    #The with statement guarantees that the file is closed upon going through the dictionary. 
    with open('executive_orders.csv', 'w') as f:
        #joins the columns with a , 
        f.write(','.join(cols) + '\n')
        #Creates a list using the column keys to the objects in the dictionary. 
        for o in executive_orders:
            row = [str(o[col]) for col in cols]
            f.write(','.join(row)+ '\n')
    input("CSV Created! Hit Enter to continue!")
    see_results()

def plotting_data():
    print("\033c")
    executive_orders = pd.read_csv('executive_orders.csv')
    print(executive_orders)






main()