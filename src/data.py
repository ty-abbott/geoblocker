import sqlite3
#for simulatneous reads and queued inserts we are going to need to switch to sqlite3 i think 

class data: 
    ip_dict = {}
    conn = sqlite3.connect('data/ip.db')
    cursor = conn.cursor()



    def addAdapter(adapter):

        return
    
    def getIP(self,ip):
        if ip in self.ip_dict.key():
            self.ip_dict[ip]["requests"] += 1
            return True
        self.ip_dict[ip] = {"requests": 1}
        addDatabase()
        return False 
    
    def getAdapters(self):
        return

    def addDatabase(self, ip):
        



#TODO: figure out the other methods.
# - database schema.
