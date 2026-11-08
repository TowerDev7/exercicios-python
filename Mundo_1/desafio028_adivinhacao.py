# Desafio 028 - Adivinhação v1.0
from random import randint
from time import sleep

comp = randint(0, 5)

print('Olá, sou o computador! Vou pensar em um número de 0 a 5 e você tenta adivinhar!')
print('PENSANDO...')
sleep(2)

jog = int(input('Digite um valor de 0 a 5: ')).strip()

if jog == comp:
  print(f'Você VENCEU o jogo eu escolhi o número {comp}! Parabéns!')
else:
  print(f'Você PERDEU o jogo eu escolhi o número {comp}! Tente novamente!')
