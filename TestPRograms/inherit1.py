#inheritance in python
class Father:
    fn=""
    age1=""
    def __init__(self,father_name,age):

        Father.fn=father_name
        Father.age1=age
    def show(self):

        print("i love my Son")


class Son(Father):
    def __init__(self,Child_name,age):
        self.cn=Child_name
        self.ln=Son.fn
        
        self.age2=age 
        print("hey my family")

    def method(self):

        print("i love my Father:",Son.fn)
        print("His age is:",Son.age1)
S1=Father("purush",37)
S1.show()
S2=Son("Laksh",8)
S2.method()




       
