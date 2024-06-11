import re


def find_sayfa(tokens):
  index = None
  length = len(tokens)
  for i,token in enumerate(tokens):
    if "sayfa" in token.lower():
      if i -1 >= 0 and tokens[i-1].isdigit():
        index = i
        break
      elif i+1 < length and tokens[i+1].isdigit():
        index = i+1
        break
      elif i+2 < length and tokens[i+1] in (":", "-") and tokens[i+2].isdigit():
        index = i+2
        break
  return index



def find_juri(tokens):
  index = None
  length = len(tokens)
  for i,token in enumerate(tokens):
    if token == "Jüri" or token == "Jüri:":
      index = i
      break
  return index


def find_danisman(tokens):
  index = None
  length = len(tokens)
  for i,token in enumerate(tokens):
    if token in ("Yöneticisi", "Danışmanı"):
      if i-1>=0 and tokens[i-1] == "Tez":
        index =i
  return index

def find_hoca_adi(tokens):
  index = None
  length = len(tokens)
  juri_ind = find_juri(tokens)
  danisman_ind = find_danisman(tokens)

  if not juri_ind and not danisman_ind:
    return None

  unvanlar = ["Yrd.Doç.Dr.", "Yard.Doç.Dr." "Doç.Dr.", "Prof.Dr."]
  for i,token in enumerate(tokens):
    if token in unvanlar or token == "Dr." or token == "Prof." or token == "Doç.":
      index = i
      break

  if index is None:
    index = juri_ind or danisman_ind

  if index+2<length and tokens[index+2].isupper():
    index = index+2
  elif index+2<length and tokens[index+2].endswith(","):
    index = index+2
  elif index+3<length and tokens[index+3].isupper():
    index = index+3
  elif index+3<length and tokens[index+3].endswith(","):
    index = index+3
  else:
    if index+2 < length: index = index+2 # ad soyad
  return index



def looks_like_a_month(token):
  months = ["ocak", "şubat", "mart", "nisan", "mayıs", "haziran", "temmuz", "ağustos", "eylül", "ekim", "kasım", "aralık"]
  token = token.lower()
  if token in months:
    return True
  if token[-1] == "," and token[:-1] in months:
    return True
  return False


def find_tarih(tokens):
  years = ['1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
  index = None
  length = len(tokens)
  for i,token in enumerate(tokens):
    if token in years:
      if i-1>=0 and looks_like_a_month(tokens[i-1]):
        index = i
        break
  return index


def find_ozet_end_index(tokens):
  sayfa_ind = find_sayfa(tokens)
  tarih_ind = find_tarih(tokens)
  hoca_ind = find_hoca_adi(tokens)

  index  = None
  if sayfa_ind:
    index = sayfa_ind
  if tarih_ind:
    if index:
      index = max(tarih_ind, index)  # sayfa already there
    else:
      index = tarih_ind
  if hoca_ind:
    if index:
      index = max(hoca_ind, index)  # sayfa already there
    else:
      index = hoca_ind
  return index

def clip_head(text):
  # Crop by picking up clue words
  if not text: return text
  if any(ozet in text for ozet in ["Ozet", "Özet", "OZET", "ÖZET"]):
    tokens = text.split()
    owindex = None
    oword = None
    for i,token in enumerate(tokens):
      if any(oz in token for oz in ["Ozet", "Özet", "OZET", "ÖZET"]):
        owindex = i
        break
    oword = tokens[owindex]

    if owindex <=3:
      if "Ozet" in oword or "Özet" in oword:
        ntokens = tokens[owindex+1:]
        text= " ".join(ntokens).lstrip()
      else:  # OZET ilk 3 kelimede
        eindex = find_ozet_end_index(tokens)
        if eindex:
          ntokens = tokens[eindex+1:]
        else:
          ntokens = tokens[owindex+1:]
        text= " ".join(ntokens).lstrip()
    else: # OZET ilerde
      if "OZET" in oword or "ÖZET" in oword:
        # cut until that point
        ntokens = tokens[owindex+1:]
        text= " ".join(ntokens).lstrip()
  else:
    return text
  return text


def clip_english_text(text):
  # Crop abstract in English if exists
  if not text: return text
  original_tokens = text.split()
  text = text.lower()
  index = None
  if "abstract" in text:
    tokens = text.split()
    for i,token in enumerate(tokens):
      if "abstract" in token:
        index = i
        break
    if index <=10: return ""
    non_eng_tokens = original_tokens[:index]
    return " ".join(non_eng_tokens)
  else:
    return " ".join(original_tokens)
  return " ".join(original_tokens)


def crop_header(text):
  text = clip_english_text(text)
  text = text.strip()
  text = clip_head(text)
  return text

