import pyshark
from capture import interface
import threading
import time
from scapy.all import *
#dependency 

class capture:
    threads = {}
    stop_events = {}

    def captureStart(self, adapterList: list) -> None:
        
        for i in range(len(adapterList)):
            item = interface(adapterList[i])
            stopEvent = threading.Event()
            self.stop_events[item.interface] = stopEvent
            thread = threading.Thread(target=self.getListIP, args=(item.interface,stopEvent))
            self.threads[item.interface] = thread
            thread.start()
        
        time.sleep(60)
        self.captureStop()
        return 


    '''
    we need to create a better algorithm to make this threading work better

    here is what I am thinking (heavy inspo from threads.py):
        we have two dictionaries
        1. has the stop events -> events are a good little feature for multithreading in python. the stop event will be the value of the dict
        and the interface name will be the key. 
        2. the interface dictionary -> it contains the actual running thread as the value and the key is the interface name

    - So we will get the interface and create the stop event and we will create the thread and we will add both to their respective dictionaries
    - we will start the capture of the interface
    - when it is time to stop then we will call the stop event of the thread. 
    - we can then proceed with further logic. When the logic is completed then we will restart the capture thread as soon as possible 


    *** there really should just be stop and go in this fle

    '''

    def captureStop(self):
        for i in self.stop_events.values():
            i.set()
            print("stopppingggg...")

        for i in self.threads.values():
            i.join()
            

    def getListIP(self, interfaceName, stopEvent):
        #here is where we will get the set of IPs 
        
        while not stopEvent.is_set(): #we will do the actual pyshark packet capture here. The adding IP logic will be called from here. 
            print("listening")
            packets = sniff(iface="eth0", count=1) 
            for i in packets:
                if i.haslayer(IP):
                    print(i[IP].src)
            
        print(f"task {interfaceName} is stopping" )
        return 