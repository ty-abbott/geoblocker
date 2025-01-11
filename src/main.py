import logging 
from capture_stage import *
from parameters import parameters
from data import data
from fastapi import FastAPI, WebSocket



app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
        
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.get("/")
def read_root():
    return("hello": "world")
#we are changing up the design. This will be easier, scalable, better
@app.get("/addInterface") 
def add_interface():
        
@app.WebSocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.recieve_text()
            #do checks and store data 
            #have a check here to see if we should keep recieving or if we need to do a stop for state reasons(report, whatever else)
            if stop == True:
                manager.broadcast("Stop") #the magic word 
                #either on the client side have a timed stop or shut down the endpoint??
    except WebSocketDisconnect:
        #log that it had been disconnect
        #wait for reconnect? 


def main():
    '''
    load state
     
    From state:
     - get the network adapters that will be monitored
     - get the list of IPs that are currently in the buffer for analysis 
      
    '''


    #get the adapters from database and if there are some returned then we can skip the getting of the paramters via function 
    db = data()

    adapterList = db.getAdapters()
    
    if not adapterList:
        paramObject = parameters()
        paramObject.getParams()
        adapterList = paramObject.adapterList
    #when and where to save the interfaces to the database? 

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
