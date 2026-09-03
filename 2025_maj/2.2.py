
      
  

lines = []
with open("data/symbole.txt", "r") as file:
  lines = file.readlines()

lines_map = [[x for x in line.strip()] for line in lines]

box_indicies = [
  [-1,-1], [-1,0], [-1,1],
  [0,-1],  [0,0],  [0,1], 
  [1,-1],  [1,0],  [1,1], 
]

# box_indicies = [
  
#     [0,-1], [0,0],  
  
# ]
boxes = []
for row_ind, row in enumerate(lines_map):
  for col_ind, col in enumerate(row):
    
    # check items
    is_box = True
    
    for indicies in box_indicies:
        item_row = indicies[0] + row_ind
        item_col = indicies[1] + col_ind

        if (item_row >= len(lines_map) or item_row < 0):
           is_box = False
           break
        if (item_col >= len(row) or item_col < 0):
           is_box = False
          #  print('break')
           break
        
        item = lines_map[item_row][item_col]

        if item != col: 
           is_box = False
           break
    
    if is_box:
      boxes.append((row_ind + 1, col_ind+1))
      
print(f'{len(boxes)} found')
for x,y in boxes:
  print(x,' ',y)
        
