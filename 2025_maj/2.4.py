
def convert_char_to_num(char: str):
  if (char == 'o'): return 0
  elif (char == '+'): return 1
  elif (char == '*'): return 2
  else: raise Exception('Unexpected char in input')
def get_number_from_str_triple(input: str):
  number = 0
  exponent = 0
  for i in range(len(input) - 1, -1, -1):
    number += convert_char_to_num(input[i]) * pow(3, exponent)
    exponent += 1

  return number
    
  

lines = []
with open("data/symbole_przyklad.txt", "r") as file:
  lines = file.readlines()
lines = [line.strip() for line in lines]

numbers = []
for line in lines:
  number = get_number_from_str_triple(line)
  numbers.append(number)

sum_of_numbers = sum(numbers)

# putting it into triples

in_triples: str = ""

to_divide = sum_of_numbers
while to_divide != 0:
  full_three_counts = to_divide // 3
  remainder = to_divide - (full_three_counts * 3)
  to_divide = full_three_counts
  if (remainder == 0): in_triples = 'o' + in_triples
  elif (remainder == 1): in_triples = '+' + in_triples
  elif (remainder == 2): in_triples = '*' + in_triples
  else: raise Exception('Unexpected remainder value')

print (sum_of_numbers, ' ', in_triples)
  

