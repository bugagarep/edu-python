matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9,10],
          [11,12,13,14,15],
          [16,17,18,19,20]]

for i in range(len(matrix)):
    print(i)
print("-------------")
n = 3
m = 3
for i in range(n):
    for j in range(m):
        print(matrix[i][j])
print("-------------")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j])
print("-------------")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()
print("-------------")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i == j:
            print(matrix[i][j], end=" ")
        print(end=" ")
        print(end=" ")
    print()
print("-------------")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i + j == len(matrix[0]) - 1:
            print(matrix[i][j], end=" ")
        print(end=" ")
        print(end=" ")
    print()
print("-------------")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if (i + j) % 2 == 0:
            print(f"{matrix[i][j]:>2}", end=" ")
        else:
            print(" " * 2, end=" ")
    print()
print("-------------")
for i in range(len(matrix)):
    row = matrix[i]
    if i % 2 == 1:
        row = reversed(row)
    for el in row:          # remove this line
        print(el, end=" ")  # print(*row)
    print()
print("-------------")
rows, cols = len(matrix), len(matrix[0])
for s in range(rows + cols - 1):
    for i in range(rows):
        j = s - i
        if 0 <= j < cols:
            print(matrix[i][j], end=" ")
    print()
print("-------------")
for j in range(len(matrix[0])):
    if j % 2 == 0:
        for i in range(len(matrix)):
            print(matrix[i][j], end=" ")
    else:
        for i in range(len(matrix)-1, -1, -1):
            print(matrix[i][j], end=" ")
    print()