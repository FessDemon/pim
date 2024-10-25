A = 2000
for num1 in range(3, A + 1):
    s1 = 0
    for d in range(1, num1):
        if num1 % d == 0:
            s1 += d
    for num2 in range(num1 + 1, A + 1):
        s2 = 0
        for d in range(1, num2):
            if num2 % d == 0:
                s2 += d
        if (s1 == num2) and (s2 == num1):
            print(f"Ответ: {num1}, {num2}")
