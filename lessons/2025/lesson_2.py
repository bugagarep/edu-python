# if
#######################################################
### and ##### | ## or ##### | ## xor ##### | # not ####
# 1  *  1 = 1 | 1  +  1 = 1 | 1  =/  1 = 0 | -|   1 = 0
# T and T = T | T  or T = T | T  xor T = F | not  T = F
# 1  *  0 = 0 | 1  +  0 = 1 | 1  =/  0 = 1 | -|   0 = 1
# T and F = F | T  or F = T | T  xor F = T | not  F = T
# 0  *  1 = 0 | 0  +  1 = 1 | 0  =/  1 = 1
# F and T = F | F  or T = T | F  xor T = T
# 0  *  0 = 0 | 0  +  0 = 1 | 0  =/  0 = 0
# F and F = F | F  or F = F | F  xor F = F
#######################################################
if True:
    print("True is True")
if False: print("True")
else:
    print("False is False")

if 1:
    print("1 is True")
if 0: print("True")
else:
    print("0 is False")
#################################
x = input("Enter a number: ")
if x == 123:
    print("x == 123 is True")
else:
    print("x == 123 is False")
#################################
x = int(input("Enter a number: "))
if x == 123:
    print("x == 123 is True")
else:
    print("x == 123 is False")
##############################################
x = float(input("Enter a number: "))
y = 123
if x == y:
    print("x(float) == 123(int) is True")
else:
    print("x == 123 is False")

if x is y:
    print("x == 123 is True")
else:
    print("x(float) == 123(int) is False")
##############################################
x = int(input("Enter a number: "))
if x != 123:
    print("x != 123 is False")
else:
    print("x == 123 is True")
#################################
x = int(input("Enter a number: "))
thisIsTrue = x == 123
if thisIsTrue:
    print("x == 123 is True")
else:
    print("x == 123 is False")
############################################
x = int(input("Enter a 1st number(123): "))
y = int(input("Enter a 2nd number(456): "))
firstIsTrue = x == 123
secondIsTrue = y == 456
if firstIsTrue and secondIsTrue:
    print("x == 123 is True and y == 456 is True")
else:
    print("x and y is False")
############################################
x = int(input("Enter a 1st number(123): "))
y = int(input("Enter a 2nd number: "))
firstIsTrue = x == 123
secondIsTrue = y == 456
if firstIsTrue or secondIsTrue:
    print("x == 123 is True or y == 456 is True")
else:
    print("x or y is False")
#################################
x = int(input("Enter a number: "))
thisIsTrue = x == 123
if not thisIsTrue:
    print("not x == 123 is True")
else:
    print("not x == 123 is False")
#################################
x = int(input("Enter a number: "))
thisIsTrue = True if x == 123 else False
if thisIsTrue:
    print("not x == 123 is True")
else:
    print("not x == 123 is False")
##############################################
x = input("Enter a string(Hello): ")
if x[0] == "H":
    print("1st character is H")
    if x[1] == "e":
        print("2nd character is e")
        if x[2] == "l":
            print("3rd character is l")
            if x[3] == "l":
                print("4th character is l")
                if x[4] == "o":
                    print("5th character is o")
                else:
                    print("wrong character 'o'")
            else:
                print("wrong character 'l'")
        else:
            print("wrong character 'l'")
    else:
        print("wrong character 'e'")
else:
    print("wrong character 'H'")

print("if elif else")
if x[0] == "H":
    print("1st character is H")
elif x[1] == "e":
    print("2nd character is e")
elif x[2] == "l":
    print("3rd character is l")
elif x[3] == "l":
    print("4th character is l")
elif x[4] == "o":
    print("5th character is o")
else:
    print("wrong some character")
#################################
