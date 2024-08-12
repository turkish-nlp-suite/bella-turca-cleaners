import re

def has_trash_chars(text):
  # Return if the doc has some trashy looking character sequences
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
  # Document consisting pf very short tokens, only 1 or 2 character tokens
  tokens = line.split()
  return all([len(token)==1 or len(token)==2 for token in tokens])

def has_arabic_chars(text):
  # Return if the document has Arabic chars
  if re.search(r"[ء-ي]", text): 
    return True
  return False


def filter(text):
  return has_arabic_chars(text) or looks_trash(text) or has_trash_chars(text)
