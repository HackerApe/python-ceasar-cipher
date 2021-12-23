alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_direction = input(
    "Type 'encode' to encrypt the message, or 'decode' to decrypt the message: ")
user_text = input("Type the message: ")
user_shift = int(input('Type the shift number: '))


def ceasar(text, shift, direction):
    output = ''
    if direction == 'decode':
        shift *= -1
    for char in text:
        output += alphabet[alphabet.index(char) + shift]
    print(f'The {direction}d text is {output}')


ceasar(user_text, user_shift, user_direction)
