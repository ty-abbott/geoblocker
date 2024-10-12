import logging 
import subprocess 
from network import *
from parameters import parameters
from data import data


def main():
    '''
    load state
     
    From state:
     - get the network adapters that will be monitored
     - get the list of IPs that are currently in the buffer for analysis 
      
    '''
    #get the adapters from database and if there are some returned then we can skip the getting of the paramters via function 
    data = data()

    adapterList = data.getAdapters()
    
    if not adapterList:
        paramObject = parameters()
        paramObject.getParams()
        adapterList = paramObject.adapterList


    


#the above will essentially just return an object of data that we will need to get this party started 
# though I will need to have a check of state so that it doesnt pop every single time the program starts 
    while True:
        try:
            logging.info("running")
            network(adapterList)
            #this will create a unique list of IP addresses that can be used for the analysis  

        
        except Exception as e:
            logging.error(f"Error occured: {e}")

if __name__ == "__main__":
    main()
