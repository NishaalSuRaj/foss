import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "root", password = "asdfghjkl", database = "foss")
cursor = conn.cursor()
def start():
    while(True):
        print("        Welcome to the library management system     ")
        print("------------------------------------------------------")
        print("Enter 1. To Return a book")
        print("Enter 2. To Display books")
        print("Enter 3. To Borrow a book")
        print("Enter 4. To exit")
        try:
            a=int(input("Select a choice from 1-4: "))
            print()
            if(a==1):
                book = input("Enter the book name : ")
                auth = input("Enter the author name : ")
                rate = int(input("Enter the rate : "))
                query = "insert into library values('" + book + "', '" + auth + "', " + str(rate) + ");"
                cursor.execute(query);
                conn.commit()
            elif(a==2):
                query = "select * from library;"
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    s = ''
                    for i in row:
                        s += str(i)
                        s += ' '
                    print('\t',s)
            elif(a==3):
                name = input("Enter the book name : ")
                query = "delete from library where bookname = '" + name + "';"
                cursor.execute(query);
                conn.commit()
            elif(a==4):
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            print("Please input as suggested.")
start()
