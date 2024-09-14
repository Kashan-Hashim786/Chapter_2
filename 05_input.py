# Input Function always takes values as string
a = input("Enter Number a : ")
b = input("Enter Number b : ")
print("Sum : ",a + b) # a and b are not sum but concatenated 

a = int(input("Enter Number a : "))
b = int(input("Enter Number b : "))
# After type convert from str to int
print("Sum : ",a + b)


