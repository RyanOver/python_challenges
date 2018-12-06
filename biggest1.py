print('Return the biggest word')

sentence = input('Input your sentence: ')

sentence_char = []

for i in range(len(sentence)):
    sentence_char.append(sentence[i])

a = ';,?!#$%^&*'

for x in a:
    sentence = sentence.replace(x, '')

sentence = sentence.split(' ')

biggest = ' '

for i in range(len(sentence)):      
    if len(biggest) < len(sentence[i]):
        biggest = sentence[i]

print(biggest)
