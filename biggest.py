print('Return the biggest word')

sentence = input('Input your sentence: ')

sentence = sentence.split(" ")

biggest = ' '

for i in range(len(sentence)):
    if len(biggest) < len(sentence[i]):
        biggest = sentence[i]

print(biggest)