# Conversor de Texto para Tabela HTML

## Como Funciona

O script utiliza a biblioteca Pandas para manipulação de dados e geração da tabela HTML. Cada linha de texto é processada para extrair as informações de posição, data e nome, que são então armazenadas em um DataFrame do Pandas. Após processar todas as linhas de texto, o DataFrame é convertido em uma tabela HTML. A extração das partes de cada linha de texto é realizada com o auxílio de expressões regulares, garantindo que o formato específico seja respeitado e que os dados sejam corretamente extraídos, mesmo que contenham espaços.

## Como Usar

1. Usando o "Google Colab" no seu navegador, faça o download do script `conversor_de_tabelas_csv_para_html.py` e importe-o.
    Se preferir, clone o repositório para a sua máquina local.
2. Caso opte por local, verifique se você tem o Python e o Pandas instalados. Você pode instalar o Pandas executando `pip install pandas`.
3. Abra o script `conversor_de_tabelas_csv_para_html.py` em um editor de texto ou IDE de sua preferência.
4. Insira as linhas de texto que você deseja converter em uma tabela HTML na lista `entradas`.
5. Execute o script. A tabela HTML resultante será impressa no console.

## Exemplo de Entrada

```python
entradas = [
    '"1" "31/10/2023" "Luã Ornelas"',
    '"2" "31/10/2023" "João Silva"'
]
```

## Resultado

O script irá gerar e imprimir a tabela HTML correspondente às entradas fornecidas.

Exemplo resultado:
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Posição</th>
      <th>Data</th>
      <th>Nome</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>30/10/2023</td>
      <td>Luã Ornelas</td>
    </tr>
    <tr>
      <td>2</td>
      <td>30/10/2023</td>
      <td>João Silva</td>
    </tr>
  </tbody>
</table>
```

## Requisitos

- Python 3.x
- Pandas
