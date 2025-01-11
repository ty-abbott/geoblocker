import threading
import time 
from scapy.all import *
import sys
import websockets
import asyncio 

loop_bool = True

async def collect(interface1):
    async with websockets.connect("URL") as websocket:
        recv_task = asyncio.create_task(recieve_stop(websocket))
    while(True):
        #create websocket connection
        #error handling with that 
        #start gathering from the interfaces 
        #figure out logic to only do new IPs 
        #send in websocket call to the server via the websocket
        if loop_bool == False:
            #stop the presses
#REMEMBER WE CAN GIVE A LIST OF INTERFACES
async def recieve_stop(websocket):
    while True:
        message = await websocket.recv()
        if message == "Stop":
            loop_bool = False
def main():
    interface1 ="en1"
    async.run(collect(interface1))






if __name__ == "__main__":
    main()
