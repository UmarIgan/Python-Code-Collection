#Source: https://www.datacamp.com/community/tutorials/recommender-systems-python
#This is a function that weighting votes for each item in ratings data

from statistics import mean
import pandas as pd

def weighting_votes(vote_data):
    items=vote_data['items']#item's column
    votes=vote_data['votes']#vote's column
    num_of_votes=len(items)
    
    m=min(votes)
    avg_votes_for_item=vote_data.groupby('items')['votes'].mean()#mean of each item's vote
    mean_vote=mean(votes)#mean of all votes
    WR=((num_of_votes/(num_of_votes+m))*avg_votes_for_item)+((m/(num_of_votes+m))*mean_vote)
    return WR

#testing it with an example
votes=[5, 4, 2, 3, 5, 7, 5, 5, 6, 1, 3]
items=[1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7]
vote_data=pd.DataFrame({'items':items, 'votes':votes})
weighting_votes(vote_data)
