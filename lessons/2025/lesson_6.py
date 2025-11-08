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