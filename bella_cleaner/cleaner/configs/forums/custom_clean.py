import re


def kill_image(text):
  if text.startswith(("<img")):
    return ""
  text = re.sub(r'<img src.*?/>', "", text)
  text = re.sub(r'<img alt.*?/>', "", text)
  text = " ".join(text.split())
  return text


def kill_some_euro_signs(text):
  text = re.sub(r"(?<!\d)€", "", text)
  return text

def fix_url(text):
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
  text = re.sub(url_regex, lambda x: x.group().replace(" ", ""), text)
  for ending, repl in endings:
    text = text.replace(ending, repl)
  return text


def custom_clean(text):
  text = kill_image(text)
  text = kill_some_euro_signs(text)
  text = fix_url(text)
  return text
