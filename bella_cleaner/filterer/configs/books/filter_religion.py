def is_religion(text):
  # bin e dikkat
  tokens = text.split()

  # el-Kuran tipi
  for token in tokens:
    if token.startswith("el-"):
      nextch = token[4:]
      if nextch and nextch.isupper():
        print("el-", nextch, "rel")
        return True

  text = text.lower()

  kuranlar =  [" siyer", "kuran-ı kerim", "kur'an", "kerîm", " sahabe"]
  #diact = ["-ı " "-i ", "-îl ", "-ul ", "-ül "]
  dualar = ["kabul olan dualar", "evlilik duası", "evlilik duaları", "peygamber efendimiz", "hz. muhammed", "kâbe", "dilek duas", "esmalar"]
  if "şerîf" in text:
    return True
  #if any([dia in text for dia in diact]):
  #  print("diact")
  #  return True
  if any([krn in text for krn in kuranlar]):
    return True
  if any([dua in text for dua in dualar]):
    return True
  return False

