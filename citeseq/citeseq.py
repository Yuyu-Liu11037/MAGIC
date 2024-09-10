import magic
import pandas as pd


X = pd.read_csv("/workspace/MAGIC/data/test_data.csv")
magic_operator = magic.MAGIC()
X_magic = magic_operator.fit_transform(X, genes=['VIM', 'CDH1', 'ZEB1'])
X_magic.to_csv("/workspace/MAGIC/data/test_data_imputed.csv")