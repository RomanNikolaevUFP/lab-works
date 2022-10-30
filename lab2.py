def zero_matrix(n, m):
    b = []
    for i in range(n):
        b.append([0] * m)
    return b

def transpose(a):
    b = zero_matrix(len(a[0]), len(a))
    for i in range(len(a[0])):
        for j in range(len(a)):
            b[i][j] = a[j][i]
    return b

def multiply(a, b):
    assert len(a[0]) == len(b)
    n = len(a)
    k = len(a[0])
    m = len(b)
    c = zero_matrix(n, m)
    for i in range(n):
        for j in range(m):
            c[i][j] = 0
            for l in range(k):
                c[i][j] += a[i][l] * b[l][j]
    return c

def det2(a):
    assert len(a) == 2
    assert len(a[0]) == 2
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]

def det3(a):
    assert len(a) == 3
    assert len(a[0]) == 3
    b1 = a[0][0]*a[1][1]*a[2][2] + a[0][2]*a[1][0]*a[2][1] + a[2][0]*a[0][1]*a[1][2]
    b2 = a[2][0]*a[1][1]*a[0][2] + a[1][0]*a[0][1]*a[2][2] + a[0][0]*a[1][2]*a[2][1]
    return b1 - b2

def det(a):
    if len(a) == 1:
        return a[0][0]    
    if len(a) == 2:
        return det2(a)
    return det3(a)

def rk2(a):
    assert len(a) == 2
    assert len(a[0]) == 2
    if det(a) != 0:
        return 2
    if a[0][0] != 0 or a[0][1] != 0 or a[1][0] != 0 or a[1][1] != 0:
        return 1
    return 0
    
def minor(a, row, col):
    b = zero_matrix(len(a) - 1, len(a[0]) - 1)
    for i in range(row):
        for j in range(col):
            b[i][j] = a[i][j]
        for j in range(col, len(b[0])):
            b[i][j] = a[i][j+1]
    for i in range(row, len(b)):
        for j in range(col):
            b[i][j] = a[i+1][j]
        for j in range(col, len(b[0])):
            b[i][j] = a[i+1][j+1]
    return b

def rk3(a):
    assert len(a) == 3
    assert len(a[0]) == 3
    if det(a) != 0:
        return 3
    r = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            m = minor(a, i, j)
            r = max(r, rk2(m))
    return r    

def rk(a):
    if len(a) == 2:
        return rk2(a)
    return rk3(a)

def inverse(a):
    d = det(a)
    assert d != 0
    im = zero_matrix(len(a), len(a[0]))
    for i in range(len(a)):
        for j in range(len(a[0])):
            im[i][j] = det(minor(a, j, i)) * (-1 if (i + j) % 2 == 1 else 1) / d
    return im

