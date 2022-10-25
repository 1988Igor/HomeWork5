#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint

def input_data(name):
    x = int(input(f"{name}, how much candies (from 1 to 28)  do you want to take : "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, how much candies (from 1 to 28) do you want to take : "))
    return x

def data_player(name, candies_numbers, curent_balance, Total_candies):
    print(f" {name} tooks {candies_numbers} candies, now he has {curent_balance} candies. On the table we have {Total_candies} candies.")

player1 = input("Enter the name of first player: ")
player2 = input("Enter the name of second player: ")
Total_candies = randint(100,130)
print(f'Dear players, we have {Total_candies} candies')
first_mover = randint(0, 2)  

if first_mover:
    print(f"First move {player1}")
else:
    print(f"First move {player2}")

curent_balance1 = 0
curent_balance2 = 0

while Total_candies > 28:
    if first_mover:
        candy_numbers = input_data(player1)
        curent_balance1 += candy_numbers
        Total_candies -= candy_numbers
        first_mover = False
        data_player(player1, candy_numbers, curent_balance1, Total_candies)
    else:
        candy_numbers = input_data(player2)
        curent_balance2 += candy_numbers
        Total_candies -= candy_numbers
        first_mover = True
        data_player(player2, candy_numbers, curent_balance2, Total_candies)

if first_mover:
    print(f"Congrutulations {player1}, you are the winner!!!")
else:
    print(f"Congrutulations {player2}, you are the winner!!!")