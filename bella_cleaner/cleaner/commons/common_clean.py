import re


def clean_visual_chars(text):
  text = re.sub(r"[\uE000-\uF8FF]", " ", text)
  return text


def clean_braille(text):
  text = re.sub(r"[\u2800-\u28FF]", " ", text)
  return text

def erase_space_after_sentence_end(text):
  # if there are spaces between words and pucnt kill it. geldim . -> geldim.
  text = re.sub(r"([\w]) ([,.!])", r"\1\2", text)  
  return text

def place_space_before_new_sent(text):
  # if there are alphabetic characters after period, put a space in between. geldim.Ben -> geldim. Ben  . Exclude digits, might be parts of decimal numbers.
  text = re.sub(r"([,.!])([^\W\d])", r"\1 \2", text) 
  return text

def clean_geo_shapes(text):
  text = re.sub(r"[\u25A0-\u25CF]", " ", text)
  return text


def replace_multiple_puncts(text):
 # No processing for too many ? and !s, as they have sentimental meaning
  text = re.sub(r"[#_-]{3,}", " ", text) # erase too many of this marks
  text = re.sub(r"\.{3,}", "...", text)   # too many periods to three dots
  text = re.sub(r",{3,}", ",", text)  # too many commas to single comma.
  return text


def common_clean(text):
  text = clean_geo_shapes(text)
  text = clean_visual_chars(text)
  text = clean_braille(text)
  text = replace_multiple_puncts(text)
  text = erase_space_after_sentence_end(text)
  text = place_space_before_new_sent(text)
  return text



