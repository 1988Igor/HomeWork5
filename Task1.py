#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
lst = ['Напишите', 'программу' , 'удаляющую', 'из','текста','все слова', 'содержащие', 'абв'  ]
find_txt = 'абв'
lst2= [i for i in lst if find_txt not in i ]
print(f'The first list: {lst} ')
print(f'The changed list: {lst2}')

