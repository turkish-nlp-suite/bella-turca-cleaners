

def filter(text):
  topic_wrds = ["PYD"]
  for text in book_page_texts:
    if any([bad in text for bad in bads]):
      return True
  return False

