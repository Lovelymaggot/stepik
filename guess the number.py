import random
a = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')
print('Введите число от 1 до 100')
def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100
def is_valid_num():
    while True:
        n = input()
        if is_valid(n):
            return int(n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

def compare_num():
    counter = 1
    while True:
        d = is_valid_num()
        if d < a:
            counter += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif d > a:
            counter += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print(f'Количество попыток : {counter}')
            print('Хотите сыграть еще?')
            print('Ведите да или нет')
    g = input()
    while g.lower() == 'да':



compare_num()






