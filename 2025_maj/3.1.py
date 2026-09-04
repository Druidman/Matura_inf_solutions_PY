import math
position_changes: list[int] = []

with open("data/dron_przyklad.txt", "r") as file:
  for line in file:
    data = line.strip().split(' ')
    # print(linedata)
    position_changes.append((int(data[0]), int(data[1])))

# biggest nwd

amount_of_gcds_bigger_than_one = 0

for x,y in position_changes:
  gcd = math.gcd(abs(x), abs(y))
  
  if gcd > 1:
    amount_of_gcds_bigger_than_one += 1

print(f'Amount: {amount_of_gcds_bigger_than_one}')