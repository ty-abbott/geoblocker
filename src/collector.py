import threading
import time 
from scapy.all import *

def fun1():
    print("Working1")
def fun2():
    print("Working2")






def main():

    ``
    t1 = Thread(target=fun1)
    t2 = Thread(target=fun2)

    t1.start()
    t2.start()






if __name__ == "__main__":
    main()
