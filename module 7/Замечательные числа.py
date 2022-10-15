triple = 0
for i in range(1, 100):
    triple = (i % 10) * (i // 10) * 3
    if i == triple:
        print(i)