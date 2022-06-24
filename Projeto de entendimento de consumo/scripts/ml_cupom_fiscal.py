#!sudo apt-get install tesseract-ocr tesseract-ocr-por
#!pip install pytesseract
#!pip install Pillow
#!pip install tika

import pytesseract
import pandas as pd
import os
from PIL import Image
from tika import parser

def obter_dados_por_foto(arquivo):
    pasta = 'img_cupons'

    return pytesseract.image_to_string(Image.open(f'{pasta}/{arquivo}'), lang= 'por')

def obter_cupons_detalhados():
    
    pasta = 'cupons_fiscais_detalhadas'
    df = pd.DataFrame()
    
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
          new_csv = pd.read_csv(f'{pasta}/{arquivo}')
          df = df.append(new_csv)
          
    df['codigo'] = df['codigo'].astype(str)
    df['data'] = df.nf.str[:8]
    df['estabelecimento'] = df.nf.str[9:]
    df = df.drop(columns=['nf'], axis=1)
    return df

def obterDadosComPDF():
    pasta = 'arquivos_para_processar'
    raw = parser.from_file(f'{pasta}/TesteEmArquivo.pdf')
    print(raw['content'])