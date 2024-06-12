import re



def crop_header_first_page(first_page_lines):
  index=None
  for i,row in enumerate(first_page_lines):
    row = row.strip()
    if row.lower() in ["öz", "özet", "amaç", "giriş"]:
      index = i
      break
  if index is not None:
    first_page_lines = first_page_lines[index+1:]
  return first_page_lines


def crop_footer_first_page(first_page_lines):
  index=None
  for i,row in enumerate(first_page_lines):
    if row.strip().lower().startswith(("anahtar kelimeler", "anahtar sözcük", "abstract", "jel kodu", "jel code")):
      index = i
      break
  if index is not None:
    first_page_lines = first_page_lines[:index]
  return first_page_lines


def crop_first_page(first_page):
  first_lines = first_page.split("\n")
  first_lines = crop_header_first_page(first_lines)
  first_lines = crop_footer_first_page(first_lines)
  return "\n".join(first_lines)



def crop_header_second_page(spage_lines):
  index=None
  for i,row in enumerate(spage_lines):
    if row.strip().lower().startswith(("keywords", "key words", "jel code", "jelcode", "jel kodu" "anahtar kelimeler", "anahtar sözcük")):
      index = i
      break
  if index:
    spage_lines = spage_lines[index+1:]
  return spage_lines


def crop_second_page(second_page):
  if not second_page: return ""
  second_lines = second_page.split("\n")
  second_lines = crop_header_second_page(second_lines)
  return "\n".join(second_lines)

def is_page_num(line):
  return line.strip().isdigit()


def is_header_line(line):
  return is_page_num(line) 

def crop_each_page(page_lines):
  pl = len(page_lines)
  if pl > 1 and is_page_num(page_lines[1]):
    #print(1, page_lines[1])
    page_lines = page_lines[1:]
  elif pl>0 and is_page_num(page_lines[0]):
    #print(0, page_lines[0])
    page_lines = page_lines[1:]

  pl = len(page_lines)
  if not pl: return []
  lrow = page_lines[-1]
  if is_page_num(lrow):
    page_lines = page_lines[:-1]
  elif pl > 1 and is_page_num(page_lines[-2]):
    page_lines = page_lines[:-2]

  page_lines =  kill_subscript_lines(page_lines)
  return page_lines

def includes_kaynakca(page):
  includes_kaynak = lambda sent: any([kaynak_w in sent.lower() for kaynak_w in ["kaynaklar", "kaynakça"]])
  lines = page.split("\n")
  index = False
  for ind, line in enumerate(lines):
    words = line.strip().split()
    words = list(filter(None, words))
    if len(words) <=3 and  includes_kaynak(line):
      index = ind
      break
  if index:
    plines = lines[:index]
    page = "\n".join(plines)
  return index, page


def crop_kaynakca(pages):
  index = None
  for ind, page in enumerate(pages):
    has_kaynakca, new_page = includes_kaynakca(page)
    if has_kaynakca:
      index = ind
      break
  if index:
    pages = pages[:index]
    pages.append(new_page)
  return pages
    
  

def process_page(page):
  page_lines = page.split("\n")
  page_lines = [line for line in page_lines if (line and not line.isspace())]
  page_lines = crop_each_page(page_lines)
  return "\n".join(page_lines)


def looks_like_titem(line):
  line = line.strip()
  if line.isdigit():
    return True
  if line.replace(".", "").replace(",", "").isdigit():
    return True
  words = line.split()
  if len(words) <= 10: 
    return True
  if len(line) < 50:
    return True
  if len(line) >= 50:
    return False
  return False



def kill_tables(lines, known_indices):
  start_ind=None
  for ind,line in enumerate(lines):
    line = line.strip()
    if re.search(r"^(Tablo|Grafik|Şekil) \d+[.:]", line):
      if ind not in known_indices:
        start_ind=ind
        #print(start_ind, line)
        break

  if start_ind:
    end_ind = start_ind+1
    max_down = min(len(lines), start_ind+500)
    while end_ind < max_down and looks_like_titem(lines[end_ind]): # allow mx 30 lines down
      #print(lines[end_ind], "end", end_ind-start_ind)
      end_ind += 1

    nlines = lines[:start_ind] + lines[end_ind:]
    return nlines, start_ind

  return lines, None


def kill_all_tables(page_lines):
  known_indices = []
  newlines, lastind = kill_tables(page_lines, known_indices)

  while lastind is not None:
    known_indices.append(lastind)
    newlines, lastind = kill_tables(newlines, known_indices)
  return newlines


def is_subscript_line(line, rel_index):
  if rel_index > 15:
    return False
  if re.search(r"^\d ?\w", line):
    return True
  return False


def kill_subscript_lines(page_lines):
  index = None
  alll = len(page_lines)
  for ind, line in enumerate(page_lines):
    line = line.strip()
    if is_subscript_line(line, alll-ind):
      index = ind
      break
  page_lines = page_lines[:index]
  return page_lines


def line_includes_math_char(line):
  math_chars = ["Σ", "×", "Π"]
  is_ch_math = lambda char: (0x2200 <= ord(char) <= 0x22FF) or (0x1D400 <= ord(char) <= 0x1D7FF)  or (char in math_chars) 
  return any([is_ch_math(char) for char in line])

def line_includes_math_sym(line):
  math_words = ["=", "değişken", "değer", "tahmin", "sayısı", ":", ")", "(", ";"]
  return any([math_word for math_word in math_words if math_word in line])

def looks_like_title(line):
  line = line.strip()
  words = line.strip().split()
  return line.istitle() and len(words) >= 2


