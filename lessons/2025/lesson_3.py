for i in range(5):
    print(i)
print()
for i in range(2, 5):
    print(i)
print()
for i in range(2, 5, 3):
    print(i)
print()
i = 0
while i<5:
    print(i)
    i += 1
print()
for i in range(5):
    if i % 2 == 0:
        print("i % 2 == 0")
        continue
    if i == 3:
        break
    print(i)
else:
    print("the end")
print()
############################
list_1 = [1, 2, True, "3.14", 3.14, (0,1)]
print(list_1)
print(list_1[3])
list_1[3] = "Hello"
print(list_1[3])
list_1.append(171)
print(list_1)
list_1.remove(True)
list_1.remove('Hello')
list_1.remove((0,1))
list_1.remove(3.14)
list_1.remove(True)
list_1.append(2)
list_1.append(7)
list_1.insert(3, 717)
print(list_1)
list_2 = [9, 9, 9]
list_2.extend(list_1)
print(list_2)
print(list_1)
list_1.sort()
print(list_1)
list_1.reverse()
print(list_1)
list_1.pop(0)
print(list_1)
print(list_1.count(2))
print(len(list_1))
##############################
list_1 = [2,4,6,8]
for i in range(len(list_1)):
    print(list_1[i], " |", list_1[i] ** 2)
print()
for item in list_1:
    print(item, " |", item ** 2)
print()
pos = 0
while pos < len(list_1):
    print(list_1[pos], " |", list_1[pos] ** 2)
    pos += 1
print()
