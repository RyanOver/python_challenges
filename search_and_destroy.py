
print('Search and replace')

def seach_and_replace_simple(sentence, find, replc):

    return print(sentence.replace(find,replc))


def seach_and_destroy(sentence, find):
    found = False
    sentence = sentence.split(' ')
    for x in range(len(sentence)):
        if find == sentence[x]:
            found = True
            sentence.pop(x)
    sentence = ' '.join(sentence)
    if found == False:
        return print('Could not found the word to replace')
    else:
        return print(sentence)


def seach_and_replace(sentence, find, replc):
    found = False
    sentence = sentence.split(' ')
    for x in range(len(sentence)):
        if find == sentence[x]:
            found = True
            sentence.pop(x)
            sentence.append(replc)
    sentence = ' '.join(sentence)
    if found == False:
        return print('Could not found the word to replace')
    else:
        return print(sentence)

def start():
    sentence = input('Enter your sentence: ')
    find = input('Enter the word to replace: ')
    replc = input('Enter the word to be replace with: ')

    seach_and_replace_simple(sentence, find, replc)
    seach_and_destroy(sentence, find)
    seach_and_replace(sentence, find, replc)

start()