def looks_like_mathline(line):
  line = line.strip()
  if line.isdigit():
    return True
  if line.startswith("("):
    return True
  words = line.split()
  if len(line) < 30 and line_includes_math_char(line):
    return True
    #print("char and short")
  if looks_like_title(line):
    return False
  if len(words) <= 10: 
    #print("less wprds")
    return True
  if len(words) > 10: 
    #print("less wprds")
    return False
  if len(line) < 45:
    #print("too short")
    return True
  if len(line) < 50 and line_includes_math_sym(line):
    #print("sym and short")
    return True
  if len(line) < 65 and line_includes_math_char(line):
    #print("char and short")
    return True
  return False


def looks_mathblock_starter(line):
  line = line.strip()
  if len(line) < 65 and line_includes_math_char(line):
    return True
  return False
  
def kill_mathblocks(lines, known_indices):
  start_ind, end_ind = None, None
  for ind, line in enumerate(lines):
    line = line.strip()
    if looks_mathblock_starter(line) and ind not in known_indices:
      start_ind = ind
      #print(start_ind, line)
      break
  if start_ind:
    end_ind = start_ind
    max_down = min(len(lines), start_ind+100)
    while end_ind < max_down and looks_like_mathline(lines[end_ind]): # allow mx 30 lines down
      end_ind += 1

    nlines = lines[:start_ind] + lines[end_ind:]
    return nlines, start_ind
  return lines, None

def kill_all_mathblocks(lines):
  known_inds = []
  newlines, lastind = kill_mathblocks(lines, known_inds)

  while lastind is not None:
    known_inds.append(lastind)
    #print(known_indices, "indices")
    newlines, lastind = kill_mathblocks(newlines, known_inds)
  return newlines


#####################

def is_single_digit(line):
  line = line.strip()
  if line.isdigit():
    return True
  if line.replace(".", "").replace(",", "").replace("+", "").replace("-", "").isdigit():
    return True
  return False


def kill_single_digits(lines):
  newl = [line for line in lines if not is_single_digit(line)]
  return newl


#####################

def line_includes_big_gap(line):
  if "    " in line:
    return True
  if "\t" in line:
    return True
  return False

def is_definite_short_line(line):
  line = line.strip()
  if line.count("•") >= 2:
    return True
  num_words = [word for word in line.split() if word not in ["", " "]]
  if line_includes_big_gap(line) and  len(num_words) <= 10:
    return True
  return False

def kill_definite_short_lines(lines): 
  newl = [line for line in lines if not is_definite_short_line(line)]
  return newl


##########################


def consists_of_nums(line):
  line = line.replace(" ", "").replace(".", "").replace(",", "")
  if line.isdigit():
    return True
  return False

def is_shortline(line):
  line = line.strip()
  if consists_of_nums(line):
    return True
  if line.endswith((".", "!", "?", ":", ";")):
    return False
  if len(line) <= 45:
    return True
  words = line.split()
  if len(words) <= 5:
    return True
  return False


def kill_shortlines(lines):
  newl = [line for line in lines if not is_shortline(line)]
  return newl


#######################

def unite_newlines(lines):
  avg_line_len = sum([len(line.strip()) for line in lines]) / len(lines)
  short_line_len = int(0.75 * avg_line_len) 
  paragraphs = []
  current_paragraph = ""
  tire = False
  for line in lines:
    line = line.strip()
    current_paragraph += line
    if line.endswith("-"):
        current_paragraph = current_paragraph[:-1]
    else:
      current_paragraph += " "
    if line.endswith(".") and len(line) <= short_line_len: # cut the paragraphs here
      paragraphs.append(current_paragraph)
      current_paragraph = ""
  if current_paragraph:
    paragraphs.append(current_paragraph)

  return paragraphs

################

def is_acilis(line):
  line = line.strip()
  words = line.split()
  return len(line) <= 50 or len(words) <= 10

def is_short_first_page(fpage):
  fpage_lines = fpage.split("\n")
  fpage_lines = [fline for fline in fpage_lines if fline not in [" ", ""]]
  if len(fpage_lines) >= 10:
    return False

  if all([is_acilis(line) for line in fpage_lines]):
    return True
  return False


def skip_short_first_page(pages):
  if not pages: return []
  fpage = pages[0]
  if is_short_first_page(fpage):
    pages = pages[1:]
  return pages


###############


def process_pages(pages):
  if not pages: return ""
  pages = crop_kaynakca(pages)
  if not pages: return ""
  pages = skip_short_first_page(pages)
  if not pages: return ""
  fpage = pages[0]
  fpage = crop_first_page(fpage)
  if not pages: return ""

  plen = len(pages)
  if plen > 1:
    spage = pages[1]
    spage = crop_second_page(spage)
    rest_pages = [spage] + pages[2:]
  else:
    rest_pages =  pages[2:]

  
  npages = [fpage]
  for page in rest_pages:
    page = process_page(page)
    npages.append(page)


  all_text = "\n".join(npages)
  all_lines = all_text.split("\n")
  all_lines = kill_all_tables(all_lines)
  all_lines = kill_all_mathblocks(all_lines)
  all_lines = kill_single_digits(all_lines)
  all_lines = kill_definite_short_lines(all_lines)
  all_lines = kill_shortlines(all_lines)
  all_lines = [line for line in all_lines if line not in ["", " "]]
  if not all_lines: return ""

  paragraphs = unite_newlines(all_lines)
  all_text = "\n".join(paragraphs)

  return all_text

