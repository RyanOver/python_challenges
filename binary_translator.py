print('Binary translator')
sentence = input('input a sentence to be translated in : ')
sentence_ascii, sentence_char,rtn = [], [],''
for i in range(len(sentence)):
    sentence_char.append(sentence[i]) 
    sentence_ascii.append(ord(sentence[i]))
def to_binary(n):
    binary,binary_val = [0,0,0,0,0,0,0,0],[128,64,32,16,8,4,2,1]
    for i in range(len(binary)):
        if (binary_val[i] <= n):
            binary[i] = 1
            n = n - binary_val[i]
            if n == 0: break
    return ' '.join(str(x) for x in binary)
for i in sentence_ascii:
    if i == 32: rtn += '   '
    else: rtn += to_binary(i) + " "
print('The binary value is -> ' , rtn)