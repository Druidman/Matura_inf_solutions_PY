def p(n):
  save_n = n
  r = n % 100 # last two digits
  a = r // 10 # decimals
  b = r % 10  # ones
  n = n//100  # removal of last two digits so decimals with ones

  if n > 0:
    w = a + (10*b) + (100*p(n))
  else:
    if a > 0:
      w = a + (10*b)
    else:
      w = b
  print(f'Called for n: {save_n} with w of: {w}')
  return w


print(p(998877665544321))