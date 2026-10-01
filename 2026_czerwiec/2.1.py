def check(t: list[int]):
    n = len(t)
    t.insert(0, None)

    k_s = []
    # k < n
    for k in range(1, n):

        k_base_t = t[1:k+1]
        comparer = t[n-k+1 : n + 1]
        if k_base_t == comparer:
            k_s.append(k)
    return k_s

            
x1 =  [3,5,3,5,3,5,3,5,3,5]
x2 =  [1,2,3,4]

for tab in [x1, x2]:
    print(f'Tablica: {tab} jest max {max([*check(tab), 0])}-podobna')
