print('Caesar Cipher')

'''
ENCRYPTING
'''
def cipher():
        sentence = input('input a sentence to be encrypted : ')

        key = int(input('input your cipher key --> '))

        sentence_char = []
        sentence_ascii = []

        encrypted_ascii = []

        for i in range(len(sentence)):
                sentence_char.append(sentence[i])
                sentence_ascii.append(ord(sentence[i]))

        encrypted = ""

        for i in range(len(sentence_ascii)):
                if sentence_ascii[i] + key > 122:
                        a = ((sentence_ascii[i] + key) - 122) + 97 - 1
                        encrypted_ascii.append(a)
                else:
                        c = sentence_ascii[i] + key
                        encrypted_ascii.append(c)

        for i in encrypted_ascii:
                if i == (32 + key):
                        encrypted += ' '
                else:
                        encrypted += chr(i)

        print('Encrypted --> ',encrypted)

'''
DECRYPTING
'''
def decipher():
        sentence = input('input a sentence to be decrypted: ')
        key = int(input('input the key of the encryption --> '))

        sentence_char = []
        sentence_ascii = []

        encrypted_ascii = []

        for i in range(len(sentence)):
                sentence_char.append(sentence[i])
                sentence_ascii.append(ord(sentence[i]))

        decrypted = ""

        for i in range(len(sentence_ascii)):
                if  sentence_ascii[i] - key < 97:
                        a = ((sentence_ascii[i] - key) + 122) - 97 + 1
                        encrypted_ascii.append(a)
                else:
                        c = sentence_ascii[i] - key
                        encrypted_ascii.append(c)

        for i in encrypted_ascii:
                if i == (((32 - key) + 122) - 97):
                        decrypted += ' '
                else:
                        decrypted += chr(i)
        
        print('Decrypted --> ', decrypted)

def menu():
        print('\nWhat would you like to do?\n1. Encrypting \n2. Decrypting \n3. Quit\n')

        user = int(input('--> '))

        while user != 3:
                if user == 1:
                        cipher()
                        menu()
                        break
                elif user == 2:
                        decipher()
                        menu()
                        break
                elif user == 3:
                        break
                else:
                        print('This is not a valid choice')
                        menu()

menu()