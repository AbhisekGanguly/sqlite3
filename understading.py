import sqlite3
conn = sqlite3.connect("industry.db")

c = conn.cursor()

# c.execute("""
#     CREATE TABLE customers(
#     f_name text,
#     l_name text,
#     phone integer,
#     address text
#     )
# """)
#
# c.execute("""
#     CREATE TABLE exployee(
#     f_name text,
#     l_name text,
#     phone integer,
#     address text
#     )
# """)

i = 1
while i == 1:
    q1 = str(input("do you want to add customers? (yes/no) \n"))
    q1 = q1.capitalize()
    q1 = q1[0]
    if ord(q1) == 89:
        i = 1
        fnc = str(input("Enter customer first name: "))
        lnc = str(input("Enter customer last name: "))
        phone = int(input("Enter Phone number: "))
        address = str(input("Enter address: "))
        customer_details = [fnc, lnc, phone, address]
        c.execute("INSERT INTO customers VALUES(?,?,?,?)", customer_details)
    elif ord(q1) == 78:
        i = 0
    else:
        print("Wrong input")
        i = 0

items = c.execute("SELECT * FROM customers")
for item in items:
    print (item)

conn.commit()

conn.close()
