def x(n, T, k):
    S = ['' for x in range(n+1)]
    a = n // k
    c = n -a
    for i in range(1,n+1):
        if i % k == 0:
            b = i // k
            S[n-a + b] = T[i-1]
        else:
            S[c] = T[i-1]
            c = c-1

    return S



print(''.join(x(14, "defragmentacja", 3)))
print(''.join(x(10, "tropikalny", 5)))

key = None
for i in range(1,1000):
    base = "tropikalny"
    text = ''.join(x(10, base, i))
    if base == text:
        key = i
        break

print(key)
# print(''.join(reversed('abc')))


for base in ["tropikalny", 'sigma', 'aura', 'dfsd']:
    key = None
    n = len(base)
    for i in range(1,1000):
        # base = "tropikalny"
        text = ''.join(x(n, base, i))
        if base == ''.join(reversed(text)):
            key = i
            break

    print(f'Key for {base} with n: {n}: {key}')