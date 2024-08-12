import re

copler = [
    "ġ",
    "Ģ",
    "ğ",
    "Ġ",
    "oı",
    "oI",
    "aı",
    "aI",
    "1ı",
    "ıı",
    "ı1",
    "i1",
    "eee"
     '¡',
    '¤',
    'ª',
     "�",

]

def is_cop(text):
  # Return if the doc has trash char sequences
  if any([cop in text for cop in copler]):
    return True
  if re.search(r"\w\$\w", text):
    return True
  return False


def too_long_words(text):
  # Return if the doc has words of length more than 50 chars, most probably many words without spaces.
  if re.search(r"\w{50}", text):
    return True
  return False


def contains_mistakes(text):
  # Return if the doc has too many single chars
  if re.search(r"\w \w \w \w \w", text):
    return True
  return False


def filter(text):
  # Main filter func
  text = text.strip()
  if not text:
    return True
  if contains_mistakes(text):
    return True
  if is_cop(text):
    return True
  if too_long_words(text):
    return True
  return False
