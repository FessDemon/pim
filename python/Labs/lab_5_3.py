import numpy as np

mass = np.array([[4, 5, 6], [2, 9, 0], [4, 0, 7]])
print(mass)

# Для первого условия
print("количество строк, не содержащих ни одного нулевого элемента")
print(sum(0 not in x for x in mass))

# Для второго условия
print(
    "максимальное значение из чисел, встречающихся в заданной матрице более одного раза"
)
print(max([x for i in [[x for a in mass for x in a]] for x in i if i.count(x) > 1]))
