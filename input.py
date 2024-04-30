# Entrada de Dados
aluno = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
falta = int(input('Digite a quantidade de falta: '))
media = (nota1+nota2+nota3) /3
print('Aluno: ' + aluno)
print('Media: ' + str (media))
print('Falta(s): ' + str(falta))

