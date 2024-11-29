from tinydb import TinyDB, Query, where
#for simulatneous reads and queued inserts we are going to need to switch to sqlite3 i think 

class data: 
    db1 = TinyDB('data/adapters.json')
    db2 = TinyDB('data/ip.json')
    ip_dict = {}

    def addIP(self, ip):
        self.ip_dict[ip] = {}
        self.ip_dict[ip]["requests"] = 1 
        return
    
    def addAdapter(adapter):

        return
    
    def getIP():
        
        return 
    
    def getAdapters(self):  
