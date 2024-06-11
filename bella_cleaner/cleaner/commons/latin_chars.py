import re



def clean_after_latin(text):
    emoticon_pattern = r"[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]+"
    text = re.sub(emoticon_pattern, " ", text)
    text = re.sub(r"[\u0530-\uFFFF]", " ", text)  # kill emoji and preserve Greek
    return text

def clean_after_latin_with_emojis(text):

  # Define the unicode blocks to preserve
  preserve_blocks = [
    (0x1F300, 0x1F53D), # Miscellaneous Symbols and Pictographs
    (0x1F600, 0x1F64F),  # Emoticons
    (0x1F680, 0x1F6C5),  # Transport and Map Symbols
  ]

  exclude_ranges = [
    (0x1F53E, 0x1F5FF),
    (0x1F650, 0x1F67F)
    # open ended after 0x16C6
          ]

  in_bad_ranges  =lambda ch: any([st <= ord(ch) <= end for (st, end) in exclude_ranges]) or ord(ch) >= 0x1F6C6
  cleaned_text = "".join([ch for ch in text if not in_bad_ranges(ch)])
  return cleaned_text


def clean_visual_chars(text):
  text = re.sub(r"[\uE000-\uF8FF]", " ", text)
  return text


