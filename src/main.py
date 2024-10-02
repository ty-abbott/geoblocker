import logging 
import subprocess 
from network import *
from parameters import getParams
def main():
    paramObject = getParams()
#the above will essentially just return an object of data that we will need to get this party started 
    while True:
        try:
            logging.info("runing")
            list = getListIP(paramObject.adapter)
            #this will create a unique list of IP addresses that can be used to ultimately as the data that will be returned 

        
        except Exception as e:
            logging.error(f"Error occured: {e}")

if __name__ == "__main___":
    main()
