#desafio 2: Classificador de ranqueadas
import random

def ranked_results():
    vitoria = random.randint(0,200)
    derrota = random.randint(0, 200)
    return abs(vitoria - derrota)

def ranking_game():
    nivel = ['Ferro', 'Bronze', 'Prata', 'Ouro', 'Platina', 'Ascendente', 'Imortal']
    saldo_vitorias = ranked_results()

    if saldo_vitorias < 10:
        print(f'O Herói tem de saldo de Vitorias de **{saldo_vitorias}** está no nível **{nivel[0]}**')
    elif saldo_vitorias > 11  and saldo_vitorias < 20:
        print(f'O Herói tem de saldo de Vitorias de **{saldo_vitorias}** está no nível **{nivel[1]}**')
    elif saldo_vitorias > 21 and saldo_vitorias < 50:
        print(f'O Herói tem de saldo de Vitorias de **{saldo_vitorias}** está no nível **{nivel[2]}**')
    elif saldo_vitorias > 51 and saldo_vitorias < 80:
        print(f'O Herói tem de saldo de Vitorias de **{saldo_vitorias}** está no nível **{nivel[3]}**')
    elif saldo_vitorias > 81 and saldo_vitorias < 90:
        print(f'O Herói tem de saldo de Vitorias de **{saldo_vitorias}** está no nível **{nivel[4]}**')
    elif saldo_vitorias > 91 and saldo_vitorias < 100:
        print(f'O Herói tem de saldo de Vitorias de **{saldo_vitorias}** está no nível **{nivel[5]}**')
    elif saldo_vitorias > 101:
        print(f'O Herói tem de saldo de Vitorias de **{saldo_vitorias}** está no nível **{nivel[6]}**')

ranking_game()

