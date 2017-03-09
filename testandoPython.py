#inserindo informações para realização de teste de funcionalidade da linguagem
nome = input('What your name?')
sobrenome = input('What your segund name?')
idade = input('How yeard old?')
# Trocando string por int
intidade = int(idade)
# Informando com variaveis e formado de numero
print('Hello ' + nome + ' ' + sobrenome + \
    ' , {0:d} years old'.format(intidade))
