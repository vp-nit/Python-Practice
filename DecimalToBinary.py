#Finding Binary code for any given Decimal Integer:

def decimalToBinary(num):
    binary = []
    while num > 1:
        div = divmod(num,2)
        num = div[0]
        binary.append(div[1])
    binary.append(div[0])
    return binary[::-1]

number = input('Please enter a number: ')
bin_num = decimalToBinary(int(number))
print(bin_num)