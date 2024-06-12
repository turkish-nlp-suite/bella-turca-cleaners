

def crop_footer(text):
  if not text: return text
  if "KAYNAKÇA" in text:
    kaynakca_index = text.index("KAYNAKÇA")
    text = text[:kaynakca_index]
  return text
