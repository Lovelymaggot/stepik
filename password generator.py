import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''
print('Приветствую тебя мой дорогой друг в генераторе паролей')
n = int(input('Сколько паролей вам нужно сгенерировать? '))
length = int(input('Какой длины должен быть пароль? '))
pwd_digits = input('Включать ли в пароль цифры от 0 до 9? да/нет:  ')
if pwd_digits.lower() == 'да':
    chars += digits
pwd_uppercase = input('Включать ли в пароль прописные буквы? да/нет:  ')
if pwd_uppercase.lower() == 'да':
    chars += uppercase_letters
pwd_lowercase = input('Включать ли в пароль строчные буквы? да/нет:  ')
if pwd_lowercase.lower() == 'да':
    chars += lowercase_letters
pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? да/нет:  ')
if pwd_punctuation.lower() == 'да':
    chars += punctuation
pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? да/нет:  ')
if pwd_exceptions.lower() == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password

for i in range(n):
    generate_password(length, chars)
    print('Ваш пароль: ')
    print(generate_password(length, chars))