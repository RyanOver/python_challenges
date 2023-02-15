"""THis"""
TITLE = 'Caesar Cipher'
print(TITLE)

# TODO: Skip the spaces, leave them as 32

def cipher():
    """This function will encrypt the inputed text"""

    sentence = input('input a sentence to be encrypted : ')

    key = int(input('input your cipher key --> '))

    sentence_char = []
    sentence_ascii = []

    encrypted_ascii = []

    for i in sentence:
        sentence_char.append(i)
        sentence_ascii.append(ord(i))

    encrypted = ""

    for i in sentence_ascii:
        if i + key > 122:
            a = ((i + key) - 122) + 97 - 1
            encrypted_ascii.append(a)
        else:
            c = i + key
            encrypted_ascii.append(c)

    for i in encrypted_ascii:
        if i == (32 + key):
            encrypted += ' '
        else:
            encrypted += chr(i)

    print('Encrypted --> ', encrypted)


def decipher():
    """Decrypting"""
    sentence = input('input a sentence to be decrypted: ')
    key = int(input('input the key of the encryption --> '))

    sentence_char = []
    sentence_ascii = []

    encrypted_ascii = []

    for i in sentence:
        sentence_char.append(i)
        sentence_ascii.append(ord(i))

    decrypted = ""

    for i in sentence_ascii:
        if i == 32:
            encrypted_ascii.append(32)
        elif i - key < 97:
            a = ((i - key) + 122) - 97 + 1
            encrypted_ascii.append(a)
        else:
            c = i - key
            encrypted_ascii.append(c)
    
    print(encrypted_ascii)
    
    for i in encrypted_ascii:
        if i == 32:
            decrypted += ' '
        else:
            decrypted += chr(i)

    print('Decrypted --> ', decrypted)


def menu():
    """This is the start menu"""
    print('\nWhat would you like to do?\n1. Encrypting \n2. Decrypting \n3. Quit\n')

    user = int(input('--> '))

    while user != 3:
        if user == 1:
            cipher()
            menu()
            break
        if user == 2:
            decipher()
            menu()
            break
        if user == 3:
            exit
        print('This is not a valid choice')
        menu()

menu()
