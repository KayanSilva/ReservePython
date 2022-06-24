def calcular_valor_por_medida(quantidade, unidade, valor):
  if(unidade == "kg"):
    gr_para_kg = quantidade / 1000
    return gr_para_kg * valor
  else:
    return unidade * valor