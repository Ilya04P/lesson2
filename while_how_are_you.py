def ask_user():
    ask = input('Как дела? ')
    while ask != 'Хорошо':
        ask = input('Как дела? ')

if __name__ == '__main__':
    ask_user()
