from ml_cupom_fiscal import *
from calculos import *

print(obter_dados_por_foto("20200606_Violeta.jpeg"))

df = obter_cupons_detalhados()
df.head()

obterDadosComPDF()