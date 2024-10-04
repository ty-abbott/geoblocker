import pyshark
#dependency 

def getListIP(adapter):
    #here is where we will get the set of IPs 
    capture = pyshark.LiveCapture(interface=adapter)
    return 