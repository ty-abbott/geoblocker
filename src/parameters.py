import psutil
#we will need network adapter, and eventually probably email(s) and other stuff 
#could be cool to be able to monitor multiple network adapters... might as well build that functionality now
#https://pypi.org/project/psutil/ 
def listInterfaces():
    list = psutil.net_if_addrs()
    for key,value in list.items():
        print(f"{key}: {value}")

    return

def getParams():
    print("Which network adapters would you like to monitor")
    listInterfaces()
    return