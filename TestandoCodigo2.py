 # importando uma biblioteca da linguagem
import datetime
#Programando com datas#
DataH = datetime.date.today()
Dia = DataH.day
Mes = DataH.month
Ano = DataH.year 

#Testando formato de datas para aperfeiçoar a leitura do programa em diferente países
#Formato mais recomendado
print(DataH.strftime('%d %b %Y'))
print(DataH.strftime('%d %B %Y'))
print(DataH.strftime('%d %B %y'))
print(DataH.strftime('Compareça ao evento %A, %d %B de %Y'))
#Demais formatos encontrados
print(DataH)
DataH = str(DataH.day) + '-' + str(DataH.month) + '-' + str(DataH.year)
print(str(Dia)  + '-' + str(Mes) + '-' + str(Ano))
print(DataH)