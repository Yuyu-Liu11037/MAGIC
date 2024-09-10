import magic
import sys
import pandas as pd
import numpy as np
import random


SITE1_CELL = 16311
SITE2_CELL = 25171
SITE3_CELL = 32029
SITE4_CELL = 16750
row_1 = SITE1_CELL + SITE2_CELL
row_2 = SITE1_CELL + SITE2_CELL + SITE3_CELL

X = pd.read_csv("/workspace/MAGIC/data/citeseq_missing.csv", index_col=0)
print(X.shape)

selected_rows = random.sample(range(row_1, row_2), SITE3_CELL)
X_selected = X.iloc[selected_rows, :]
print(X_selected.shape)

magic_operator = magic.MAGIC()
X_selected_magic = magic_operator.fit_transform(X_selected)
X.iloc[selected_rows, :] = X_selected_magic
print(X.shape)

chunk_size = 10000
print(f'Start writing in chunks.\n')
with open("/workspace/MAGIC/data/citeseq_imputed.csv", 'w') as f:
    X.iloc[:0].to_csv(f, index=True)
    
    total_rows = len(X)
    for i in range(0, total_rows, chunk_size):
        X.iloc[i:i + chunk_size].to_csv(f, header=False, index=True)
        print(f'Written {i + chunk_size if i + chunk_size < total_rows else total_rows}/{total_rows} rows')
print("Finished writing the CSV file in chunks.")
