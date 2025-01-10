import logging 
from capture_stage import *
from parameters import parameters
from data import data
from fastapi import FastAPI, WebSocket

def main():
    '''
    load state
     
    From state:
     - get the network adapters that will be monitored
     - get the list of IPs that are currently in the buffer for analysis 
      
    '''
    app = FastAPI()


    #get the adapters from database and if there are some returned then we can skip the getting of the paramters via function 
    db = data()

    adapterList = db.getAdapters()
    
    if not adapterList:
        paramObject = parameters()
        paramObject.getParams()
        adapterList = paramObject.adapterList
    #when and where to save the interfaces to the database? 

    @app.get("/")
    def read_root():
        return("hello": "world")
#we are changing up the design. This will be easier, scalable, better
    @app.get("/addInterface") 
    def add_interface():
        


#the above will essentially just return an object of data that we will need to get this party started 
# we can create this loop to just be checking for input, eventually there will be a systemd service that is running
# so all we will need to do is have a command/alias that will gather the input here. 
    while True:
        try:
            logging.info("running")
            capObj = capture()
            capObj.captureStart(adapterList, db)

            command = input()
            match command:
                case "add":
                    continue
                case "list":
                      continue
                case "report":
                    continue
                case "stop":
                    continue



            #this will create a unique list of IP addresses that can be used for the analysis  

        
        except Exception as e:
            logging.error(f"Error occured: {e}")

if __name__ == "__main__":
    main()
