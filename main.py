import string
import random
from pathlib import Path
import json

class Students:
    data = []
    database = "student.json"
    
    with open(database) as fs:
        data = json.loads(fs.read())

    @classmethod
    def updatedata(cls):
        with open(cls.database,"w") as fs:
            fs.write(json.dumps(cls.data))

    @classmethod
    def Randomid(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        numbers = random.choices(string.digits,k = 3)
        spchar = random.choices("!!@#$%^&*", k = 2)
        id = alpha + numbers + spchar
        random.shuffle(id)
        return "".join(id)


    def registerstudent(self):
        stu = {
            "id":1,
            "name":input("tell your name"),
            "email": input("tell your email"),
            "password":input("tell your password"),
            "age":int(input("tell your age"))
        }
        Students.data.append(stu)
        Students.updatedata()
    
    def readsinglestudent(self):
        id = input("Enter Id:")
        password = input("Enter your password:")
        student = [i for i in Students.data if i["id"]==id and i["password"]==password]
        if len(student)==0:
            print("Sorry wrong credentials try again")
        else:
            for i in student[0]:
                print()
                print(f"{i} : {student[0][i]}")

    def accessdatabase(self):
        a = Students.data
        counter = 1
        print()
        for i in a:
            print()
            print(counter)
            print()
            for j in i:
                print(f"{j} : {i[j]}")
            counter += 1

    def updatestudent(self):
        id = input("Enter Id:")
        password = input("Enter your password:")
        student = [i for i in Students.data if i["id"]==id and i["password"]==password]
        if len(student) == 0:
            print("wrong credentials")
        else:
            print("either write new name or press enter to skip")
            stu = {
                "name": input("please update your name"),
                "email": input("tell your new email"),
                "password": input("tell your new password"),
                "age": int(input("tell your new age or press 0"))
            }
            if stu["name"] == "":
                stu["name"] = student[0]["name"]
            if stu["email"]== "":
                stu["email"] = student[0]["email"]
            if stu["password"]== "":
                stu["password"] = student[0]["password"]
            if stu["age"]== 0:
                stu["age"] = student[0]["age"]

        for i in stu.keys():
            if stu[i]==student[0][i]:
                continue
            else:
                student[0][i]=stu[i]
        self.updatedata()

    def deletestudent(self):
        id = input("Enter Id:")
        password = input("Enter your password:")
        student = [i for i in Students.data if i["id"]==id and i["password"]==password]

        if len(student) == 0:
            print("wrong credentials")
        else:
            check = input("Are you sure you want to delete press Y/N")

            if check == "Y":
                studentindex = Students.data.index(student[0])
                Students.data.pop(studentindex) 
                self.updatedata()
            elif check == "N":
                pass
            else:
                print("Invalid input")

while True:     
    obj = Students()
    print(""" 
    select an option
          1. Register a Student
          2. Login Student profile
          3. Access database
          4. Update Student data
          5. Delete Student data
          6. Exit the application
    """)
    n = int(input("Tell your response"))
    if n == 6:
        exit(0)
    
    if n == 1:
        obj.registerstudent()
    
    elif n == 2:
        obj.readsinglestudent()
    
    elif n==3:
        obj.accessdatabase()
    
    elif n==4 :
        obj.updatestudent()
    
    elif n==5:
        obj.deletestudent()
    
    else:
        print("Invalid input")