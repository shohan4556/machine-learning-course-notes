from pprint import pprint
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

pprint(keywords_list)