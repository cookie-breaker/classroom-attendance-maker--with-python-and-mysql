import mysql.connector #connecting python with MySQL

#exception handling
try:
    conDict ={'host':'localhost',         
          'user':'root',
          'database':'miniclass',
          'password':'',
              'connect_timeout':1000 }
    db = mysql.connector.connect(**conDict) #creating a database connection
    cursor = db.cursor(buffered = True) #creating a cursor 
    

except Exception:
        print("""OOPS!!
        seems like something's wrong with your MySQL database connection,
               please try again before starting the following process""")
        print()
        print()
        print()
        print()
    
        
#functions of the program
        
def main():
    print("<<<<<<<student attendance marker>>>>>>>")    #this function will return the main menu of the program
    print()
    print("1. enter the data to students information table")
    print("2. mark the attendance")
    print("3. make changes to tables(update/delete/insert)")
    print("4. view student details")
    print("5. view attendance details")
    print("6. view attendance of a student")
    print("7. end the process")
    print()
    global choice
    choice = int(input("enter your preferred options : "))
    print()
   
def studentIn():  #this function will get records from user to store in the studentstbl
    print("enter details of students here, minimum 3 and maximum 5 students can be inserted to the table")
    print()
    record_no = int(input("how many students are going to be in the table ? "))
    print()
    if record_no >2 and record_no <=5:
        for no in range (record_no):
            global studentNo
            studentNo = int(input("enter the student no : "))
            firstName = input("enter the first name of the student : ")
            lastName = input("enter the last name of the student : ")
            print()
            mySQLText = ("INSERT INTO studentstbl (studentNo,firstname,lastname) VALUES (%s,%s,%s)")
            student_details = (studentNo,firstName,lastName)
            cursor.execute(mySQLText,student_details)
    else:
        print()
        print("please make sure to enter at least 3 records and maximum 5 records")
        
    
def attendanceInfo():    #this function will mark the attendace with the records from user
    date_in = input("enter the date in dd-mm-yy format : ")
    print()
    cursor.execute("SELECT studentNo FROM studentstbl")
    data = cursor.fetchall()
    

    
    for item in data:
        print("enter the student number displayed above and then mark the attendance(P if present,A if absent)")
        print()
        print(item)
        print()
        studentNo = int(input("student No : "))
        attendance = input("enter P if present,A if absent : ").upper()
        print()
    
        mycmd = "INSERT INTO attendancetbl (studentNo,attendance,date) VALUES (%s,%s,%s) "
        det = (studentNo,attendance,date_in)
        
        cursor.execute(mycmd,det)
        
       
def update(): # a function which contains a small menu which comes under update option
    print("what you want to update?")
    print()
    print("1. update student number")
    print("2. update first name ")
    print("3. update last name")
    
    
def stunoupd():  #this function will update the student number
    info = input("enter the first name of the student that you need to change the student number of : ")
    newstuNo = input("enter the new student number : ")

    uptxt = "UPDATE studentstbl SET studentNo = '{}'  WHERE firstName = '{}'".format(newstuNo,info)
    cursor.execute(uptxt)
    
    
    

def stuFirstNameupd():  #this function will update the first name of students
    info = input("enter the student number of the student that you need to change the student firstname of : ")
    newstuName = input("enter the new first name of the student : ")

    uptxt = "UPDATE studentstbl SET firstName = '{}'  WHERE studentNo = '{}'".format(newstuName,info)
    
    cursor.execute(uptxt)
    
def stuLastNameupd(): #this function will update the last name of students
    info = input("enter the studnet number of the student that you need to change the student lastname of : ")
    newstuName = input("enter the new last name of the student : ")

    uptxt = "UPDATE studentstbl SET lastName = '{}'  WHERE studentNo = '{}'".format(newstuName,info)
    cursor.execute(uptxt)

def stuInput():  #this function will let the user to input new records to studentstbl
    studentNo = input("enter the student no : ")
    firstName = input("enter the first name of the student : ")
    lastName = input("enter the last name of the student : ")
    print()
    mySQLText = ("INSERT INTO studentstbl (studentNo,firstname,lastname) VALUES (%s,%s,%s)")
    student_details = (studentNo,firstName,lastName)
    cursor.execute(mySQLText,student_details)
    

