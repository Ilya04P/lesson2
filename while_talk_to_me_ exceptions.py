asked_question = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}

def ask_user(questions):
    if type(questions) is dict:
        while True:
            try:
                asks = input('Пользователь: ')
                for ask, answer in questions.items():
                    if asks == ask:
                        print('Программа: {}'.format(answer))
            except KeyboardInterrupt:
                print('Пока')
                break           

if __name__ == '__main__':
    ask_user(asked_question)
