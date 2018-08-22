# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
#Select the cars_per_cap column from cars as a Pandas Series and store it as cpc.
cpc = cars.cars_per_cap
#Use cpc in combination with a comparison operator and 500. You want to end up with a boolean Series that's True if the corresponding country has a cars_per_cap of more than 500 and False otherwise. Store this boolean Series as many_cars
many_cars = cpc > 500
#Use many_cars to subset cars, similar to what you did before. Store the result as car_maniac.
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)
