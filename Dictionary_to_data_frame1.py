# Pre-defined lists
#names, containing the country names for which data is available.
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
#dr, a list with booleans that tells whether people drive left or right in the corresponding country
dr =  [True, False, False, False, True, True, True]
#cpc, the number of motor vehicles per 1000 people in the corresponding country.
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names,'drives_right':dr,'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

