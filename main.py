#This is the main file where the heart of my program will reside. 
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests 

#Goals: 
    #Build a connection to mongo DB -DONE 
    #Find site to scrape information off of -Done
    #Enter information in DB 
    #Pull information from DB and build a graph from the information 
    

#This function greets the user and starts the entire program.
def main():
    print("\033c")
    print("---------------------------")
    print("Welcome to Py Mongo Project")
    print("---------------------------")
    input("Press Enter to continue ")
    database_setup()

#This function will establish the connection to the Mongo DB, create a DB as well as a collection. 
def database_setup():
    print("\033c")
    client = MongoClient() #Setting up the connection to mongo DB
    db = client.executive_orders #Creating a practice DB
    coll = db.orders #Creating a winners collection within the practice DB
    input("Database now set up! Enter to continue! ")
    scrape_data(coll)

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
        orders = {'President': name, 'Orders': order}
        executive_orders.append(orders)
    coll.insert(executive_orders) #Inserting the executive orders dictionary into the collection.




main()