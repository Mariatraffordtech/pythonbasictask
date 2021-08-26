class Student:
    def __init__(self,studID,name,age, status,classID):
        self.studID = studID

        self.name = name

        self.age = age

        self.status =  status

        self.classID = classID
         
    def accept(self,studID,name,age, status,classID):
        ob = Student(studID,name,age, status,classID) 
        ls.append(ob)
        
        


    def display(self, ob):
            print("studID   : ", ob.studID)
            print("name : ", ob.name)
            print("age : ", ob.age)
            print("status : ", ob.status)
            print("classID : ", ob.classID)
            
         
    def search(self, st):
        for i in range(ls.__len__()):
            if(ls[i].StudID == st):
                return i   
        s = obj.search(2) 
        obj.display(ls[s])   
  
    def delete(self, st):
        i = obj.search(st)  
        del ls[i]
        obj.delete(2)
    
    def update(self, st, No):
        i = obj.search(rn)
        stud = No
        ls[i].studID = stud;
        obj.update(3, 2)
         
ls =[]
obj = Student(" ", 0, 0, 0, 0)
  
print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n" 
"3.Search Details of a Student\n4.Delete Details of Student" 
"\n5.Update Student Details\n6.Exit")
 
obj.accept(2,"tin",22,"M",4)
obj.accept(3,"Yin",12,"M",6)
obj.accept(7,"LINU",18,"M",8)


print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):    
    obj.display(ls[i])

print("\n Student Found, ")

print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):    
    obj.display(ls[i])
             
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):    
    obj.display(ls[i])
          
  

         

