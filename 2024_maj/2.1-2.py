def solve(n, _amount: int = 0):
  b = 1
  c = 0
  while n > 0:
    a = n % 10
    n //= 10

    if (a % 2 == 0):
      c += b*(a // 2)
    else:
      _amount+=1
      c += b

    b *= 10
  return c, _amount

# 2.1

print(solve(33658))
print(solve(542102))
print(solve(87654321012345678))

# 2.2
print(solve(333333666666999999))


# Tf is this task xD? So easy???

