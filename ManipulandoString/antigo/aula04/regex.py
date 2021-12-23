import re

email1 = "Meu numero é 12234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é meu celular"
email4 = "lalalalaala 99543-1254 hfuqerheruhveurghequg 9999-8787 wdhurhqeugh 995432-1243"

padrao  = "[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]"
padrao2 = "[0-9][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]"
padrao3 = "[0-9]{4,5}[-][0-9]{4}"

retorno = re.search(padrao3,email1)
print(retorno.group())

retorno2 = re.findall(padrao3,email4) 
print(retorno2)