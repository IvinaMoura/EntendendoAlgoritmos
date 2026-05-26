# %%
import pandas as pd
from pathlib import Path
# %%

# %%
df = pd.read_csv("TeoMeWhy/data/Dados Comunidade (respostas) - dados.csv")
print(df.head())
# %%
df = df.replace("Sim": 1, "Não":0)
# %%
