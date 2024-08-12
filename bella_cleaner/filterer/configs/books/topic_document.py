

def filter(text):
  topic_wrds = ["PYD"]
  if any([bad in text for bad in topic_wrds]):
    return True
  return False

