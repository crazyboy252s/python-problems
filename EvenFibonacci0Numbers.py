for i in range(100):
    x=0
    y=1
    for _ in range(i):
        x, y = y, x + y
    print(x)