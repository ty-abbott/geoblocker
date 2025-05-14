import sqlite3
#for simulatneous reads and queued inserts we are going to need to switch to sqlite3 i think 

class data: 
    ip_dict = {}
    conn = sqlite3.connect('data/ip.db')
    cursor = conn.cursor()

    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS ip_information (
        ip TEXT PRIMARY KEY,
        count INTEGER 
    );
    '''
    
    create_table_sql2 = '''
    CREATE TABLE IF NOT EXISTS traffic_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        port_from INTEGER,
        port_visited INTEGER,
        FOREIGN KEY(ip) REFERENCES ip_information(ip)
    );
    '''
    cursor.execute(create_table_sql)
    cursor.execute(create_table_sql2)



    def addAdapter(adapter):

        return
    
    def getIP(self,ip):
        if ip in self.ip_dict.key():
            self.ip_dict[ip]["requests"] += 1
            return True
        self.ip_dict[ip] = {"requests": 1}
        self.addDatabase(ip)
        return False 
    
    def getAdapters(self):
        return

    def addDatabase(self, ip):
        add_ip_sql = '''
            INSERT INTO ip_information (ip, count) values (?,?) 
            '''
        self.cursor.execute(add_ip_sql, ip, 1)
        self.conn.commit()



#TODO: figure out the other methods.
# - database schema.
