import sqlite3
#for simulatneous reads and queued inserts we are going to need to switch to sqlite3 i think 

class data: 
    ip_dict = {}

    def addAdapter(adapter):

        return
    
    def getIP(self,ip):
        if ip in self.ip_dict.key():
            self.ip_dict[ip]["requests"] += 1
            return True
        self.ip_dict[ip] = {"requests": 1}
        return False 
    
    def getAdapters(self):
        return
