user_age = int(input('Введи свой возраст: '))

if 0 < user_age < 7:
    print('Ходишь в детский сад')
elif 7 <= user_age < 18:
    print('Учишся в школе')
elif 18 <= user_age < 24:
    print('Учишся в ВУЗе')
elif 24 <= user_age:
    print('Работаешь')
    if user_age >= 65:
        print('ПФР нужны твои деньги')
else:
    print('Тебя еще нет!!!')