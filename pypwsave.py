import sqlite3

connection = sqlite3.connect('./pwsafe.db')
cursor = connection.cursor()
#create_table = "CREATE TABLE pwsafe (service text, user text, password text)"
#cursor.execute(create_table)
service = input("Your service: ")
username = input("Your user: ")
password = input("Your password: ")
triple_date = (service, username, password)
insert_data = "INSERT INTO pwsafe VALUES (?, ?, ?)"
cursor.execute(insert_data, triple_date)
print("Show DB \n")
show_date = "SELECT * FROM pwsafe;"
for row in cursor.execute(show_date):
    print (row)



connection.commit()
