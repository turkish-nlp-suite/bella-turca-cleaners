import re


abbrevs = set([
"doç",
"dr",
"prof",
"ar",
"araşgör",
"argör",
"yrd",
"yrddoç",
"asb",
"atğm",
"av",
"bçvş",
"by",
"bk",
"bknz",
"bkz",
"bn",
"bnb",
"böl",
"coğ",
"coğr",
"cum",
"bşk",
"cumbşk",
"çvş",
"doçdr",
"dz",
"kuv",
"dzkuv",
"kuvk",
"ecz",
"fak",
"fiz",
"fizy",
"gön",
"gr",
"hs",
"uzm",
"huk",
"hz",
"hv",
"cc",
"sa",
"kur",
"bşk",
"ltd",
"şti",
"mah",
"cad",
"sok",
"müh",
"mür",
"ord",
"org",
"sav",
"savs",
"sn",
"dk",
"sf",
"şb",
"tel",
"telg",
"tüma",
"tümg",
"uzm",
"ünl",
"ütğm",
"vb",
"vs",
"vd",
"mim",
"yd",
"yb",
"yy",
])


def has_no_vowel(token):
  vowels = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
  if any([vowel in token for vowel in vowels]):
    return False
  return True


def looks_like_abbrev(token):
  token = token.replace(".", "")
  if len(token) == 1:
    return True
  if "-" in token or "_" in token:
    return True
  if token.isupper():
    return True
  if has_no_vowel(token):
    return True
  if token.lower() in abbrevs:
    return True
  return False


def is_abbrev_or_num(sent_piece):
  if sent_piece[-2].isdigit():
    return True
  tokens = sent_piece.split()
  last_token = tokens[-1][:-1]
  if looks_like_abbrev(last_token):
    return True
  return False


def split_into_sentences(text):
  newsents = []
  sentences = re.split(r'(?<=[^ÇĞİÖÜŞA-Z].[.?]) +(?=[ÇĞİÖÜŞA-Z])', text)
  prev_sent = ""
  for sent in sentences:
    if prev_sent.endswith("."):
      if is_abbrev_or_num(prev_sent):
        newsents[-1] = prev_sent + " " + sent
      else:
        newsents.append(sent)
    else:
      newsents.append(sent)

    prev_sent = sent

  return newsents
