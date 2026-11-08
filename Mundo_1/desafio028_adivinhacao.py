# Desafio 028 - Adivinhação v1.0
from random import randint
from time import sleep
comp = randint(0, 5)
print('Olá, sou o Computador, vou pensar em um número e você tenta adivinhar!')
print('PENSANDO...')
sleep(2)
jog = int(input('Digite um valor de 0 a 5: ')
if jog == comp:
  print('Você VENCEU o jogo, parabéns!')
else:
print('Você PERDEU, tente novamente!')
