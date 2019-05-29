def solution(a: str, count) -> str:
  return "".join(['%20' if c.isspace() else c for c in a])
