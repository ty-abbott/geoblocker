import threading
import time 
from scapy.all import *
import sys

def collect(interface1):
    while(True):
        #create websocket connection
        #error handling with that 
        #start gathering from the interfaces 
        #figure out logic to only do new IPs 
        #send in websocket call to the server via the websocket

#REMEMBER WE CAN GIVE A LIST OF INTERFACES

def main():
    interface1 ="en1"
    collect(interface1)






if __name__ == "__main__":
    main()
