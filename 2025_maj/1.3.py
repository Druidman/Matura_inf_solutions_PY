def calc_value_of_w_for_n(n: int, last_sum: int):
  w = 0

  r = n % 100 # last two digits
  a = r // 10 # decimals
  b = r % 10  # ones
  n = n//100  # removal of last two digits so decimals with ones

  if n > 0:
    w = a + (10*b) + (100*last_sum)
  else:
    if a > 0:
      w = a + (10*b)
    else:
      w = b

  return w

def przestaw(n: int): 
  # w = 0
  ns = []
  while n > 0:
    ns.append(n)
    n = n // 100 # removal of last two digits

  sum = 0
  # now sum everything
  for i in range(len(ns) -1, -1, -1):
   
    sum = calc_value_of_w_for_n(ns[i], sum)
    

  return sum


    




print(f'Wynik: {przestaw(998877665544321)}')