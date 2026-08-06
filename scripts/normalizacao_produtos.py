
from pathlib import Path # caminho do arquivo
import pandas as pd
import numpy as np

## Leitura dos dados

DIRETORIO_RAIZ = Path(__file__).parent.parent # Path.cwd()

CSV_PATH = DIRETORIO_RAIZ / "raw" / "produtos_raw.csv"

df_vendas = pd.read_csv(CSV_PATH)

print(df_vendas.head())

## Limpeza das categorias

df_vendas ["actual_category"] = (
    df_vendas["actual_category"]
    .str.lower()
    .str.strip()
    .str.replace(r"\s+", "", regex=True)
)

## Padronização

condicoes = [ 
  df_vendas['actual_category'].str.contains('eletr', case=False, na=False),
  df_vendas['actual_category'].str.contains('prop', case=False, na=False),
  df_vendas['actual_category'].str.contains('ancor|encor', case=False, na=False)
]

categorias = ['eletrônicos', 'propulsão', 'ancoragem']

df_vendas['actual_category'] = np.select(
  condicoes, categorias, 
  default=df_vendas['actual_category']
  )

print(df_vendas["actual_category"].value_counts())

## Conversão da coluna de preços 

print(df_vendas["price"].dtype)


df_vendas['price'] = (

  df_vendas['price']
  .str.strip()
  .str.replace('R$ ', '', regex=False)

)
df_vendas['price'] = pd.to_numeric(
df_vendas['price'], 
errors='coerce'
)


print(df_vendas["price"].dtype)

# Remoção de Duplicatas

df_vendas = df_vendas.drop_duplicates()

print(df_vendas.info())

