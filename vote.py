def vote(votes):
  c = []
  for i in votes:
    c.append(votes.count(i))
    max_times = max(c)
    n = c.index(max_times)
  return votes[n]

if __name__ == '__main__':
  print(vote([1,1,1,2,3]))
  print(vote([1,2,3,2,2]))