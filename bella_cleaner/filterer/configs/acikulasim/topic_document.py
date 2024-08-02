def is_religion(text):
  # bin e dikkat
  tokens = text.split()
  nwords = ["iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz", "on", "bir", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan", "yüz"]
  if "bin" in tokens:
    bindex = tokens.index("bin")
    if bindex>=1:
      prev_tok = tokens[bindex-1]
      if prev_tok.isdigit() or prev_tok.lower() in nwords:
        pass
      else:
        return True

  # el-Kuran tipi
  for token in tokens:
    if token.startswith("el-"):
      nextch = token[4:]
      if nextch and nextch.isupper():
        return True

  text = text.lower()

  kuranlar =  ["siyer", "kuran-ı kerim", "kur'an", "kerîm"]
  diact = ["-ı " "-i ", "-îl ", "-ul ", "-ül "]
  if "şerîf" in text:
    return True
  if any([dia in text for dia in diact]):
    return True
  if any([krn in text for krn in kuranlar]):
    return True
  return False


def filter(text):
  return is_religion(text)
