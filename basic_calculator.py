class MathOp:
    def AddOp(self):
        self.a=int(input("Enter first no:"))
        self.b=int(input("Enter second no:"))
        self.c=self.a+self.b
        print("Addition is:",self.c)
    def SubOp(self):
        self.a=int(input("Enter first no:"))
        self.b=int(input("Enter Second no:"))
        self.c= self.a - self.b
        print("Sub is:",self.c)
    def MulOp(self):
        self.a=int(input("Enter first no:"))
        self.b=int(input("Enter Second no:"))
        self.c= self.a * self.b
        print("Addition is:",self.c)
        print("Multiplication is:",self.c)
#main body
obj=MathOp()
while True:
        print("\n1. Addtion")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Exit")    

        ch=int(input("Enter choice to perform any opertaion"))
        if ch==1:
            obj.AddOp()
        elif ch==2:
            obj.SubOp()
        elif ch==3:
            obj.MulOp()
        elif ch==4:
            print("\nProgram Stop")
            break
        else:
            print("Wrong Choice")    