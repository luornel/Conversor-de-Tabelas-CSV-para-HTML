import pandas as pd
import re
from datetime import datetime

def converter_formato_data(data):
    try:
        data_obj = datetime.strptime(data, '%m/%d/%Y')
        data_formatada = data_obj.strftime('%d/%m/%Y')
        return data_formatada
    except ValueError:
        return 'Data inválida'

def gerar_tabela_html(entradas):
    dados = {'Posição': [], 'Data': [], 'Nome': []}

    for entrada in entradas:
        partes = re.match(r'"(.*?)"\s+"(.*?)"\s+"(.*?)"', entrada)
        if not partes:
            return 'Formato de entrada inválido. Por favor, insira no formato "posição" "data" "nome".'

        posicao, data, nome = partes.groups()
        data_formatada = converter_formato_data(data)
        dados['Posição'].append(posicao)
        dados['Data'].append(data_formatada)
        dados['Nome'].append(nome)

    df = pd.DataFrame(dados)
    tabela_html = df.to_html(index=False, escape=False)
    return tabela_html

entradas = [
'"1" "10/31/2023" "Luã Ornelas"',
'"2" "10/31/2023" "João Silva"'
]
tabela_html = gerar_tabela_html(entradas)
print(tabela_html)
