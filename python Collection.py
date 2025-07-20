# list[]
# tuple()
# set{}
# dictionary{}

#list
a =[1, 2, 3, 4, 5]
print(a[0])  
print(a[1])  
print(a[2])
print(a[3])  
print(a[4])  


a =[1, 2, 3, 4, 5]
a.pop(2)  
print(a)

a =[1, 2, 3, 4, 5]
a.append(6)
print(a)

a =[1, 2, 3, 4, 5]
a.insert(2, 10)
print(a)

a =[1, 2, 3, 4, 5]
b =[6, 7, 8, 9, 10] 
a.extend(b)
print(a)


#tuple
a =(1, 2, 3, 4, 5)
b=list(a)
print(b[0])


#dictionary
a = {"name": "John", "age": 30, "city": "New York"}
print(a["name"])

#dictionary - keys
a = {"name": "John", "age": 30, "city": "New York"}
print(a.keys())

#dictionary - values
a = {"name": "John", "age": 30, "city": "New York"}
print(a.values())