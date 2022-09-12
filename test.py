word = input().split()
alfavit_EU_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_EU_low = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'


def smeshenie(): #Создание списка из слов без знаков препинания
    w_list = word
    for i in range(len(w_list)):
        w_list[i] = w_list[i].strip(',"!.')
    return w_list

def pas_word(j, w_list):  #Зашифровка одного слова из списка слов
    words = word[j]
    for i in words:
        step_pass = w_list[j]
        if word[i] in alfavit_EU_low:
            mesto = alfavit_EU_low.find(i)
            new_mesto = mesto - step_pass
            print(alfavit_EU_low[new_mesto], end='')
        if i in alfavit_EU_up:
            mesto = alfavit_EU_up.find(i)
            new_mesto = mesto - step_pass
            print(alfavit_EU_up[new_mesto], end='')
        if i in ' ,.?!':
            print(i, end='')

def pas_sentence():
    smeshenie()
    for j in range(len(word)):
        pas_word(j, w_list)

pas_sentence()