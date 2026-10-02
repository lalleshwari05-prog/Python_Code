class Student:

    def __init__(self,first_name,last_name,age):
                self.n1=first_name
                self.n2=last_name
                self.n3=age
                print("My first name is :",self.n1) 
                print("My last name is:",self.n2)
                print("MY age is:",self.n3) 
     

    def show(self):
        print("Inside show method:",self)
        print("Inside show method:",self.n1)

S1=Student("lallu","purush","37")
S1.show() 