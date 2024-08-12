

def filter(sentence):
  # If the sentence doesn't have EOS punct
  if not any([line.endswith(punct) for punct in [".", ",", "!"]]):
    return True
  if line.isupper():
    return True
  return False
