#main

#Learning about socket library.
# import my_functions
import socket
import sqlite3

hostname = socket.gethostname() #this is my computer name
ip_addr = socket.gethostbyname(hostname) # this is my ip address

print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + ip_addr)


conn = sqlite3.connect('databasetest1.db')

c = conn.cursor()

# c.execute("""CREATE TABLE pc_information (
#             hostname text,
#             ipaddress text
#             )""")

c.execute("INSERT INTO pc_information VALUES (?, ?)", (hostname, ip_addr))

conn.commit()

c.execute("SELECT * FROM pc_information")

print(c.fetchall())

conn.commit()

conn.close()
