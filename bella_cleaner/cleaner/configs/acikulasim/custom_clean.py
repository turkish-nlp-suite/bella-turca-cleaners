import re

def fix_url(line):
  # Fix some fauty appearing of urls
  endings = [
    ("twitter. com", "twitter.com"),
    ("youtube. com", "youtube.com"),
    ("instagram. com", "instagram.com"),
    ("Twitter. com", "Twitter.com"),
    ("Youtube. com", "Youtube.com"),
    ("Instagram. com", "Instagram.com"),
    ("www. youtube. com", "www.youtube.com"),
    ("www. facebook. com", "www.facebook.com"),
    (". aspx", ".aspx"),
    (". html", ".html"),
    (". htm", ".htm"),
    (". gov. tr", ".gov.tr"),
    (". com. tr", ".com.tr"),
    (". edu. tr", ".edu.tr"),
    (". tr", ".tr"),
    (". com", ".com"),
    (". io", ".io"),
  ]
  url_regex = r"(https?:\/\/(www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\. [^\s]{2,}|www\. [a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\. [^\s]{2,}|https?:\/\/(www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\. [a-zA-Z0-9]+\.[^\s]{2,})( tr)?"
  line = re.sub(url_regex, lambda x: x.group().replace(" ", ""), line)
  for ending, repl in endings:
    line = line.replace(ending, repl)
  return line


def clean_words_in_parenthesis(text):
  # Delete text in parenthesis
  BRACKETS_REGEX = r'\(+[^\d()]*\)+'
  SQUARE_BRACKETS_REGEX = r'\[+[^\[\]]*\]'
  CURLY_BRACKETS_REGEX = r'\{+[^\{\}]*\}'
  text = re.sub(BRACKETS_REGEX, " ", text)
  text = re.sub(SQUARE_BRACKETS_REGEX, " ", text)
  text = re.sub(CURLY_BRACKETS_REGEX, " ", text)
  return text


def custom_clean(text):
  text = fix_url(text)
  text = clean_words_in_parenthesis(text)
  return text
