a = [1,2,3,4,5]
def print_a(a):
    print(*a)
print_a(a)
def print_a_2(a,b,c,d,e):
    print(a,b,c,d,e)
print_a_2(*a)
#################################################
a = {1:"one",2:"two",3:"three",4:"four",5:"five"}
def print_a_dict(a):
    print(**a)
print_a(a)
a = {"a":"one","b":"two","c":"three","d":"four","e":"five"}
def print_a_2_dict(a,b,c,d,e):
    print(a,b,c,d,e)
print_a_2_dict(**a)
print(*a)
###########################################################
a = {"a":"one","b":"two","c":"three","d":"four","e":"five"}
print(a)
a["f"] = "six"
print(a)
for key, value in a.items():
    print(key, "+", value)
print(list(a.items()))
#######################################
a = set("abc")
print(a)
a.add("d")
print(a)
a.add("a")
a.add("a")
print(a)
##############################################
pairs = [(1, "one"), (2, "two"), (3, "three")]
for num, name in pairs:
    print(num, "+", name)
##############################################
student = {
    "name": "Bob",
    "age": 15,
    "grade": 9,
    "subjects": ["Math", "Informatics", "Physics"],
    "average_score": 11.2
}
print(student)
print(student["average_score"])
student["average_score"] = 5
print(student)
student.update({"average_score": "12+"})
print(student)
student["subjects"][1] = "Chemistry"
print(student)
##############################################
#####   lesson #2   ####################
def day_name_with_if(day):
    print("day_name_with_if -- called")
    if day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6 or day == 7:
        return "Weekend"
    else:
        return "Unknown day"
def day_name_with_match(day):
    print("day_name_with_match -- called")
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6 | 7:
            return "Weekend"
        case _:
            return "Unknown day"
def day_name_with_dict(day):
    print("day_name_with_dict -- called")
    tmp_list = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6 | 7: "Weekend"}
    #tmp_list = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    # tmp_list = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Weekend", 7: "Weekend"}
    # return tmp_list[day]
    return tmp_list.get(day, "Unknown day")

print(day_name_with_if(1))
print(day_name_with_if(7))
print(day_name_with_if(9))
print()
print(day_name_with_match(1))
print(day_name_with_match(7))
print(day_name_with_match(9))
print()
print(day_name_with_dict(1))
print(day_name_with_dict(7))
print(day_name_with_dict(9))
####################################
# ************** * *************** #
####################################
def grade_category(score):
    categories = {
        range(10,12): "excellent",
        range(7,9):  "good",
        range(4,6):  "fine",
        range(1,3):   "okay"
    }
    for rng, name in categories.items():
        if score in rng:
            return name
    return "error"
print(grade_category(5))
print(grade_category(11))
print(grade_category(25))
####################################
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "error"

operations = {"+": add, "-": sub, "*": mul, "/": div}

oper = input("enter the operation (+, -, *, /): ")
x, y = 10, 5
print("result:", operations.get(oper, lambda a, b: "unknown operation")(x, y))
##############################################################################
######## Caesar ######################
def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            new_ch = chr((ord(ch) - base + shift) % 26 + base)
            result += new_ch
        else:
            result += ch
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

original = "Hello, World!"
encrypted = caesar_encrypt(original, 3)
decrypted = caesar_decrypt(encrypted, 3)

print("original:", original)
print("encrypted:", encrypted)
print("decrypted:", decrypted)

######## dictionary ######################
def build_caesar_dict(shift):
    lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    table = {}
    for i in range(26):
        table[lower[i]] = lower[(i + shift) % 26]
        table[upper[i]] = upper[(i + shift) % 26]
    return table

def caesar_encrypt_dict(text, shift):
    table = build_caesar_dict(shift)
    return "".join(table.get(ch, ch) for ch in text)

def caesar_decrypt_dict(text, shift):
    return caesar_encrypt_dict(text, -shift)

original = "Hello, World!"
encrypted = caesar_encrypt_dict(original, 5)
decrypted = caesar_decrypt_dict(encrypted, 5)

print("original:", original)
print("encrypted:", encrypted)
print("decrypted:", decrypted)
