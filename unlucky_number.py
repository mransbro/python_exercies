# Loop through 1 - 20
# for 4 and 13 print 'x is unlucky'
# for even numbers, print 'x is even'
# for odd numbers, print 'x is odd'

numbers = range(1, 21)

for n in numbers:
    if n == 4 or n == 13:
        print(f"{n} is UNLUCKY!")
    elif n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")
