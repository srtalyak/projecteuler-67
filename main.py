# This program is a solution for
# Project Euler Problem 67
# https://projecteuler.net/problem=67

# Find the maximum total from top to bottom in p067_triangle.txt


file = open("p067_triangle.txt", "r")
text = file.read()
file.close()
text = text.split("\n")
triangleList = list()

for row in text:
    number = row.split()
    triangleList.append(number)

for row in range(0, len(triangleList)):
    for column in range(0, row + 1):
        # converting variables from string to integer
        triangleList[row][column] = int(triangleList[row][column])

for i in range(len(triangleList) - 1, -1, -1):
    for j in range(0, i):
        # adding the largest number below the number to the number
        triangleList[i - 1][j] += max(triangleList[i][j], triangleList[i][j + 1])

print(triangleList[0][0])
