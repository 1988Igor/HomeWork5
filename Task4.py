#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from dataclasses import replace

def encode(message):
    encoded_message = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        letter = message[i]
        j = i
        while (j < len(message)-1):
            if (message[j] == message[j+1]):
                count = count+1
                j = j+1
            else:
                break
        encoded_message=encoded_message+str(count)+letter
        i = j+1
    return encoded_message
with open('file2.txt', 'w') as cb:
    cb.write('ABBBCCCCCCCCAB')
lst = open('file2.txt' ,'r') .read().split()
lst = str(lst).replace('[', '').replace(']', '').replace('"','').replace("'", '')
print(f'The message from file2.txt message: {lst}')
#The message from file.txt message: ABBBCCCCCCCCAB
encoded_message = encode(str(lst))
with open('file2.txt', 'a+') as data:
    data.write('\n' + encoded_message )
print(f'The encoded message is:{encoded_message}')
#The encoded message is:1A3B8C1A1B

