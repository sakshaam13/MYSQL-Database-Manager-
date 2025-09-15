#A menu driven program with options to:
#   1) Display  2) Add  3) Update (data of relation s_info).
#Prepared by Saksham Rao Chaturvedi
import mysql.connector as mysqlcon

def print_relation(dataa):
    print()
    print()
    print("Name\t\tClass\t\tRoll no.\tMarks\n-------------------------------------------------------")
    for i in dataa:
        for j in i:
            print(j,"\t\t",end='')
        print()

#estabilishing connection
mycon=mysqlcon.connect(host="localhost", user="root", password="root", database="student")
print("Connection establised!")
#creating cursor object and taking choice input
cur = mycon.cursor()
print("1>Display database\n2>Add to database\n3>Update database")
c=int(input("Enter your choice>>"))
#creating the relation login_data
query ="CREATE TABLE IF NOT EXISTS s_info(name varchar(20) not null,class int not null,rollno int primary key,marks int not null);"
cur.execute(query)
mycon.commit()
#Menu Base Operation
if c==1:
    #executing queries
    query = "select * from s_info"
    cur.execute(query)
    data = cur.fetchall()
    #printing table and closing connection
    print_relation(data)
    mycon.close()
elif c==3:
     #Taking inputs
     rollno=input("Enter student rollno: ")
     name=input("Enter student new name: ")
     Class=input("Enter student new class: ")
     marks=input("Enter student new marks: ")
     #executing queries
     query ="update s_info set name='{0}' where rollno={1}".format(name,rollno)
     cur.execute(query)
     query ="update s_info set class='{0}' where rollno={1}".format(Class,rollno)
     cur.execute(query)
     query ="update s_info set marks='{0}' where rollno={1}".format(marks,rollno)
     cur.execute(query)
     mycon.commit()
     query = "select * from s_info"
     cur.execute(query)
     data = cur.fetchall()
     #printing table and closing connection
     print_relation(data)
     mycon.close()
elif c==2:
    #Taking inputs
    name=input("Enter student name: ")
    Class=input("Enter student class: ")
    rollno=input("Enter student rollno: ")
    marks=input("Enter student marks: ")
    #executing queries
    query ="Insert into s_info values('%s',%s,%s,%s)"%(name,Class,rollno,marks)
    cur.execute(query)
    mycon.commit()
    query = "select * from s_info"
    cur.execute(query)
    data = cur.fetchall()
    #printing table and closing connection
    print_relation(data)
    mycon.close()
else:
    print()
    print()
    print("Invalid Choice!!!!")
    exit()
try:
    while True:
        continue
except KeyboardInterrupt:
    print()
    print("Quitting................Closing Database!!!!")
