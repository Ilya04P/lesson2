def get_sum(num_one, num_two):
    try:
        num_one = int(num_one)
        num_two = int(num_two)
        return num_one + num_two
    except ValueError:
        return 'NaN'

if __name__ == '__main__':
    num_one = input('Введи первое число: ')
    num_two = input('Введи второе число: ')
    print('Сумма чисел равна: ', get_sum(num_one, num_two))
    