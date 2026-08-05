
from pathlib import Path
import pandas as pd

DIRETORIO_RAIZ = Path(__file__).parent.parent

CSV_PATH = DIRETORIO_RAIZ / "raw" / "produtos_raw.csv"

df = pd.read_csv(CSV_PATH)

print(df.head())