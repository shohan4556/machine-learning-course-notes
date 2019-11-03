import pandas as pd 

baby_names_df = pd.read_csv("Codes/Pandas/baby_names.csv", index_col=0)
#print(baby_names_df)

# keep data as dataframe 
print(baby_names_df[["Child's First Name"]])

# slicing data (start from 0 & end of slice not included)
print(baby_names_df[1:5])

# loc (label based )
# iloc (index based )

# print all row labeld as 2011 
print(baby_names_df.loc[[2011]])

# specific column access
print(baby_names_df.loc[:, ["Child's First Name"]])

