# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = enumerate(mutants)

print(mutant_list)

for index1, index2 in enumerate(mutants):
    print(index1, index2)

for i, j in enumerate(mutants, start = 10):
    print(i,j)    