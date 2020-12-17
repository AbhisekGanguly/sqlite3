#main file
#--------------------
#imports
import sqlite3


#--------------------

#connection
#connecting database to python.
conn = sqlite3.connect('customer.db') #creating database to connect to
#connection done succesfully!

#--------------------
#creating a cursor
c = conn.cursor()

#creating a table
#datatypes to choose from:
# text
# integer
# real
# null
# blob
#commenting these because tables have already been created.
# c.execute("""CREATE TABLE customers(
#     first_name text,
#     last_name text,
#     email text,
#     phone_number integer,
#     age integer,
#     address text,
#     illness text
# )""")

# many_customers = [
#     ('Wes', 'Brown', 'wesbrown@gmail.com', '8280834234', '38', 'Queens NYC', 'Cold'),
#     ('Marcus', 'Browney', 'mb@gmail.com', '8280834235', '48', 'Queens NYC', 'COVID'),
#     ('Welberg', 'Santos', 'welberg@gmail.com', '8240734234', '59', 'Time Square NYC', 'Stroke'),
# ]
#
# c.executemany("INSERT INTO customers VALUES (?,?,?,?,?,?,?)", many_customers)
#
# print("Command executed successfully!")

#Query The Database
c.execute("SELECT * FROM customers")
#print(c.fetchall()) #brings out everything
# print(c.fetchone()) #brings only one data, the first item that was inserted
# print(c.fetchmany(3)) #brings many data as specified from the first

#formatting data
items = c.fetchall()

for item in items:
    print(item)


#executing the cursor / commiting it to database
conn.commit()

#close our connection
#it's done by default, but it's best practise to do it explicitely
conn.close()
