
points: list[tuple[int]] = []
points_set = set()
with open("data/dron.txt", "r") as file:
  for line in file:
 
    data = line.strip().split(' ')

    # print(linedata)
    baseX = points[-1][0] if len(points) > 0 else 0
    baseY = points[-1][1] if len(points) > 0 else 0
    point = (baseX + int(data[0]), baseY + int(data[1]))
    points.append(point)
    points_set.add(point)

# a

def check_if_inside_rectangle(point: tuple[int]):
  if (
    (point[0] <= 0 or point[0] >= 5000)
    or
    (point[1] <= 0 or point[1] >= 5000)
  ):
    return False

  return True
  

count  = 0
for point in points:
  # break optimisation since next x is always bigger
  if point[0] >= 5000:
    break

  if check_if_inside_rectangle(point):
    count += 1
    
print(count)


# b
found_triples = []
for i,point1 in enumerate(points):
  for point2 in points[i+1:]:

    distance_x_f = abs(point1[0] - point2[0]) / 2
    distance_y_f = abs(point1[1] - point2[1]) / 2
    distance_x = int(distance_x_f)
    distance_y = int(distance_y_f)

    if (distance_x_f != distance_x or distance_y_f != distance_y):
      continue

    middle = (max(point1[0], point2[0]) - distance_x, max(point1[1], point2[1]) - distance_y)
    # middle_set_hash = f'{middle[0]} {middle[1]}'
    # print(middle)
    if middle in points_set:
      found_triples.append((point1, middle, point2))
      break # "There is only one triple"

print(found_triples)


  



  
