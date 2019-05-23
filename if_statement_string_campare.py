def string_campare(str_1, str_2):
    if type(str_1) is str and type(str_2) is str:
        if str_1 == str_2:
            return 1
        elif str_1 != str_2 and len(str_1) > len(str_2): # вопрос, можно ли здесь использовать просто if ?
            return 2
        elif str_1 != str_2  and str_2 == 'learn':
            return 3
    else:
        return 0

print(string_campare(1, 1))
print(string_campare(1, 'a'))
print(string_campare('a', 1))
print(string_campare('a', 'a'))
print(string_campare('as', 'a'))
print(string_campare('a', 'learn'))