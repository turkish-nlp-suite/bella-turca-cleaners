

def filter(sentence):
  # If sentence doesn't have an EOS punct
  if not any([sentence.endswith(punct) for punct in [".", ",", "!"]]):
    return True
  if sentence.isupper():
    return True
  return False
