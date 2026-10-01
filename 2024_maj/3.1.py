import time
def make_shortcut(num: int):

    shortcut = 0
    # ...[x]


    currentOne = 1
    multiplier = 1

    while num > 0:
        digit = num % 10
    
        if digit % 2 != 0:
            shortcut += digit * multiplier
            multiplier *= 10

        num -= digit
        num //= 10
        currentOne += 1

        

    print(shortcut)

    return shortcut

x = 294762
print(f'Shortcut for {x} is {make_shortcut(x)}')