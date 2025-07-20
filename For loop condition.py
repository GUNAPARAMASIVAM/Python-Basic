for i in range(1, 11):
    print(i,"*2", "=", i * 2)
    
 # 1   
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
for i in range(a+1, b): 
    print(i)  
    
 # 2

count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count= count + 1
        print(count)

a = []
print("Enter 10 numbers:")
sum = 0
for i in range(10):
    num = int(input())
    a.append(num)
    print(a)
    sum += num
print("Sum:", sum)


a = []
for a in range (1,6):
    print("Number is:", a, "and cube is:", a**3)
    
    
    
for i in range(1, 6):
     print(i,"apple") 
     for j in range(1, 3):
       print(j,"flower") 
       
       
       
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()          