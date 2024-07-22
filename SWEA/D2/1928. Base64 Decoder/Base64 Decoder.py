sequence = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def binary_six(decimal):
    six = ''
    
    for i in range(1, 7):
        if decimal % (2 ** (6 - i)) != decimal:
            decimal = decimal - (2 ** (6 - i))
            six += '1'
        else:
            six += '0'

    return six

def decimal_eight(binary):
    attach = '0b' + binary
    print(chr(int(attach, 2)), end="")

T = int(input())

for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    encoding_string = input()

    binary_string = ''
    decoding_string = ''

    for i in encoding_string:
        binary_string += binary_six(sequence.find(i))

    for j in range(0, len(binary_string), 8):
        decimal_eight(binary_string[j:j+8])
    print()
