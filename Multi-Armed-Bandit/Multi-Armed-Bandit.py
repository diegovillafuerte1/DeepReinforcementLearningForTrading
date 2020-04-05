# Random Selection

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Ads_Optimisation.csv')

# Implementing Random Selection
import random
N = 10000
d = 10
ads_selected = []
total_reward = 0
for n in range(0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    total_reward = total_reward + reward

print("Random Selection")
print(total_reward)


# Implementing UCB
import math
# hard limit on number of trials
N = 10000
# number of ads
d = 10
ads_selected = []
numbers_of_selections = [0] * d
sums_of_reward = [0] * d
total_reward = 0

for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        # if we've selected this ad ever before
        if (numbers_of_selections[i] > 0):
            # the average reward is equal to the sum of all the rewards for this ad, divided by the number of times we've selected it
            average_reward = sums_of_reward[i] / numbers_of_selections[i]
            # the use of math.log here means that selections that have already been selected frequently,
            # will be selected with decreasing frequency over time.
            delta_i = math.sqrt(2 * math.log(n+1) / numbers_of_selections[i])
            # each time something is selected, "upper_bound" will decrease (denominator of average reward and delta_i is increasing)
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            # if we find an ad with an upper bound greater than our previous upper bound, we decided to select that ad and replace the max_upper_bound
            max_upper_bound = upper_bound
            ad = i
    # this doesn't really do anything, I'd imagine if we were doing other things with the ads we've selected we might use it
    ads_selected.append(ad)
    # this determines the frequency we select ads in our mathy section above
    numbers_of_selections[ad] += 1
    # get the reward from having selected whichever add we have selected
    reward = dataset.values[n, ad]
    # keep track of all the rewards we've gotten for this particular ad 
    # (which we'll use in the mathy bits to determine if we want to try selecting a different ad)
    sums_of_reward[ad] += reward
    # keep track of the total reward we've gotten while running this algo
    total_reward += reward

print("Upper Confidence Bound")
print(total_reward)