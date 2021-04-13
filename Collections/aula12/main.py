# Testando o uso de diversas coleções

from collections import Counter

texto1 = """A profissão de Analista de BI começou a se destacar devido à constante necessidade 
das empresas entenderem os dados armazenados em diversas fontes, ou seja, quando a empresa possui
dados não unificados e padronizados em um mesmo sistema.
Isso vem acontecendo, pois, dentro de uma organização é necessário um gerenciamento completo, 
que permita uma visualização geral de todas as dificuldades, ameaças, pontos fortes e oportunidades, 
que são capazes de manter a saúde do negócio, sendo aí que essa profissão se mostra fundamental.
Como o próprio nome Business Intelligence já diz, no português, Inteligência do Negócio, 
é de suma importância, que o Analista de BI entenda as métricas e as regras de negócio da área na qual estiver atuando."""

texto2 = """Antes de entrar a fundo nas diferenças entre stateless e stateful, que tal relembrar um pouco o que é widget? 
Quando criamos uma aplicação inicial com Flutter, podemos observar a estrutura de código contida no arquivo main.dart.
Rapidamente, é possível notar que existem itens que são filhos de outros itens a partir das propriedades child ou children.
Chamamos esses itens de widgets. No exemplo abaixo, repare que o widget Align tem duas propriedades: alignment e child.
Através do child é possível atribuir um filho, e esse widget filho é um elemento personalizado, criado por nós, chamado MeuWidget.
Aqui entra um ponto interessante: o Flutter traz uma série de widgets prontos nas bibliotecas material.dart e cupertino.dart.
Botões, listas, campos de texto, scrolls e mais uma série de itens que recebemos de “brinde”.
Mas e se precisarmos de algo bastante específico que não exista por padrão no SDK? Sem problemas!
É aí que entra o super poder de personalizar widgets,
criando-os do zero! Caso queira se aprofundar em widgets e arquitetura Flutter,
recomendamos esta leitura."""


def analisa_frequencia_de_letras(texto):
    letras_texto = Counter(texto.lower())
    print(letras_texto)
    total_palavras_texto1 = sum(letras_texto.values())
    print(total_palavras_texto1)
    proporcoes = [(letra, frequencia / total_palavras_texto1)
                  for letra, frequencia in letras_texto.items()]
    proporcoes = Counter(dict(proporcoes))
    for caractere, porporcao in proporcoes.most_common(10):
        print("{} => {:.2f}%".format(caractere, porporcao * 100))
    # for letra, frequencia in letras_texto.items():
    #     porcentagem_aparicao = (frequencia / total_palavras_texto1) * 100
    #     tupla = (letra, porcentagem_aparicao)
    #     print(tupla)


analisa_frequencia_de_letras(texto1)
analisa_frequencia_de_letras(texto2)
