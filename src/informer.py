from threading import Lock

'''
    here is where we will do the actual threat intelligence:
1. seeing if the IP is already in our data 
2. seeing how many times the IP has reached out to our server and on which ports(eventually)
3. its going to essentially do all the data fleshing out parts

we are going to need an object that holds our dictionaries and data structures 
with lock: 
- this ^^ would work better instead for mutex. It ensures that locks are lifted

'''
lock = Lock()
def checker(ip, stateObj):
    with lock:
        isThere = stateObj.getIP(ip)
        if isThere == True:
            return 
        else: 
            return
    #logging should be updated here
    return
#TODO - basically figure out the do stuff and test that this works
