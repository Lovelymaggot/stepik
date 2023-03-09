print('Добро пожаловать в шифровальщик Цезаря')
s = input('Введите текст:  ')
a = int(input('Если хотите зашифровать текст то введите 1, а если дешифровать то 2:  '))
k = int(input('Введите шаг сдвига для шифровки ( >0 ) или дешифровки ( <0 ) '))
rupper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
rlower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
result = ''
alphas = 32
for i in range(len(s)):
    if s[i].isalpha():
        if s[i] == s[i].lower():
            place = rlower.index(s[i])
        if s[i] == s[i].upper():
            place = rupper.index(s[i])
        if a == 1:
            index = (place + k) % alphas
        elif a == 2:
            index = (place-k) % alphas

        if s[i] == s[i].lower():
            print(rlower[index], end = '')
        if s[i] == s[i].upper():
            print(rupper[index], end = '')
    else:
        print(s[i], end = '')
