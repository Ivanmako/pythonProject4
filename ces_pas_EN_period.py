word = input()
alfavit_EU_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_EU_low = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

def pas(smeshenie):
    for i in word:
        if i in alfavit_EU_low:
            mesto = alfavit_EU_low.find(i)
            new_mesto = mesto - smeshenie
            print(alfavit_EU_low[new_mesto], end='')
        if i in alfavit_EU_up:
            mesto = alfavit_EU_up.find(i)
            new_mesto = mesto - smeshenie
            print(alfavit_EU_up[new_mesto], end='')
        if i in ' ,.?!':
            print(i, end='')

for j in range(0, 25):
    pas(j)
    print(end='\n')