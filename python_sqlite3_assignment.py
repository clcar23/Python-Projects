fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.png','graffititxt.png')


import sqlite3
#importing the sqlite3 module

conn = sqlite3.connect('assignment1.db')
#creating variable 'conn' that connects/creates 'assignment' database

#opens the connection 
with conn:
    #creates the cur variable
    cur = conn.cursor()
    #using the execute command to create the table and its two columns
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_nicknames( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_name TEXT \
    )")
    #commiting the changes
    conn.commit()
    #closing the connection
conn.close()


conn = sqlite3.connect('assignment1.db')

with conn:
    cur = conn.cursor()
    #setting up a loop to iterate through the db
    for i in fileList:
        if i.endswith('.txt'):
            #looking for files ending in .txt and adding them into the database
            cur.execute("INSERT INTO tbl_nicknames(col_name) VALUES (?)", (i,))
    conn.commit()
conn.close()


conn = sqlite3.connect('assignment1.db')

with conn:
    cur = conn.cursor()
    #execute a SELECT statement to get the data from tbl_nicknames
    cur.execute("SELECT * FROM tbl_nicknames")
    #using the fetchall method to get all the results
    results = cur.fetchall()
    #printing the results
    print(results)
conn.close


     

