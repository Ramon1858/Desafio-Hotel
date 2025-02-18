#desfaio de criar um sistema de cadastro  de hotel e informar o preço com e sem desconto
simples = 100
duplo = 150
luxo = 250
cliente = input('digite seu nome completo:')
print('seja muito bem vindo ao moon palace',cliente)
idade = input('por favor,digite sua idade:')
print('nós temos três tipos de quartos o simples de 100 reais por noite,o duplo de 150 por noite e asuite de luxo de 250 por noite')
quarto = input('por favor digite o nome do quarto desejado(simples,duplo ou luxo):')
dias = int(input('por fim digite os dias que ficará hospedado:'))

if quarto == 'simples':
    valor_total = simples * dias * 0.75
    print('se for pago a vista será de',simples * dias)

elif quarto == 'duplo':
    valor_total = duplo * dias * 0.85
    print('sem seu desconto fica',duplo * dias)

elif quarto == 'luxo':
    valor_total = luxo * dias * 0.97
    print('sem seu super deconto ficaria',luxo * dias)

print(valor_total)