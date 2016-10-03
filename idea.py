#All ideas that I am testing out I place into this file. 

from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests 

#### Web Scraping ####

#https://en.wikipedia.org/wiki/Executive_order

response = requests.get('https://en.wikipedia.org/wiki/Executive_order')
soup = BeautifulSoup(response.content, 'lxml')
# print(soup.prettify())
# print(soup.find_all('a'))
# print(page.find('table', {'class': 'wikitable sortable'}))
#print(page.select('table.wikitable.sortable'))
#table = soup.select('table.wikitable.sortable')
# print(page.select('tr'))
# print(table)

# print(table.find_all('td'))

#Working on getting the Presidents names 
presidents = []
for tr in soup.find_all('tr')[1:45]:
    tds = tr.find_all('td')
    president = tds[0].text
    presidents.append(president)

print(presidents)


#These lines get the number of executive orders 
# orders = []
# for tr in soup.find_all('tr')[1:45]:
#     tds = tr.find_all('td')
#     order = tds[1].text
#     orders.append(order)

# print(orders)

# links = soup.find_all('a')
# for link in links:
#   if "/wiki/" in link:
#   #print(link.get('href'))
#     print(link.text)









# cols = []
# for tr in table('td').select('td'):
#   link = th.select_one('a')
#   cols.append({'name': link.text, 'href': link.attrs['href']})
#   print(cols)



# coll.insert(nobel_winners) #Inserting the nobel winners dictionary to the collection. 

# res = coll.find({'category':'Physics'})
# print(list(res))


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