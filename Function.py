def add():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Sum is: ", a+b)  
    
def sub():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Difference is: ", a-b,)
    
def mul():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Product is: ", a*b)      
    
    
def div():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Quotient is: ", a/b)
    
def findevenorodd():
    a=int(input("Enter a number: "))
    if a%2==0:
        print("Number is even")
    else:
        print("Number is odd")    
        
        
def passorfail():
    a=int(input("Enter marks: "))
    if a>=35:
        print("You have passed")
    else:
        print("You have failed") 
        
def printrange():
    a=int(input("Enter the start of range: "))
    b=int(input("Enter the end of range: "))
    for i in range(a, b+1):
        print(i, end=' ')
    print()                    


                   

    