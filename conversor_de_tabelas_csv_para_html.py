import pandas as pd
import re

def gerar_tabela_html(entradas):
    dados = {'Posição': [], 'Data': [], 'Nome': []}

    for entrada in entradas:

        partes = re.match(r'"(.*?)"\s+"(.*?)"\s+"(.*?)"', entrada)
        if not partes:
            return 'Formato de entrada inválido. Por favor, insira no formato "posição" "data" "nome".'

        posicao, data, nome = partes.groups()
        dados['Posição'].append(posicao)
        dados['Data'].append(data)
        dados['Nome'].append(nome)

    df = pd.DataFrame(dados)

    tabela_html = df.to_html(index=False, escape=False)

    return tabela_html

entradas = [
'"1" "30/10/2023" "Luã Ornelas"',
'"2" "30//10/2023" "João Silva"'
]
tabela_html = gerar_tabela_html(entradas)
print(tabela_html)
