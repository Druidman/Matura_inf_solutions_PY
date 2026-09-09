def solve(t,n,m):
  p = [[False for i in range(m)] for x in range(n)]
  p[0][0] = True
  for i in range(n):
    for j in range(m):
      if (t[i][j] == 0):
          p[i][j] = False
      else:
        if i == 0 and j != 0:
          p[i][j] = p[i][j-1]
  
        elif j == 0 and i != 0:
          p[i][j] = p[i-1][j]
        elif j != 0 and i != 0:
          p[i][j] = p[i-1][j] or p[i][j-1]
  
    
  return p[n-1][m-1]

a1 = [
  [1,1,1],
  [0,1,0],
  [1,1,1],
]
a2 = [
  [1,1,1],
  [0,0,1],
  [1,1,1],
  [1,0,0],
  [1,1,1]
]
a3 = [
  [1,0,0,0,0],
  [1,1,0,0,1],
  [0,1,0,0,1],
  [0,1,1,1,0],
  [0,1,0,1,1],
]


print(solve(a1, 3,3))
print(solve(a2, 5,3))
print(solve(a3, 5,5))