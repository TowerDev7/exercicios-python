# Desafio 031 - viagem de carro
print('-='*20)
print('Vamos planejar uma viagem de carro!')
print('-='*20)
print('Viagens de até 200 km custam R$0,50 por km, e viagens maiores custam R$0,45 por km.')
print('-='*20)
dist = float(input('Qual a distância em km (quilômetros) será percorrida com o carro? '))
if dist <= 200:
  tot = dist * 0.50
  print(f'No total, a viagem custou R${tot} ao percorrer {dist} km.')
else:
  tot = dist * 0.45
  print(f'No total, a viagem custou R${tot} ao percorrer {dist} km.')
print('Obrigado por viajar conosco! Volte sempre.')
