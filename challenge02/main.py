# Author: Ec25
def recorrer_cadena(value:int, charset:str):
    output = ''

    for letter in charset:
        if letter == '#':
            value += 1

        elif letter == '@':
            value -= 1

        elif letter == '*':
            value *= value

        elif letter == '&':
            output += str(value)

        else:
            exit('Input Fail...')

    return output


if __name__ == '__main__':
    value = 0
    charset = input('Input: ')
    output = recorrer_cadena(value, charset)
    print(f'Output: {output}')