print("Программа для работы с матрицами")
print("-----")
f = 1
while True:
    if f == 1:
        print()
        print("Введите код математической операции с матрицей (матрицами), введите -1 для перехода к вычислениям с помощью библиотеки numpy или введите любое другое число для выхода из программы:")
        print()
        print("1 - Транспонировать матрицу;")
        print("2 - Умножить матрицы друг на друга;")
        print("3 - Определить ранг матрицы (только для матриц 2x2 и 3x3);")
        print("4 - Вычислить обратную матрицу (только для матриц 2x2 и 3x3)")
        print()
        o = int(input("Код операции: "))
        if o < -1 or o == 0 or o > 4:
            break
    if o == 1:
        while True:
            n = int(input("Введите длину строки (количество столбцов) в матрице: "))
            a = list(map(float, input("Введите элементы матрицы последовательно, считывая строки слева направо. Для разделения элементов используйте пробелы: ").split()))
            if len(a) % n != 0:
                print()
                print("Ошибка! Матрица задана неверно, попробуйте ещё раз")
                print()
                continue
            else:
                a = [a[i:i + n] for i in range(0, len(a), n)]
                if f == 1:
                    a = transpose(a)
                    print()
                    for i in range(len(a)):
                        print(a[i])
                    break
                else:
                    b = np.array(a)
                    b = b.transpose()
                    print()
                    print(b)
                    print()
                    print("P. S. Сравним производительность написанной функции и библиотеки numpy с помощью библиотеки timeit, выяснив время, затраченное на 10000 вычислений:")
                    c = ti.timeit("transpose(a)", number=10000, globals={"transpose":transpose, "a":a})
                    d = ti.timeit("b.transpose()", number=10000, globals={"transpose":transpose, "b":b})
                    print("Написанная функция: ", c, "секунды")
                    print("Библиотека numpy: ", d, "секунды")
                    if c > d:
                        print("Вывод: библиотека numpy быстрее в", c / d, "раза")
                    elif c == d:
                        print("Вывод: производительность одинакова")
                    else:
                        print("Вывод: написанная функция быстрее в", d / c, "раза")
                    o = -1
                    break
    elif o == 2:
        while True:
            n1 = int(input("Введите длину строки (количество столбцов) в матрице A: "))
            a = list(map(float, input("Введите элементы матрицы последовательно, считывая строки слева направо. Для разделения элементов используйте пробелы: ").split()))
            if len(a) % n1 != 0:
                print()
                print("Ошибка! Матрица задана неверно, попробуйте ещё раз")
                print()
                continue
            else:
                while True:
                    n2 = int(input("Введите длину строки (количество столбцов) в матрице B: "))
                    b = list(map(float, input("Введите элементы матрицы последовательно, считывая строки слева направо. Для разделения элементов используйте пробелы: ").split()))
                    if len(b) % n2 != 0:
                        print()
                        print("Ошибка! Матрица задана неверно, попробуйте ещё раз")
                        print()
                        continue
                    else:
                        break
                a = [a[i:i + n1] for i in range(0, len(a), n1)]
                b = [b[i:i + n2] for i in range(0, len(b), n2)]
                if n1 != len(b):
                    print()
                    print("Ошибка! Количество столбцов в матрице A не совпадает с количеством строк в матрице B.")
                    print()
                    break
                else:
                    if f == 1:
                        c = multiply(a,b)
                        print()
                        for i in range(len(c)):
                            print(c[i])
                        break
                    else:
                        c = np.array(a)
                        d = np.array(b)
                        print()
                        print(c.dot(d))
                        print()
                        print("P. S. Сравним производительность написанной функции и библиотеки numpy с помощью библиотеки timeit, выяснив время, затраченное на 10000 вычислений:")
                        e = ti.timeit("multiply(a,b)", number=10000, globals={"multiply":multiply, "a":a, "b":b})
                        g = ti.timeit("c.dot(d)", number=10000, globals={"c":c, "d":d})
                        print("Написанная функция: ", e, "секунды")
                        print("Библиотека numpy: ", g, "секунды")
                        if e > g:
                            print("Вывод: библиотека numpy быстрее в", e / g, "раза")
                        elif e == g:
                            print("Вывод: производительность одинакова")
                        else:
                            print("Вывод: написанная функция быстрее в", g / e, "раза")
                        o = -1
                        break
    elif o == 3:
        while True:
            n = int(input("Введите длину строки (количество столбцов) в матрице: "))
            a = list(map(float, input("Введите элементы матрицы последовательно, считывая строки слева направо. Для разделения элементов используйте пробелы: ").split()))
            if len(a) % n != 0:
                print()
                print("Ошибка! Матрица задана неверно, попробуйте ещё раз")
                print()
                continue
            else:
                a = [a[i:i + n] for i in range(0, len(a), n)]
                if f == 1:
                    if (n == 2 and len(a) == 2) or (n == 3 and len(a) == 3):
                        print()
                        print("Ранг матрицы:", rk(a))
                        break
                    else:
                        print()
                        print("Предупреждение! Задана матрица с недопустимой для написанных функций размерностью. Ранг заданной матрицы будет определён с помощью библиотеки numpy.")
                        import numpy as np
                        import numpy.linalg as la
                        f = -1
                if f == -1:
                    b = np.array(a)
                    print()
                    print("Ранг матрицы:", la.matrix_rank(b))
                    if (n == 2 and len(a) == 2) or (n == 3 and len(a) == 3):
                        print()
                        print("P. S. Сравним производительность написанной функции и библиотеки numpy с помощью библиотеки timeit, выяснив время, затраченное на 10000 вычислений:")
                        c = ti.timeit("rk(a)", number=10000, globals={"rk":rk, "a":a})
                        d = ti.timeit("la.matrix_rank(b)", number=10000, globals={"la":la, "b":b})
                        print("Написанная функция: ", c, "секунды")
                        print("Библиотека numpy: ", d, "секунды")
                        if c > d:
                            print("Вывод: библиотека numpy быстрее в", c / d, "раза")
                        elif c == d:
                            print("Вывод: производительность одинакова")
                        else:
                            print("Вывод: написанная функция быстрее в", d / c, "раза")
                    o = -1
                    break
    elif o == 4:
        while True:
            n = int(input("Введите длину строки (количество столбцов) в матрице: "))
            a = list(map(float, input("Введите элементы матрицы последовательно, считывая строки слева направо. Для разделения элементов используйте пробелы: ").split()))
            if len(a) % n != 0:
                print()
                print("Ошибка! Матрица задана неверно, попробуйте ещё раз")
                print()
                continue
            else:
                a = [a[i:i + n] for i in range(0, len(a), n)]
                if f == 1:
                    if (n == 2 and len(a) == 2) or (n == 3 and len(a) == 3):
                        a = inverse(a)
                        print()
                        for i in range(len(a)):
                            print(a[i])
                        break
                    else:
                        print()
                        print("Предупреждение! Задана матрица с недопустимой для написанных функций размерностью. Обратная матрица будет вычислена с помощью библиотеки numpy.")
                        import numpy as np
                        import numpy.linalg as la
                        f = -1
                if f == -1:
                    b = np.array(a)
                    b = la.inv(b)
                    print()
                    print(b)
                    if (n == 2 and len(a) == 2) or (n == 3 and len(a) == 3):
                        print()
                        print("P. S. Сравним производительность написанной функции и библиотеки numpy с помощью библиотеки timeit, выяснив время, затраченное на 10000 вычислений:")
                        c = ti.timeit("inverse(a)", number=10000, globals={"inverse":inverse, "a":a})
                        d = ti.timeit("la.inv(b)", number=10000, globals={"la":la, "b":b})
                        print("Написанная функция: ", c, "секунды")
                        print("Библиотека numpy: ", d, "секунды")
                        if c > d:
                            print("Вывод: библиотека numpy быстрее в", c / d, "раза")
                        elif c == d:
                            print("Вывод: производительность одинакова")
                        else:
                            print("Вывод: написанная функция быстрее в", d / c, "раза")
                    o = -1
                    break
    elif o == -1:
        import numpy as np
        import numpy.linalg as la
        import timeit as ti
        print()
        print("При помощи библиотеки numpy:")
        print()
        print("1 - Транспонировать матрицу;")
        print("2 - Умножить матрицы друг на друга;")
        print("3 - Определить ранг матрицы;")
        print("4 - Вычислить обратную матрицу")
        print()
        print("Введите код математической операции с матрицей (матрицами), введите -1, чтобы вернуться обратно, или введите любое другое число для выхода из программы.")
        print()
        o = int(input("Код операции: "))
        if o < -1 or o == 0 or o > 4:
            break
        elif o == -1:
            f = 1
            continue
        else:
            f = -1
            continue
