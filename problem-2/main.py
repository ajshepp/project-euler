MAX = 4000000
fib_low = 1
fib_high = 2
sum = 0

while fib_low < MAX:

    # check to add to sum
    if fib_low % 2 == 0:
        sum += fib_low

    # update fib numbers
    temp = fib_high
    fib_high += fib_low
    fib_low = temp

print(sum)