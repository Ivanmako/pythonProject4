word = input()
alfavit_EU_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_EU_low = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
def smeshenie(word): #Создание сптска из слов без знаков препинания
    w_list = word.split()
    for i in range(len(w_list)):
        w_list[i] = w_list[i].strip(',"!.')
        return w_list

def pas():
    smeshenie(word)
    for i in word:
        step_pass = word_list[i]
        if i in alfavit_EU_low:
            mesto = alfavit_EU_low.find(i)
            new_mesto = mesto - step_pass
            print(alfavit_EU_low[new_mesto], end='')
        if i in alfavit_EU_up:
            mesto = alfavit_EU_up.find(i)
            new_mesto = mesto - step_pass
            print(alfavit_EU_up[new_mesto], end='')
        if i in ' ,.?!':
            print(i, end='')
