import random
import pandas as pd

# Set up the initial condition.
number_of_user = 1000
follow_for_each_user = 5

# generate the pair of the follower_id and user_id
i = 1
users = []
follows = []
while i <= number_of_user:
    users += [i] * follow_for_each_user
    random_nums = random.sample(range(1,number_of_user),
                                follow_for_each_user) 
    while i in random_nums:
        random_nums = random.sample(range(1,number_of_user),
                                follow_for_each_user)
    i+=1
    follows += random_nums

# store the data into csv file
follow_table = pd.DataFrame({'user_id':users, 'follows_id':follows})
follow_table.to_csv("follows.csv")
