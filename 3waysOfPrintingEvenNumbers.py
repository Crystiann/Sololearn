# 3 ways of printing even numbers

# First
for n in range(21):
    if n%2 == 0:
        print(n)
    n+=1

# Second
x = 0
while x < 21:
    if x%2 == 0:
        print(x)
    x+=1

# Third - this is not recommended
for y in range(0, 21, 2):
    print(y)
