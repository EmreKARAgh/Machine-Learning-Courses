# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 23:08:24 2019

@author: EmreKARA
"""

import sqlite3

def selections():
    connection = sqlite3.connect("chinook/chinook.db")
    
    cursor = connection.execute("""select FirstName, LastName from customers where city='Prague' or city='Berlin' order by firstName, lastName desc""")
    
    for row in cursor:
        print(row)
    
    
    print("\n\n\nSecond Query...")
    
    cursor = connection.execute(""" select city,count(*) from customers group by city having count(*)>1 order by count(*) """)
    
    for row in cursor:
        print(row)
    
    print("\n\n\nThird Query...")
    
    cursor = connection.execute(""" select FirstName, LastName from customers where FirstName like 'a%' """)
    
    for row in cursor:
        print(row)
        
    cursor = connection.execute(""" select * from customers where FirstName like 'em%' """)
    
    print("\n\n\nFourth Query...")
    for row in cursor:
        print(row)
        
    connection.close()

def insertions():
    connection = sqlite3.connect("chinook/chinook.db")

    
    connection.execute(""" insert into customers (firstName,lastName,city,email) values ('Emre','Kara','Adiyaman','emre@gmail.com') """)
    
    connection.commit()
    connection.close

def update():
    connection = sqlite3.connect("chinook/chinook.db")
    
    connection.execute(""" update customers set firstName='Emre2' where firstName='Emre' """)
    
    
    connection.commit()
    connection.close()
    
def remove():
    connection = sqlite3.connect("chinook/chinook.db")
    
    connection.execute(""" delete from customers where lastname='Kara' """)
    
    
    connection.commit()
    connection.close()
def join():
    connection = sqlite3.connect("chinook/chinook.db")
    
    cursor = connection.execute(""" select albums.title,artists.Name  from artists inner join albums on artists.ArtistId = albums.ArtistId """)
    
    for row in cursor:
        print(row)
    connection.close()
    
    
#insertions()
#update()    
#selections()
join()
#remove()
#selections()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    