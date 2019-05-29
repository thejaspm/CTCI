def solution(inp: str):
  s = sorted(inp)
  for i in range(1, len(s))
    if s[i] == s[i-1]:
      return False
  return True
 


def solution1(inp: str):
  s = set(inp.lower())
return True if len(s) == len(inp) else False
