import re
from filter_religion import is_religion
import itertools

copler = [
    "ġ",
    "Ģ",
    "ğ",
    "Ġ",
    "▶",
    "■؛",
    "^",
    "oı",
    "oI",
    "aı",
    "aI",
    "1ı",
    "ıı",
    "ı1",
    "1i",
    "i1",
    "<>",
    "eee"
    "‹",
     '¡',
    '¤',
    '©',
    'ª',
     '¬',
     '®',
     "ﬂ",
     "›",
     "‹",
     "te dirler",
     "oturü",
     "Şim di",
     "optii",
     "\\\\",
     "öı",
     "öi",
     "öa",
     "öu",
     "üı",
     "üi",
     "üa",
     "üu",
     "uı",
     "ui",
     "uö",
     "aö",
     "aü",
     "eö",
     "ıo",
     "ıö",
     "ıe",
]

def is_cop(text):
  if any([cop in text for cop in copler]):
    return True
  if text.endswith("Yayınları."):
    return True
  return False




def too_long_words(text):
  if re.search(r"\w{50}", text):
    return True
  return False



def has_arabic_chars(text):
  if re.search(r"[ء-ي]", text): 
    return True
  return False


def is_too_short(text):
  if len(text) <= 5:
    return True
  return False


def contains_consec_consonants(text):
  consos = "bcçdfghjklmnprsştqvwyzx"
  text = text.lower()
  count = 0
  charseq=""
  for char in text:
    if char in consos:
      count += 1
      charseq += char
      if count == 5:
        return True
    else:
      count = 0
      charseq=""
  return False

def contains_consec_vowels(text):
  vowels = "aeiıoöuü"
  text = text.lower()
  charseq=""
  count=0
  for char in text:
    if char in vowels:
      count += 1
      charseq += char
      if count == 4:
        return True
    else:
      count = 0
      charseq=""
  return False

sent  = "Büyükelçi Noallles'den Digiçlerl Baka٥ Veklll FaUUOr٥s.."

def contains_single_letters(text):
  if re.search(r"\b\w \w \w \w \w\b", text):
    return True
  shorts1 =  re.search(r"\b\w\w \w\w \w\b", text)
  shorts2 = re.search(r"\b\w \w\w \w\b", text)
  shorts3 = re.search(r"\b\w \w\w \w\w\b", text)
  shorts4 = re.search(r"\b\w \w \w\w\b", text)
  for shorts in [shorts1, shorts2, shorts3, shorts4]:
    if shorts:
      strt, end = shorts.span()
      matchw = text[strt:end]
      legits = ("ve", "bu", "o", "da", "ya", "ki", "de", "şu", "on")
      if any([shrtw in matchw for shrtw in legits]):
        return False
      else:
        #print("search 5")
        return True
  return False


def too_many_single_digits(text):
  words = text.split()
  shortwrds = [wrd for wrd in words if len(wrd) <=2]
  shrts = len(shortwrds)
  lwrds = len(words)
  ratio = shrts / lwrds
  if ratio >= 0.25: return True
  return False

def contains_mistakes(text):
  bad_patterns = [
        r"\w[!;:?()><{}\~·]\w",
        r" [!,;:?.)><~{}·]\w",
        r"[~,.;:_<>{}][\:;!?_(-]",
        r"[!?][\:;_(]", r"[-][\:;_-]",
        r"[)][)\_]",
        r"[(][\:;_(-]",
        r"\w[~·]",
        r"\w_\w",
        r"[^\d\W][.,][^\d\W]",
        r"[$£][^\d\W]",
        r"[^\d\W][$£]"
    ]
  if any([re.search(bad_pattern, text) for bad_pattern in bad_patterns]):
    return True
  if re.search(r"( @\w|\w@ )", text):
    return True
  if re.search(r"\wII\w", text):
    return True
  if contains_single_letters(text):
    return True
  if too_many_single_digits(text):
    return True
  if re.search(r"\. \. \. \. \. \.", text):
    return True
  if re.search(r"\.\.\.\.\.\.", text):
    return True
  if re.search(r"\.\. \.\. \.\.", text):
    return True
  if re.search(r"\w\- ", text):
    return True
  if contains_consec_consonants(text):
    return True
  if contains_consec_vowels(text):
    return True
  return False


def filter(text):
  text = text.strip()
  if not text:
    return True
  if not is_turkish(text):
    return True
  if contains_mistakes(text):
    return True
  if is_too_short(text):
    return True
  if is_cop(text):
    return True
  if too_long_words(text):
    return True
  if has_arabic_chars(text):
    return True
  return False

