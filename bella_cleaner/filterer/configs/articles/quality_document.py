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
  for cop in copler:
    if cop in text:
      print(cop)
      return True
  #if any([cop in text for cop in copler]):
  #  return True
  if re.search(r"\w\$\w", text):
    return True
  return False



def too_long_words(text):
  if re.search(r"\w{50}", text):
    return True
  return False




def contains_mistakes(text):
  if re.search(r"\w \w \w \w \w", text):
    return True
  return False


def filter(text):
  text = text.strip()
  if not text:
    return True
  if contains_mistakes(text):
    return True
  if is_too_short(text):
    return True
  if is_cop(text):
    return True
  if too_long_words(text):
    return True
  return False
