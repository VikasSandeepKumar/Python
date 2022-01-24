# def pypart(n):
#     for i in range(0, n):
#         for j in range(0, i+1):
#             print("* ", end="")
#             print("\r")
# n=5
# pypart(n)

rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")

# Program to print half pyramid a using numbers

rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end="")
    print("\n")

# Program to print half pyramid using alphabets

rows = int(input("Enter number of rows: "))

ascii_value = 65
for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")

    ascii_value += 1
    print("\n")