import re

def clean_chinese_chars(text):
  text = re.sub(r"一-龥", " ", text)
  return text

def clean_korean_chars(text):
  text = re.sub(r"[\u1100-\u11FF\u3130-\u318F\uA960-\uA97F\uAC00-\uD7AF\uD7B0-\uD7FF]", " ", text)
  return text


def clean_arabic_chars(text):
  text = re.sub(r"[ﺀ-ﻱ]", " ", text)
  text =  re.sub(r"[\u0621-\u064a\ufb50-\ufdff\ufe70-\ufefc]", " ", text)
  return text

