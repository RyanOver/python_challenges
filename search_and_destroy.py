
print('\nSearch and replace or destroy')

def search_and_destroy():
    sentence = input('Enter your sentence: ')
    find = input('Enter the word to replace: ')
    found = False
    sentence = sentence.split(' ')
    x = 0
    for i in sentence:
        if find in i:
            found = True
            sentence.pop(x)
        x += 1
    sentence = ' '.join(sentence)
    if found == False:
        return print('Could not found the word to replace')
    else:
        return print(sentence)


def search_and_replace():
    sentence = input('Enter your sentence: ')
    find = input('Enter the word to replace: ')
    replc = input('Enter the word to be replace with: ')
    found = False
    sentence = sentence.split(' ')
    i = 0
    for x in sentence:
        if find == x:
            found = True
            sentence.pop(i)
            sentence[i] = replc
        i += 1
    sentence = ' '.join(sentence)
    if found == False:
        return print('Could not found the word to replace')
    else:
        return print(sentence)

def start():

    print('\nWhat would you like to do?\n1. Search & Destroy\n2. Search & Replace\n3. Quit\n')

    user = int(input('--> '))

    while user != 3:
        if user == 1:
            search_and_destroy()
            start()
            break
        elif user == 2:
            search_and_replace()
            start()
            break
        elif user == 3:
            break
        else:
            print('This is not a valid choice')
            start()

start()
