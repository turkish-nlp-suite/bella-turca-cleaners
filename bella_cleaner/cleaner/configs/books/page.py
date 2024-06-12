import re


# Looks like footer:  comes after -\n
#136 Etienne s.30.

def looks_like_a_footer(line):
  if re.match(r"(\d+|[-*(]) ", line) and re.search(r"(s.|sayfa) ?\d+ \.?$", line):
    return True
  return False

def starts_digitic(line):
  if re.match(r"(\d+|\W| )", line):
    return True
  return False

def ends_with_dash(line):
  if line.endswith("-"):
    return True
  return False

def cut_footer(lines, has_dashes):
  if has_dashes:
    footer_ind = None
    last_five_lines = lines[-15:]
    for i, line in enumerate(last_five_lines):
      prev_line = None if i==0 else last_five_lines[i-1]
      if starts_digitic(line) and prev_line is not None and ends_with_dash(prev_line):
         footer_ind = i
         break
      elif looks_like_a_footer(line):
         footer_ind = i
         break
    if footer_ind:
        lines = lines[:-15] + last_five_lines[:i]
  else:
    footer_ind = None
    last_five_lines = lines[-15:]
    for i, line in enumerate(last_five_lines):
      if looks_like_a_footer(line):
         footer_ind = i
         break
    if footer_ind:
        lines = lines[:-15] + last_five_lines[:i]
  return lines


def is_roman_digits(line):
  return len(line) <= 6 and set(line) == set("IVX.")

def is_number(line):
  return line.isdigit() or is_roman_digits(line)

def looks_author_or_pub_name(line):
   words = line.split()
   words = [word for word in words if word not in ["ve", "ile"]]
   newl = " ".join(words)
   return newl.istitle() or newl.isupper()


def cut_header(lines):
  if len(lines) < 2:
    return lines

  first_line = lines[0].strip()
  second_line = lines[1].strip()

  if is_number(second_line):
    lines = lines[2:]
  elif is_number(first_line):
    if looks_author_or_pub_name(lines[1]):
      lines = lines[2:]
    else:
      lines = lines[1:]
  elif looks_author_or_pub_name(first_line):
    lines = lines[1:]
  return lines



def book_contain_dashes(some_pages):
  for page in some_pages:
    lines = page.split("\n")
    lines = [line for line in lines if line and not line.isspace()]
    lines = lines[:-2]
    for line in lines:
      line = line.strip()
      if line.endswith("-"):
        return True
  return False


def is_ending_short(line):
  words = line.strip().split()
  last_word = words[-1]
  if len(last_word) < 4:
    return True
  return False

def is_firstw_short(line):
  words = line.split()
  fword = words[0]
  if len(fword) < 4:
    return True
  return False

def is_ending_zero(line):
  line = line.strip()
  return line.endswith("\xad")


def unite_lines(lines, has_dashes):
  page_text = ""
  if has_dashes:
    prev_dash = False
    for line in lines:
      line = line.strip()
      if prev_dash:
          page_text = page_text[:-1] # kill previous dash and append without space
      else:
          page_text += " " #add a space
      page_text += line

      prev_dash=True if line.endswith("-") else False
  else:
    prev_zero_width = False
    for line in lines:
      line = line.strip()
      if prev_zero_width: # uniite words without space
        pass
      else:
        page_text += " " #add a space
      page_text += line
      prev_zero_width = is_ending_zero(line)

  page_text = page_text.strip()
  return page_text


def process_single_page(page, has_dashes):
  if not page or page.isspace():
    return []
  page = page.strip()
  lines = page.split("\n")
  lines = [line for line in lines if not(line.isspace() or line =='')]
  last_line = lines[-1].strip()
  if last_line.isdigit():
    lines = lines[:-1]  # kill page number

  lines =  cut_footer(lines, has_dashes)
  lines =  cut_header(lines)
  page_text = unite_lines(lines, has_dashes)
  return page_text

def process_pages(book_pages):
  book_pages = crop_header_footer(book_pages)
  if len(book_pages) == 0: return ""
  first_page = book_pages[0]
  book_has_dashes = book_contain_dashes(book_pages[:5])
  book_page_texts = [process_single_page(page, book_has_dashes) for page in book_pages]
  return "\n".join(book_page_texts)

