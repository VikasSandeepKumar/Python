# Matrix Addition using Nested Loop
X = [[1,2,3],
     [4,5,6],
     [7,8,9]]

Y = [[9,8,7],
     [6,5,4],
     [3,2,1]]

Nested_Loop = [[0,0,0,],
          [0,0,0],
          [0,0,0]]

Nested_Loop = [[X[i][j] - Y[i][j]]
          for j in range(len(X[0]))
for i in range(len(X))]


for r in Nested_Loop:
    print(r)

# Matrix Addition using Nested List Comprehension

X = [[12,7,3],
     [4,5,6],
     [7,8,9]]
Y = [[5,8,1],
     [6,7,3],
     [4,5,9]]

Nested_List = [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
for z in Nested_List:
    print(z)