
print('\nSearch and replace or destroy\n')

def search_and_destroy():
    sentence = input('Enter your sentence: ')
    find = input('Enter the word to replace: ')
    found = False
    sentence = sentence.split(' ')
    print(len(sentence))
    for i in range(len(sentence)):
        if find == sentence[i]:
            found = True
            sentence.pop(i)
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
    for x in range(len(sentence)):
        if find == sentence[x]:
            found = True
            sentence.pop(x)
            sentence[x] = replc
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
