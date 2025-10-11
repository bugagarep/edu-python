###### strings
name = "Bob"
print("Hello,", name)
print("Hello,", name, "!", sep="")
print("Hello,", name + "!")
print(f"Hello, {name}!")
print("------------------------------")
####### int/float/str
value1 = input("enter the number: ") # 123
value2 = input("enter the number: ") # 321
result = value1 + value2
print(result)
print("------------------------------")
value3 = int(input("enter the number: ")) # 123
value4 = int(input("enter the number: ")) # 321
result = value3 + value4
print(result)
print("------------------------------")
####### swap var
x = 1
y = 2
z = x
x = y
y = z
print(f"result -> x = {x}, y = {y}")
print("------------------------------")
x_1 = 1
y_1 = 2
x_1, y_1 = y_1, x_1
print(f"result -> x_1 = {x_1}, y_1 = {y_1}")
print("------------------------------")
x_2 = 1
y_2 = 2
print(f"before -> x_2 = {x_2} | {x_2:04b} bits, y_2 = {y_2} | {y_2:04b} bits")
y_2 = x_2 ^ y_2
print(f"step 1 -> y_2 = {y_2} | {y_2:04b} bits")
x_2 = x_2 ^ y_2
print(f"step 2 -> x_2 = {x_2} | {x_2:04b} bits")
y_2 = x_2 ^ y_2
print(f"step 3 -> y_2 = {y_2} | {y_2:04b} bits")
print(f"result -> x_2 = {x_2}, y_2 = {y_2}")
print("------------------------------")