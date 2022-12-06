import copy
class MyError(Exception):
    def __init__(self, error):
        self.error = error


def get_matrix():
    matrix = []
    num = "0123456789"
    while True:
        try:
            size = input("Enter size of matrix:\n> ")
            size = size.split(sep=" ")
            if len(size) > 2 or len(size) < 2 or str(size[0]) not in num or str(size[1]) not in num:
                raise MyError(f'Incorrect input!\nYou should enter the size, like "3 3", "4 4", etc.\n')
            break
        except MyError as err:
            print(err)
        except Exception as err:
            print(err)

    print("Enter matrix:")
    for z in range(int(size[0])):
        while True:
            try:
                elem = input("> ")
                elem = elem.split(sep=" ")
                if int(len(elem)) > int(size[1]) or int(len(elem)) < int(size[1]):
                    raise MyError(f'You should enter only {size[1]} numbers in line!')
                else:
                    matrix.append(elem)
                    break
            except MyError as no:
                print(no)
    int_matrix = []
    list_m = []
    for c in range(int(size[0])):
        for x in matrix[c]:
            i = float(x)
            list_m.append(i)
        int_matrix.append(list_m)
        list_m = []
    return int_matrix


def add_mat():
    int_matrix_a = get_matrix()
    int_matrix_b = get_matrix()
    if len(int_matrix_a[0]) != len(int_matrix_b[0]) or len(int_matrix_a) != len(int_matrix_b):
        print("The operation cannot be performed.(Операція не може бути виконана.)")
        print("The size of the second matrix must be the same as size of the first matrix! "
              "(Розмір другої матриці повинен бути таким самим, як розмір першої матриці!)")
    else:
        print("The result is (Резульат):")
        for i in range(len(int_matrix_b)):
            k = 0
            for x in int_matrix_a[i]:
                x += int_matrix_b[i][k]
                print(int(x), end=" ")
                k += 1
            print()


def multiply_con():
    int_matrix = get_matrix()
    while True:
        try:
            cons = float(input("Enter constant:\n> "))
            break
        except ValueError:
            print("Incorrect input! You must enter a number and only one.(Невірне введення! Ви повинні ввести число "
                  "і тільки одне.)")
    print("The result is (Резульат) :")
    for i in range(len(int_matrix)):
        for x in int_matrix[i]:
            x *= cons
            print(x, end="  ")
        print()


def multiply():
    int_matrix_a = get_matrix()
    int_matrix_b = get_matrix()
    result = []
    for i in range(len(int_matrix_a)):
        string = []
        for d in range(len(int_matrix_b[0])):
            number = 0
            for k in range(len(int_matrix_a[0])):
                number += int_matrix_a[i][k] * int_matrix_b[k][d]
            string.append(number)
        result.append(string)

    print("The result is (Резульат):")
    for i in range(len(result)):
        for x in result[i]:
            print(int(x), end=" ")
        print()


def transpose():
    print("""1. Main diagonal 2. Side diagonal 3. Vertical line 4. Horizontal line""")

    while True:
        try:
            good = "1234"
            choice_t = input("\nEnter your choice: 1, 2, 3 or 4:\n> ")
            if choice_t not in good:
                raise MyError("Incorrect input, try again (Спробуйте знову)")
            break
        except MyError as no:
            print(no)

    int_matrix = get_matrix()

    result = []
    for i in range(len(int_matrix)):
        string = []
        for d in range(len(int_matrix[0])):
            number = 0
            for k in range(1):
                number += int_matrix[d][i]
            string.append(number)
        result.append(string)

    print("The result is (Резульат):")
    if choice_t == "1":
        for i in range(len(result)):
            for x in result[i]:
                print(int(x), end=" ")
            print()

    elif choice_t == "2":
        for c in range(len(result)):
            result[c].reverse()
        result.reverse()
        for i in range(len(result)):
            for x in result[i]:
                print(int(x), end=" ")
            print()

    elif choice_t == "3":
        for c in range(len(int_matrix)):
            int_matrix[c].reverse()
        for i in range(len(int_matrix)):
            for x in int_matrix[i]:
                print(int(x), end=" ")
            print()

    elif choice_t == "4":
        int_matrix.reverse()
        for i in range(len(int_matrix)):
            for x in int_matrix[i]:
                print(int(x), end=" ")
            print()


