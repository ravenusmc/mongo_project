#All ideas that I am testing out I place into this file. 

from pymongo import MongoClient

#This is the dictionary of nobel winners.
nobel_winners = [
  {
    'category': 'Physics',
    'name': 'Albert Einstein',
    'nationality': 'Swiss',
    'sex': 'male',
    'year': 1921
  },
  {
    'category': 'Physics',
    'name': 'Paul Dirac',
    'nationality': 'British',
    'sex': 'male',
    'year': 1921
  },
  {
    'category': 'Chemistry',
    'name': 'Marie Curie',
    'nationality': 'Polish',
    'sex': 'female',
    'year': 1921
  },
]


client = MongoClient() #Setting up the connection to mongo DB
db = client.nobel_prize #Creating a nobel_prize DB
coll = db.winners #Creating a winners collection within the nobel_prize DB

# coll.insert(nobel_winners) #Inserting the nobel winners dictionary to the collection. 

# res = coll.find({'category':'Physics'})
# print(list(res))

#Make a program that has a dictionary, add dictionary to the data base. 


info = []

name = input("What is your name: ")
age = int(input("What is your age: "))

new_info = {'name': name, 'age': age}
info.append(new_info)

print(info)