from data.py import *

'''
    here is where we will do the actual threat intelligence:
1. seeing if the IP is already in our data 
2. seeing how many times the IP has reached out to our server and on which ports(eventually)
3. its going to essentially do all the data fleshing out parts

we are going to need an object that holds our dictionaries and data structures 
race conditions need to be avoided with data object. The best way to do this would be through a queue or through locks with threading library 

'''