def determinant(i_m):
    result = 0
    sign_1 = 1
    if len(i_m) == 1:
        result += i_m[0][0]
    elif len(i_m) == 2:
        result += i_m[0][0] * i_m[1][1] - i_m[1][0] * i_m[0][1]
    elif len(i_m) == 3:
        result += i_m[0][0] * (i_m[1][1] * i_m[2][2] - i_m[2][1] * i_m[1][2]) - i_m[0][1] * (
            i_m[1][0] * i_m[2][2] - i_m[2][0] * i_m[1][2]) + i_m[0][2] * (i_m[1][0] * i_m[2][1] - i_m[2][0] * i_m[1][1])
    else:
        for j in range(len(i_m)):
            m_1 = copy.deepcopy(i_m)
            if len(i_m) > 4:
                del m_1[0]
                for i in range(len(m_1)):
                    del m_1[i][j]

            sign = 1
            det = 0
            for b in range(len(m_1)):
                m = copy.deepcopy(m_1)
                del m[0]
                for i in range(len(m)):
                    del m[i][b]

                det += (sign * m_1[0][b]) * (
                        m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1] -
                        m[0][2] * m[1][1] * m[2][0] - m[0][0] * m[1][2] * m[2][1] - m[0][1] * m[1][0] * m[2][2])
                if sign == 1:
                    sign = -1
                else:
                    sign = 1
            if len(i_m) > 4:
                result += det * (sign_1 * i_m[0][j])
                if sign_1 == 1:
                    sign_1 = -1
                else:
                    sign_1 = 1
            else:
                result += det
                break
    return result


def minor(a, i, j):
    m = copy.deepcopy(a)
    del m[i]
    for b in range(len(m)):
        del m[b][j]
    return m


def inverse(m, det):
    trans_m = []
    for i in range(len(m)):
        string = []
        for j in range(len(m[0])):
            number = 0
            for k in range(1):
                number += int(m[j][i])
            string.append(number)
        trans_m.append(string)
    result = []
    if len(trans_m) == 1:
        result += trans_m[0][0]
    elif len(trans_m) == 2:
        result += [[trans_m[1][1], trans_m[1][0] * (-1)], [trans_m[0][1] * (-1), trans_m[0][0]]]
    elif len(trans_m) == 3:
        sign = 1
        for s in range(len(trans_m)):
            string = []
            for c in range(len(trans_m[0])):
                mn = minor(trans_m, s, c)
                calc = round((((mn[0][0] * mn[1][1] - mn[1][0] * mn[0][1]) * sign) / det), 2)
                if calc == 0.0 or calc == -0.0:
                    calc = 0
                if sign == 1:
                    sign = -1
                else:
                    sign = 1
                string.append(calc)
            result.append(string)
    else:
        for s in range(len(trans_m)):
            if s % 2 == 1:
                sign = -1
            else:
                sign = 1
            string = []
            for c in range(len(trans_m[0])):
                mn = minor(trans_m, s, c)
                calc = round((((determinant(mn)) * sign) / det), 2)
                if calc == 0.0 or calc == -0.0:
                    calc = 0
                if sign == 1:
                    sign = -1
                else:
                    sign = 1
                string.append(calc)
            result.append(string)
    for i in range(len(result)):
        for x in result[i]:
            print(x, end=" ")
        print()



while True:
    try:
        print("""\n
1. Add matrices (Додати матрицю)
2. Multiply matrix by a constant (Помножити матрицю на константу)
3. Multiply matrices (Множення матриць)
4. Transpose matrix (Транспонувати матрицю)
5. Calculate a determinant (Обчисліть визначник)
6. Inverse matrix (Обернена матриця)
0. Exit""")

        choice = input("\nEnter your choice: 1, 2, 3, 4, 5, 6 or 0:\n> ")

        if choice == "1":
            print("ATTENTION! The size of the two matrices must be the same!(Розмір двох матриць повинен бути однаковим"
                  "!)")
            add_mat()
        elif choice == "2":
            multiply_con()
        elif choice == "3":
            multiply()
        elif choice == "4":
            transpose()
        elif choice == "5":
            matrix = get_matrix()
            print("The result is (Результат):")
            print(int(determinant(matrix)))
        elif choice == "6":
            matrix = get_matrix()
            d = determinant(matrix)
            if d == 0:
                print("This matrix doesn't have an inverse (Ця матриця не має оберненої матриці)")
            else:
                print("The result is (Результат):")
                inverse(matrix, d)
        elif choice == "0":
            print("Have a nice day!")
            break
        else:
            raise MyError("Incorrect input, try again.(Невірно введено, повторіть спробу.)")
    except MyError as inc:
        print(inc)


