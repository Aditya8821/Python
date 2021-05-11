from collections import Counter
def winner(votes):
    vote_count=Counter(votes)
    max_votes=max(vote_count.values())
    lst=[i for i in vote_count.keys() if vote_count[i]==max_votes]
    print(sorted(lst[0]))
votes =['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john'] 
winner(votes) 