mark=int(input("Enter your mark: "))
if mark > 35:
    print("You are pass")
else:
    print("You are fail")    
    
income = int(input("Enter your income: "))
if income > 7000:
    print("eligible for scholarship")
else:
    print("not eligible for scholarship") 
    
number = int(input("Enter a number: "))
if number % 3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")
    
number = int(input("Enter a number: "))
if number % 5 == 0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")    
                   
# binary operators
a=int(input("Enter first number: "))
if a%3 == 0 and a%5 == 0:
    print("Number is divisible by both 3 and 5")    
else:
    print("Number is not divisible by both 3 and 5")  
    
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
    
    
score = int(input("Enter your score: "))
if score <= 35:
    print("poor student")
elif score > 35 and score <= 70:
    print("average student")
elif score > 70:
    print("good student")
else:
    print("invalid score")
        
        
score_percentage = int(input("Enter your score percentage: "))
Name=input("Enter your name: ")
Department=input("Enter your department: ")
Location=input("Enter your location: ")
if score_percentage > 70:
    print("you are eligible", Name, "from", Department, "department in", Location, "for scoring above 70%!")
else:
    print("you are not eligible", Name, "from", Department, "department in", Location, "for scoring below 70%!")    
    
       
salary = int(input("Enter your salary: "))
age = int(input("Enter your age: "))
if salary >= 20000 and age > 25:
    loan = int(input("Enter loan amount: "))
    if loan <= 500000:
        print("Loan approved")
    else:
        print("Loan not approved")
else:
    print("Loan not approved due to salary or age criteria")
        
    