def delete():  #this function will let the users to delete records from studentstbl
    print("what record you want to delete?")
    cursor.execute ("SELECT * FROM studentstbl")
    data = cursor.fetchall()
    
    print("student No  : date : attendance")
    print()
    for item in data: #printing the records one by one with for loop
        print(item)
    print()    
    delRec = input("type the student number of the record that you need to delete : ")
    cursor.execute("DELETE FROM studentstbl WHERE studentNo = "+ delRec + "")
    print()
    print(cursor.rowcount, "record deleted successfully")
    

      
try:  #exception hanfling
    main()  #calling main function
except Exception as e:
    print("OOPS! somethings's wrong")
    print(e)
while True:  #while loop getting started
    
    if choice == 1: 
        try: #exception handling
            studentIn() #calling studentIn function
            db.commit() #saving changes 
            print()
            print()
            need_to_cont = input("do you want to continue to main menu? (Y/N) : ").upper() #asking whether the user needs to continue or not
            if need_to_cont == "Y":
                main()
            elif need_to_cont == "N":
                db.close()  #disconnecting from MySQL server
                print()
                print("program ended successfully")
                break
            else:
                db.close()  #disconnecting from MySQL server
                print("invalid input")
                break
        except Exception as e:
            print("OOPS! something went wrong,please try again") #error message
            print(e)  
            print()
            main() #calling main function
        
            
        
    
    elif choice == 2:
        try: #exception handling
            attendanceInfo() #calling attendanceInfo function
            db.commit() #saving changes
            print()
            print()
            need_to_cont = input("do you want to continue to main menu? (Y/N) : ").upper()   #asking whether the user needs to continue or not
            if need_to_cont == "Y":
                main()
            elif need_to_cont == "N":
                db.close()
                print()
                print("program ended successfully")
                break
            else:
                db.close() 
                print("invalid input")
                break
        except Exception as e:
            print("OOPS! something went wrong,please try again") #error message
            print(e)
            print()
            main()  #calling main function
            
    
    elif choice == 3:
        print("what change you want to do?") #a small menu for 3rd choice
        print("1. update")
        print("2. insert")
        print("3. delete")
        
        try:  #exception handling
            
            mychoice = int(input("enter your preferred option : "))
            if mychoice == 1:
                update() #calling update function
                upt = int(input("what operation you need to do : ")) #getting user input to proceed
                if upt == 1:
                    stunoupd() #calling stunoupd function to update student's student number
                    db.commit() #saving changes
                    print()
                    print()
                    need_to_cont = input("do you want to continue to main menu? (Y/N) : ").upper()   #asking whether the user needs to continue or not          
                    if need_to_cont == "Y":
                        main() #calling the main menu if user needs to continue
                    elif need_to_cont == "N":
                        db.close() #disconnecting from MySQL server
                        print()
                        print("program ended successfully")
                        break
                    else:
                        db.close() 
                        print("invalid input")
                        break
                elif upt == 2:
                    stuFirstNameupd() #calling stufNameupd function to update student's first name
                    db.commit()
                    print()
                    print()
                    need_to_cont = input("do you want to continue to main menu? (Y/N) : ").upper()   #asking whether the user needs to continue or not
                    if need_to_cont == "Y":
                        main()  #calling main function 
                    elif need_to_cont == "N":
                        db.close()
                        print()
                        print("program ended successfully")
                        break 
                    else:
                        db.close() 
                        print()
                        print("invalid input")
                        break
                elif upt == 3:
                    stuLastNameupd() #calling stulNameupd function to update student's last name
                    db.commit()  #saving changes
                    print()
                    print()
                    need_to_cont = input("do you want to continue to main menu? (Y/N) : ").upper()   #asking whether the user needs to continue or not
                    if need_to_cont == "Y":
                        main()
                    elif need_to_cont == "N":
                        db.close()
                        print()
                        print("program ended successfully")
                        break
                    else:
                        db.close() 
                        print()
                        print("invalid input")
                        break
            elif mychoice == 2:
                
                stuInput() #calling stuNoIn function to insert new data records 
                db.commit()
                print(cursor.rowcount, "record added")
                print()
                print()
                need_to_cont = input("do you want to continue to main menu? (Y/N) : ").upper()  #asking whether the user needs to continue or not
                if need_to_cont == "Y":
                    main()
                elif need_to_cont == "N":
                    db.close() 
                    print()
                    print("program ended successfully")
                    break
                else:
                    db.close()
                    print()
                    print("invalid input")
                    break
            elif mychoice == 3: 
                delete()  #calling delete function to delete records
                db.commit()
                print()
                print()
                need_to_cont = input("do you want to continue to main menu? (Y/N) : ").upper()   #asking whether the user needs to continue or not
                if need_to_cont == "Y":
                    main()
                elif need_to_cont == "N":
                    db.close()
                    print()
                    print("program ended successfully")
                    break 
                else:
                    db.close()
                    print()
                    print("invalid input")
                    break
        except Exception as e: 
            print()
            print("OOPS! something's wrong")  #error message
            print()
            print(e)
    elif choice == 4:
        cursor.execute("SELECT * FROM studentstbl")  #MySQL query command to display every records of the studentstbl
        data = cursor.fetchall() # fetching data from the database
        
        print("student No : first name : last name")
        for item in data: #using for loop to print records one by one 
            print(item)
        need_to_cont = input("do you want to continue to main menu? (Y/N) : ").upper()  #asking whether the user needs to continue or not
        print()
        print()
        if need_to_cont == "Y":
            main()
        elif need_to_cont == "N":
            db.close()
            print()
            print("program ended successfully")
            break
        else:
            db.close()
            print()
            print("invalid input")
            break
        
           
    elif choice == 5:
        cursor.execute("SELECT * FROM attendancetbl")  #MySQL query command to display every records of the attendancetbl
        data = cursor.fetchall()# fetching data from the database
        print("student No  : date : attendance")
        print()
        for item in data: #using for loop to print records one by one
            print(item)
        print()
        print()
        need_to_cont = input("do you want to continue to main menu? (Y/N) : ").upper()  #asking whether the user needs to continue or not
        if need_to_cont == "Y":
            main()
        elif need_to_cont == "N":
            db.close()
            print()
            print("program ended successfully")
            break
        else:
            db.close()
            print()
            print("invalid input")
            break
            
            
            
    elif choice == 6:
        
        try: #exception handling
            
            stunum = input("enter the student number : ")
            print()
            print("student No : date : attendance")
            print()
            cursor.execute("SELECT * FROM attendancetbl WHERE studentNo = "+ stunum + "") # MySQL query to show the attendance of the student, whose student number is entered above
            data = cursor.fetchall()  # fetching data from the database
            print(data)
            print()
            print()
            need_to_cont = input("do you want to continue to main menu? (Y/N) : ").upper()  #asking whether the user needs to continue or not
            if need_to_cont == "Y":
                main()
            elif need_to_cont == "N":
                db.close()
                print()
                print("program ended successfully")
                break
            else:
                db.close()
                print()
                print("invalid input")
                break
        except Exception as e:
           print()
           print("OOPS! something went wrong,please try again") #error message
           print()
           print(e)
           print()
           main() 
            
    elif choice == 7:
        print()
        print("left from the student attendance marker successfully!")
        break
        db.close()  #disconnecting from MySQL server
    else:
        print("please enter a valid input")
        need_to_cont = input("do you want to continue to main menu? (Y/N) : ").upper()
        if need_to_cont == "Y":
            main()
        elif need_to_cont == "N":
            db.close() #disconnecting from MySQL server
            print()
            print("program ended successfully")
            break
        else:
            db.close()  #disconnecting from MySQL server
            print()
            print("invalid input")
            break
        
        
    
    
    
    
     
        
        


       
            
        
