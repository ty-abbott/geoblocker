import pyshark
#dependency 


def network(adapterList: list) -> None:
    
    return 

def getListIP(adapter: str):
    #here is where we will get the set of IPs 
    capture = pyshark.LiveCapture(interface=adapter)
    return 