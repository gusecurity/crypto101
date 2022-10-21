from collections import defaultdict

votes = defaultdict(list)

with open("ex1/votes.txt") as f:
    for voter, vote in map(str.split, iter(f)):
        votes[vote].append(voter)

print(votes)
