from pprint import pprint
import pandas as pd
# https://cocalc.com/projects/00d0105a-f68b-4b26-bd81-2949bd2c5204/files/notebook.ipynb?session=default

# clients input
products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']
# my input 
words = ['buy', 'price', 'discount', 'promotion', 'promo', 'shop']

keywords_list = []
# Loop through products
for product in products:
    # Loop through words
    for word in words:
        # Append combinations
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])

#pprint(keywords_list)

# converted to dataframe 
keywords_df = pd.DataFrame(keywords_list)
keywords_df = keywords_df.rename(columns={0:'Ad Group', 1:'Keyword'})

# Add a campaign column
keywords_df['Campaign'] = 'SEM_Sofas'
keywords_df['Criterion Type'] = 'Exact'

# two match type exact match and pharse match 

keywords_phrase = keywords_df.copy()
keywords_phrase['Criterion Type'] = 'Phrase'
keywords_df_final = keywords_df.append(keywords_phrase)

#export csv
keywords_df_final.to_csv('Codes/Projects/adword_cam.csv', index=False)

summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)

#print(keywords_df_final)