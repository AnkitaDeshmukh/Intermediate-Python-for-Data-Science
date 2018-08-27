
#Determine your next move
#In the Empire State Building bet, your next move depends on the number of eyes you throw with the dice.
# We can perfectly code this with an if-elif-else construct!

#The sample code assumes that you're currently at step 50. 

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)