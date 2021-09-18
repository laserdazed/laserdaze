# Умножение длинных чисел с использованием строк. Кандаков В.И.
def multiply(num1, num2):
    len_num1 = len(num1)
    len_num2 = len(num2)

    if len_num1 == 0 or len_num2 == 0:
        return "0"

    # Записываем поразрядно в виде вектора
    result = [0]* (len_num1 + len_num2)

    index_num1 = 0

    # Цикл для смещения справа налево
    for i in range(len_num1 - 1, -1, -1):

        n1 = int(num1[i])
        transfer = 0
        index_num2 = 0

        # Цикл для смещения справа налево (2-е число)
        for j in range(len_num2 - 1, -1, -1):

            n2 = int(num2[j])
            # Умножение с учетом текущего остатка от предыдущего разряда
            temp = n1 * n2 + transfer + result[index_num1 + index_num2]

            # Сохранение остатка для следующего разряда
            transfer = temp // 10
            result[index_num1 + index_num2] = temp % 10

            index_num2 += 1

            # Перенос остатка в следующую строку
        if transfer > 0:
            result[index_num1 + index_num2] += transfer

        index_num1 += 1

    # Отбрасываем лишние нули
    k = len(result) - 1
    while k >= 0 and result[k] == 0:
        k -= 1

    final_result = ""
    while k >= 0:
        final_result += str(int(result[k]))
        k -= 1

    return final_result


if __name__ == "__main__":
    bruh = input("Введите первое число!\n")
    moment = input("Введите второе число!\n")

    if ((bruh[0] == '-' or moment[0] == '-') and
            (bruh[0] != '-' or moment[0] != '-')):
        print("-", end='')

    if bruh[0] == '-' and moment[0] != '-':
        bruh = bruh[1:]
    elif bruh[0] != '-' and moment[0] == '-':
        moment = moment[1:]
    elif bruh[0] == '-' and moment[0] == '-':
        bruh = bruh[1:]
        moment = moment[1:]

    try:
        print(f'Результат умножения:{multiply(bruh, moment)}')
    except ValueError:
        print("Ошибка - Вы ввели не число!")