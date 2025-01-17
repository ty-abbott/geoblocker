import psutil
import time

class parameters:
    def __init__(self, adapters: list=[]):
        self.adapterList = adapters
    list = psutil.net_if_addrs()
    adapter = ""
    isYes = False
    # adapterList = []

#we will need network adapter, and eventually probably email(s) and other stuff 
#could be cool to be able to monitor multiple network adapters... might as well build that functionality now
#https://pypi.org/project/psutil/ 
    def __listInterfaces(self):
        for key,value in self.list.items():
            print(f"{key}: {value}\n")

        return None

    def __verify(self):
        print("\n")
        print (self.list.keys())
        print(self.adapter)
        if self.adapter in self.list.keys():
            return True
        print("Not a valid network adapter.\n")
        time.sleep(3)
        return False
    
    def __input_verify(self, input):
        if (input == "y" or input == "Y"):
            self.isYes = True
            return True
        elif (input == "n" or input=="N"):
            self.isYes = False
            return True
        else:
            return False


    def getParams(self):
        interfaceAdded = False
        print("Which network adapters would you like to monitor")
        while(True):
            self.__listInterfaces()
            self.adapter = input("Adapter: ")
        
            print (f"{self.adapter} was chosen. Is this correct?")
            confirm = input("y or n: ")
            valid = self.__input_verify(confirm)
            if (valid == True and self.isYes == True):
                inThere = self.__verify()
                if(inThere == True):
                    self.adapterList.append(self.adapter)
                    interfaceAdded = True


            #input and error handling needs to be added of course.

            # there needs to be a way to check that this is a valid adapter 
            # ^^ put the keys into a list and then check to make sure that the input is found within that list 
            # if it is valid then add to the state 
            
        #there needs to then be a flag to state if one adapter was even added
        # if there has been one then we display add another? 

            if (interfaceAdded == True):
                while(True):
                    print("Would you like to add another network adapter: ")
                    further = input("y or n: ")
                    valid = self.__input_verify(further)
                    if(valid == True and self.isYes == True):
                        break
                    elif(valid == False):
                        print("Unknown input - try again")
                        continue

                    else:
                        break
                if (self.isYes == False):
                    break


    
        return
