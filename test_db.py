from ast import Set
import sqlite3



try:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    users_Pogr = cursor.execute("SELECT user_id FROM 'Pogr_sost_telegram'")
    users_id_Pogr = [i[0] for i in users_Pogr]
 
    conn.commit()

except sqlite3.Error as error:
    print('Error', error)


finally:
    if(conn):
        conn.close()

try:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    users_Detsk = cursor.execute("SELECT user_id FROM 'narcology'")
    users_id_Detsk = [q[0] for q in users_Detsk]
   
    conn.commit()

except sqlite3.Error as error:
    print('Error', error)


finally:
    if(conn):
        conn.close()

try:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    users_Narkolog = cursor.execute("SELECT user_id FROM 'childrens_department'")   
    users_id_Narkolog = [i[0] for i in users_Narkolog]
    
    conn.commit()

except sqlite3.Error as error:
    print('Error', error)


finally:
    if(conn):
        conn.close()

ALL = users_id_Pogr + users_id_Detsk + users_id_Narkolog

def add_info():
        
    pass
    #return


