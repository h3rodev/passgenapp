import random


def genPass(c):

    chars = [
        ['@', '#', '$', '%'],

        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],

        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],

        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],

        ['{', '}', '[', ']',
         '(', ')', '/', '\', ''', '"', '`', '~', ',', ':', '.', '<', '>']
    ]

    i = 0
    passgen = ''
    while i < c:
        passgen += charandom(chars)
        i += 1

    return passgen


def charandom(a):
    ranchar = random.randint(0, 4)
    ranum = random.randrange(0, len(a[ranchar]))
    return a[ranchar][ranum]
