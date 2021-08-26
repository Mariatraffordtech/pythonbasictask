class Staff:
    def __init__(self,staffID,category,mobile, status):
        self.staffID = staffID

        self.category = category

        self.mobile = mobile

        self.status =  status

        
         
    def accept(self,staffID,category,mobile, status):
        dt = Staff(staffID,category,mobile, status) 
        ls.append(dt)
        
        


    def display(self, dt):
            print("staffID   : ", dt.staffID)
            print("category : ", dt.category)
            print("mobile : ", dt.mobile)
            print("status : ", dt.status)
            
            
         
    def search(self, stf):
        for k in range(ls.__len__()):
            if(ls[k].StaffID == stf):
                return k  
        ser = dts.search(2) 
        dts.display(ls[ser])   
  
    def delete(self, stf):
        k = dts.search(stf)  
        del ls[k]
        dts.delete(2)
    
    def update(self, stf, Num):
        k = dts.search(stfid)
        stfs = Num
        ls[k].staffID = stfs;
        dts.update(3, 2)
         
ls =[]
dts = Staff(" ", 0, 0, 0)
  
print("\nOperations used, ")
print("\n1.Accept Staff details\n2.Display Staff Details\n" 
"3.Search Details of a Staff\n4.Delete Details of Staff" 
"\n5.Update Staff Details\n6.Exit")
 
dts.accept(21,"Non-Teaching",2267898768,"M")
dts.accept(30,"Teaching",1267898765,"M")
dts.accept(17,"Teaching",6789876780,"M")


print("\n")
print("\nList of Staffs\n")
for k in range(ls.__len__()):    
    dts.display(ls[k])

print("\n Staff Found, ")

print(ls.__len__())
print("List after deletion")
for k in range(ls.__len__()):    
    dts.display(ls[k])
             
print(ls.__len__())
print("List after updation")
for k in range(ls.__len__()):    
    dts.display(ls[k])





          
  

         

