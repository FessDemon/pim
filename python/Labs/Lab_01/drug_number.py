import datetime

start = datetime.datetime.now()

f = 0
for ch in range(1, 100_000):
    if ch != f:
        s1 = 0
        for i in range(1, ch // 2 + 1):
            if ch % i == 0:
                s1 += i
        s2 = 0
        if s1 < ch:
            for j in range(1, s1 // 2 + 1):
                if s1 % j == 0:
                    s2 += j
            if s2 == ch != s1:
                print(s1, ch)
                f = s1

finish = datetime.datetime.now()
print(finish - start)
