import re



def find_comment_index(lines):
  yorum_lines = ("yorum yapan siz olun", "hiç yorum yok", "bir yorum gönder", "yeni yorum gönder", "yorum bırak", "yorum ekle") 
  yorum_words = ("comment", "comments", "yorum", "yorumlar", "kaynaklar", "kaynak")
  for ind, line in reversed(list(enumerate(lines))):
    line = line.strip().lower()
    words = line.split()
    if len(words) == 2 and line.endswith(yorum_words):
      return ind
    elif line.endswith(yorum_lines):
      return ind
  return None


def crop_footer(text):
  if not text: return text
  lines = text.split("\n")
  ci = find_comment_index(lines)
  if ci:
    lines = lines[:ci]
  text = "\n".join(lines)
  return text

