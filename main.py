def math(first_n, second_n):
    first_n_reverse = first_n[len(first_n) - 1::] + first_n[1:len(first_n) - 1:] + first_n[0:1:]  # перевернутое 1 число
    print('Первое перевернутое число:', int(first_n_reverse))
    second_n_reverse = second_n[len(second_n) - 1::] + second_n[1:len(second_n) - 1:] + second_n[
                                                                                        0:1:]  # перевернутое 2 число
    print('Второе перевернутое число:', int(second_n_reverse))
    return first_n_reverse, second_n_reverse


first_n = input("Введите первое число: ")
second_n = input("Введите второе число: ")

if len(first_n) < 3 or len(second_n) < 4:  # проверка ввода
    print('Некорректный ввов. Программа завершается!')
else:
    numbers = math(first_n, second_n)  # забираем два числа с функции
    summ = int(numbers[0]) + int(numbers[1])  # сумма чисел
    print('Сумма чисел: ', summ)