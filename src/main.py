import logging 
from capture_stage import *
from parameters import parameters
from data import data
from fastapi import FastAPI, WebSocket

stop = False

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
db = data()

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
            print("here we are")
            print(data)#do checks and store data 
            #have a check here to see if we should keep recieving or if we need to do a stop for state reasons(report, whatever else)
            if stop == True:
                manager.broadcast("Stop") #the magic word 
                print("this should be stopping")
                #either on the client side have a timed stop or shut down the endpoint??
    except WebSocketDisconnect:
        #log that it had been disconnect
        #wait for reconnect? 
@app.post("/stop")
def stop():
    stop = True

    '''
    load state
     
    From state:
     - get the list of IPs that are currently in the buffer for analysis 
      
    '''


