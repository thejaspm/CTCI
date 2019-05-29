def solution(x:str, y:str):
  from functools import reduce
  return reduce(lambda x,y: x&y , [True if a == b else False for a,b in zip(sorted(x),sorted(y))])
