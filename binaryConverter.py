
print('\nBinary converter (8 bit)')

number = int(input('\nInput a number to be converted: '))

binary = [0,0,0,0,0,0,0,0]
binary_val = [128,64,32,16,8,4,2,1]

for i in range(8):
    if(binary_val[i] <= number):
        binary[i] = 1
        number = number - binary_val[i]
        if number == 0:
            break

b = ' '.join(str(x) for x in binary)

print('The binary value is -> ' , b)