

def filter(sentence):
  if not any([line.endswith(punct) for punct in [".", ",", "!"]]):
    return True
  if line.isupper():
    return True
  return False
