a=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]

 for i in range(len(a)):
     for j in range(len(a[i])):
         if i==j:


print(a[i][j])

primary_diagonal=0
for i in range(len(a)):
    for j in range(len(a[i])):
        if i==j:
            primary_diagonal=primary_diagonal+a[i][j]


print(primary_diagonal)

# Reverse diagonal Multiplication

# a=[[12,56,38,49],
#    [15,47,32,72],
#    [52,43,27,16],
#    [89,75,96,25]]
# n=4
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if j == (n-1):
#             print(a[i][j])
#
# sum=0
# n=4
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if j ==(n-i-1):
#             sum = sum+a[i][j]