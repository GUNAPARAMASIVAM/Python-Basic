class laptop:
    HPprice = 50000
    HPPprocessor = "i5"
    HPram = 8
    HPstorage = 512
    
    DELLprice = 60000
    DELLprocessor = "i7"
    DELLram = 16
    DELLstorage = 1024
    
    LENOVOprice = 55000
    LENOVOprocessor = "i3"
    LENOVOram = 4
    LENOVOstorage = 256

    def __init__(self):
        print("welcome to laptop store")
    def store(self):
        print("Chennai computers")
    def display(self):
        print("OLED display")
       
       
HP= laptop()       
DELL = laptop()
LENOVO = laptop()  

print("HP Laptop:")
print("Price: ", HP.HPprice)
print("Processor: ", HP.HPPprocessor)
print("RAM: ", HP.HPram)
print("Storage: ", HP.HPstorage)
    