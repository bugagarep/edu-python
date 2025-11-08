# lesson #1
name = "Bob"
print("Hello,", name + "!")
# lesson #5
def say_hello():
    print("Hello,", name + "!")
say_hello()
def say_hello(fnk_name):
    print("Hello,", fnk_name + "!")
say_hello(name)
####################################
for i in range(5):
    say_hello("from for")
say_hello(name)
####################################
def add(a, b):
    return a + b
print("sum of 3 and 2 =", add(3, 2))
result = add("3", "2")
print("sum of 3 and 2 =", result)
print("sum of 3 and 2 =", str(add(3, 2)) + result)
print("sum of 3 and 2 =", add(3, 2) + int(result))
########################################################
# max
x = 5; y = 2; z = 8
if x > y:
    max_num = x
else:
    max_num = y
if z > max_num:
    max_num = z
print("max number:", max_num)
def fn_max_num(x1, y1):
    return x1 if x1 > y1 else y1
print("max number:", fn_max_num(fn_max_num(x, y), z))
#####################################################
def add(x):
    print("add:", x)
    return multiply(x + 2)
def multiply(x):
    print("multiply:", x)
    return subtract(x * 3)
def subtract(x):
    print("subtract:", x)
    return x - 5

result = add(4)
print("result:", result)
####################################
# ************** * *************** #
####################################
def suma(n):
    if n == 0:
        return 0
    return n + suma(n - 1)
print("suma:", suma(6))
####################################
def func1(n):
    print("func1", n)
    if n > 0:
        func2(n - 1)
def func2(n):
    print("  func2", n)
    if n > 0:
        func3(n - 1)
def func3(n):
    print("    func3", n)
    if n > 0:
        func1(n - 1)
func1(6)
####################################
print("------------------")
def func(level, n):
    indent = "  " * level
    print(f"{indent}func{level+1}", n)
    if n > 0:
        next_level = (level + 1) % 3
        func(next_level, n - 1)
func(0, 6)
##########################################################
print("------------------")
def hanoi(n, start, target, aux):
    if n == 1:
        print(f"Move disk 1 from {start} to {target}")
        return

    hanoi(n - 1, start, aux, target)
    print(f"Move disk {n} from {start} to {target}")
    hanoi(n - 1, aux, target, start)
hanoi(3, "A", "C", "B")
