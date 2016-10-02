#This is the main file where the heart of my program will reside. 
from pymongo import MongoClient

#Goals: 
    #Build a connection to mongo DB
    #Find site to scrape information off of
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
    db = client.practice #Creating a practice DB
    coll = db.test #Creating a winners collection within the practice DB
    input("Database now set up! Enter to continue! ")
    enter_data(coll)





main()