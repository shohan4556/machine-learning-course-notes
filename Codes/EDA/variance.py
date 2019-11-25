import numpy as np

versicolor_petal_length = [4.7, 4.5, 4.9, 4.0,  4.6, 4.5, 4.7, 3.3, 4.6, 3.9, 3.5, 4.2, 4.0,  4.7, 3.6, 4.4, 4.5, 4.1,
     4.5, 3.9, 4.8, 4.0,  4.9, 4.7, 4.3, 4.4, 4.8, 5.0,  4.5, 3.5, 3.8, 3.7, 3.9, 5.1, 4.5, 4.5,
     4.7, 4.4, 4.1, 4.0,  4.4, 4.6, 4.0,  3.3, 4.2, 4.2, 4.2, 4.3, 3.0,  4.1]

# Array of differences to mean: differences
difference = versicolor_petal_length - np.mean(versicolor_petal_length)
#print(difference)

# Square the differences: diff_sq
diff_sq = difference **2

# Compute the mean square difference: variance_explicit
variance_explicit = np.mean(diff_sq)

# Compute the variance using NumPy: variance_np
variance_np = np.var(versicolor_petal_length) 

# Print the results
print(variance_explicit, variance_np)

standard_dev_exp = np.sqrt(variance_explicit)
standard_dev_np = np.std(versicolor_petal_length)

print(standard_dev_exp, standard_dev_np)