import re


def kill_ending_abstract(text):
  endings = ["Abstract", "ABSTRACT"]
  for ending in endings:
    if ending in text:
      ind = text.index(ending)
      return text[:ind-1]
  return text

def cut_ending(text):
  endings = r"(anahtar (kelime(ler)?|sözcükler))"
  end_indice = None
  textl = text.lower()
  match = re.search(endings, textl)
  if match:
    sindice, end_indice = match.span()
    text = text[:end_indice-1]
  return text


def crop_footer(text):
  text = cut_ending(text)
  text = text.strip()
  text = kill_ending_abstract(text)
  return text
