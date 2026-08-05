
from pathlib import Path # caminho do arquivo
import pandas as pd
import numpy as np

DIRETORIO_RAIZ = Path(__file__).parent.parent

CSV_PATH = DIRETORIO_RAIZ / "raw" / "produtos_raw.csv"

df_vendas = pd.read_csv(CSV_PATH)

print(df_vendas.head())

# padronização do nome das categorias: eletrônicos, propulsão e ancoragem


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





