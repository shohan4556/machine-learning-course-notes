import pandas as pd 

baby_names_df = pd.read_csv("Codes/Pandas/baby_names.csv", index_col=0)
print(baby_names_df)