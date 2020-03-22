max = 10 # top end of the range 
sum = 0 # answer

for i in range(0, max):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)
