import threading
import time 
from scapy.all import *
import sys
import websockets
import asyncio 

loop_bool = False

def is_stop():#I suspect we may need to include a packet argument
    return loop_bool

def process_packet(pkt):
    #ok here is where we build out the sniffing logic
    #right now we will gather IP, dst Port, and Protocol 
    
async def collect(interface1):
    async with websockets.connect("URL") as websocket:#we connect to the server via websocker
        recv_task = asyncio.create_task(recieve_stop(websocket)) #we create a new task with a coroutine, this coroutine is running and waiting for a stop
        sniff(iface=interface1, stop_filter=is_stop, prn=process_packet) #sniff and then use the recv_task to send to server. This sniff may not work because im not sure stop_filter is a possible param

        #create websocket connection
        #error handling with that 
        #start gathering from the interfaces 
        #figure out logic to only do new IPs 
        #send in websocket call to the server via the websocket
#REMEMBER WE CAN GIVE A LIST OF INTERFACES
async def recieve_stop(websocket):
    while True:
        message = await websocket.recv()
        if message == "Stop":
            loop_bool = True #the actual stop logic, loop_bool might be pointless. This all looks for a message stop and then should stop sending stuff and look to reconnect 
def main():
    interface1 ="en1"
    asyncio.run(collect(interface1))






if __name__ == "__main__":
    main()
