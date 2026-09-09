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

# 4 = 1 bo 2x2 czyli 2 + 2 - (1) = 3 biale, 1 czarna

# wzor: n^2 - (2n - 1)
# n^2 - 2n + 1 = (n-1)^2

a = [
  [1,0,0],
  [1,0,0],
  [1,1,1],
]

print(solve(a, 3,3))
