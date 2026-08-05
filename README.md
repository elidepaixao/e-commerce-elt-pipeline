# Pipeline ELT e Analytics - E-commerce Náutico

## Sobre o Projeto
Este repositório contém o desenvolvimento de uma pipeline de dados ponta a ponta e resoluções analíticas para um e-commerce do setor náutico. O objetivo central do projeto é processar dados brutos desorganizados, construir modelagens financeiras, aplicar técnicas de SQL estruturado e desenvolver modelos estatísticos para apoiar a tomada de decisão estratégica da empresa.

O projeto foi desenvolvido inteiramente em Python 3 e abrange desde etapas de extração e transformação (ELT) até análises de Machine Learning baseline.

## Estrutura dos Desafios Resolvidos

O escopo do projeto foi dividido nas seguintes frentes de engenharia e análise de dados:

### 1. Limpeza e Normalização de Dados (Camada Silver)
* O projeto realiza a normalização dos dados presentes no arquivo `produtos_raw.csv`[cite: 1]. 
* Os nomes das categorias de produtos são padronizados especificamente em: eletrônicos, propulsão e ancoragem[cite: 1]. 
* O script realiza o *casting* de dados, convertendo os valores apropriados para o tipo numérico, além de garantir a remoção de todas as duplicatas[cite: 1].

### 2. Tratamento de Estruturas Complexas (JSON)
* Os dados históricos de preços de compra encontram-se aninhados no arquivo `custos_importacao.json`[cite: 1]. 
* Foi desenvolvido um pipeline para carregar esse arquivo JSON, processar a estrutura aninhada e gerar um novo arquivo CSV organizado[cite: 1].

### 3. Modelagem Financeira e Conversão Cambial
* O sistema cruza os valores de venda do sistema (`vendas_2023_2024.csv` em BRL) com o catálogo de fornecedores (`custos_importacao.json` em USD unitário)[cite: 1].
* O custo em BRL é calculado utilizando a média da cotação de venda do dia baseada no Banco Central[cite: 1].
* Os dados são agregados por `id_produto`, gerando métricas fundamentais: receita total (BRL), prejuízo total (BRL) e percentual de perda[cite: 1].

### 4. Modelagem Dimensional em SQL (Dimensão de Datas)
* Foi construída uma dimensão de datas utilizando SQL para resolver inconsistências no cálculo de médias diárias[cite: 1].
* O cruzamento da dimensão de calendário com a tabela de vendas garante que dias sem registros no sistema sejam considerados com valor de venda igual a zero, permitindo identificar com precisão o dia da semana com a pior média de vendas[cite: 1].

### 5. Previsão de Demanda (Baseline Model)
* Desenvolvimento de um modelo preditivo focado em estimar a demanda para o item "Motor de Popa Yamaha Evo Dash 155HP"[cite: 1].
* O modelo baseline foi construído utilizando a média móvel dos últimos 7 dias de vendas[cite: 1].
* A previsão estipula as vendas diárias para o período de teste correspondente a janeiro de 2024, comparando o resultado com os valores reais através da métrica MAE (Mean Absolute Error)[cite: 1].

### 6. Motor de Recomendação
* Implementação de um sistema de recomendação baseado em comportamento de compra[cite: 1].
* A solução constrói uma matriz de interação Usuário-Produto (considerando presença/ausência de compra) e calcula a Similaridade de Cosseno entre os itens[cite: 1].
* O algoritmo gera um ranking dos 5 produtos mais similares para serem recomendados junto ao item de referência "GPS Garmin Vortex Maré Drift"[cite: 1].

## Tecnologias Utilizadas
* **Linguagem Principal:** Python 3
* **Manipulação de Dados:** Pandas, Numpy
* **Modelagem de Dados e Banco de Dados:** SQL (Dimensão de Calendário)
* **Algoritmos e Estatística:** Scikit-Learn (para Cosine Similarity) e cálculos nativos de MAE

## Como Executar o Projeto

1. Faça o clone deste repositório:
   ```bash
   git clone <url-do-repositorio>

2. Crie e ative um ambiente virtual:

  # Windows
  python -m venv venv
  .\venv\Scripts\activate

  # Linux/MacOS
  python3 -m venv venv
  source venv/bin/activate

3. Instale as dependências:

  pip install -r requirements.txt

4. Execute os scripts localizados na pasta scripts/ para reproduzir as pipelines de transformação e visualização dos resultados.