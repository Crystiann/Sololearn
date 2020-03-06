#simple hanoi game using recursion

print('f is from\nh is helper\nt is target\n')

def move(f, t):
    print(f'Move {f} to {t}')

def hanoi(n, f, h, t):
    if n == 0:
        pass
    else:
        hanoi(n-1, f, t, h)
        move(f, t)
        hanoi(n-1, h, f, t)

hanoi(4, 'A', 'B', 'C')
