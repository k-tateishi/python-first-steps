for i in range(10):
    if i == 0:
        continue
    for j in range(10):
        if j == 0:
            continue
        result = i * j
        if result < 10:
            print(' ', end='')
        print(str(result), end=' ')
    print()
