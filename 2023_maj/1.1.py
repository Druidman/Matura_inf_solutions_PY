booksShelves: dict[int, list[int | None]] = {}



def place(i,j, bookNum):
    print(bookNum, i, j-1, max(2**i, 1))

    if i not in booksShelves:
        booksShelves[i] = [None for x in range(max(2**i, 1))]

    print(booksShelves[i])

    
    num = booksShelves[i][j-1]
    if num == None:
        booksShelves[i][j-1] = bookNum
    else:
        if bookNum < num:
            return place(i+1, 2*j - 1, bookNum)
        elif bookNum > num:
            return place(i+1, 2*j, bookNum)




books = [14, 18, 12, 9, 20, 15, 17] # to fill

for i,book in enumerate(books):
    place(0, 1, book)

print(booksShelves)

