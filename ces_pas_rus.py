word = input()
alfavit_ru_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alfavit_ru_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
smeshenie = int(input())
for j in range(0, 25)
    for i in word:
        if i in alfavit_ru_low:
            mesto = alfavit_ru_low.find(i)
            new_mesto = mesto - smeshenie
            print(alfavit_ru_low[new_mesto], end='')
        if i in alfavit_ru_up:
            mesto = alfavit_ru_up.find(i)
            new_mesto = mesto - smeshenie
            print(alfavit_ru_up[new_mesto], end='')
        if i in ' ,.?!':
            print(i, end='')
