height = int(input('Введите высоту: '))
for row in range(height):
    for col in range(height - row - 1, 0, -1):
        print(' ', end = '')
    for col in range(row * 2 + 1, 0, -1):
        print('#', end = '')
    print()