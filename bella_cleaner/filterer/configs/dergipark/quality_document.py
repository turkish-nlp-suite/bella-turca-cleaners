import re

def eliminate_article(text):
  bad_words = ["ġ", "Ģ", "ğ", "Ġ", "«", "»", "¬", "Z=", "Z =", "p=", "p =", "~x~ı", "^", "Süleyman Seyyid", "¦", "_Ab", "Jşçi", "Badge_of", "t_ç_ı_", "verdi_i", "aileleriüzerind", " hic "]
  if any([bad in text for bad in bad_words]):
    return True
  if re.search(r"\w[?!]\w", text):
    return True
  if re.search(r" [?!]\w", text):
    return True
  if re.search(r" \w \w \w ", text):
    return True
  if re.search(r"\w{50}", text):
    return True
  if "______" in text:
    return True
  return False



def looks_trash(line):
  tokens = line.split()
  return all([len(token)==1 or len(token)==2 for token in tokens])



def has_arabic_chars(text):
  if re.search(r"[ء-ي]", text): 
    return True
  return False


def filter(text):
  return has_arabic_chars(text) or looks_trash(text) or eliminate_article(text)
