#Desafio 1: Classificador de nível de Herói
import random

xp = random.randint(1000, 10010)
heroi = input('Digite o seu nome de Herói: ').capitalize()
nivel = ['Ferro', 'Bronze', 'Prata', 'Ouro', 'Platina', 'Ascendente', 'Imortal', 'Radiante']

if xp <= 1000:
    print(f'O Herói de nome **{heroi}** está no nível **{nivel[0]}**')
elif xp >= 1001 and xp <= 2000:
    print(f'O Herói de nome **{heroi}** está no nível **{nivel[1]}**')
elif xp >= 2001 and xp <= 5000:
    print(f'O Herói de nome **{heroi}** está no nível **{nivel[2]}**')
elif xp >= 5001 and xp <= 7000:
    print(f'O Herói de nome **{heroi}** está no nível **{nivel[3]}**')
elif xp >= 7001 and xp <= 8000:
    print(f'O Herói de nome **{heroi}** está no nível **{nivel[4]}**')
elif xp >= 8001 and xp <= 9000:
    print(f'O Herói de nome **{heroi}** está no nível **{nivel[5]}**')
elif xp >= 9001 and xp <= 10000:
    print(f'O Herói de nome **{heroi}** está no nível **{nivel[6]}**')
elif xp >= 10001:
    print(f'O Herói de nome **{heroi}** está no nível **{nivel[7]}**')