import re, os, yaml, importlib, functools
import unicodedata

from bella_cleaner.cleaner.commons import common_clean
from bella_cleaner.cleaner.commons.latin_chars import clean_after_latin, clean_after_latin_with_emojis
from bella_cleaner.cleaner.commons.foreign_char_handling import clean_chinese_chars, clean_korean_chars, clean_arabic_chars


class Cleaner:
  def __init__(self, base_dir= "turkish_corpus_cleaner", config_name=None):
    # Set up config dirs
    cleaner_dir = os.path.join(base_dir,  "bella_cleaner", "cleaner")
    self.commons_dir = os.path.join(cleaner_dir,  "commons")
    configs_dir = os.path.join(cleaner_dir, "configs")

    # Load from config dirs
    self.load_commons()

    # Set up defaults
    id_func = lambda x: x
    self.crop_header, self.crop_footer = id_func, id_func

    self.kill_non_latin_chars =  clean_after_latin # default is to KILL emoticon
    self.custom_clean = id_func  # no custom code, read from config

    self.kill_foreign_chars = id_func # customly, korean, combination of killing chinese or arabic chars

    self.has_pages=False # book or article, coming from a pdf most probably
    self.process_pages=id_func

    # Load and arrange custom config
    if config_name is not None:
      self.custom_dir =  os.path.join(configs_dir, config_name)
      self.custom_mod = "bella_cleaner.cleaner.configs." + config_name 
      self.load_extra_config()
      self.eval_custom_config()
      self.configure_extras()


  def load_commons(self):
    # Load common config files, replacements and deletions
    replace_file = os.path.join(self.commons_dir, "replace.txt")
    delete_file = os.path.join(self.commons_dir, "delete.txt")

    replacements = open(replace_file, "r").read().split("\n")
    deletions = open(delete_file, "r").read().split("\n")

    self.replacements = [tuple(" ".join(line.strip().split()).split(" ")) for line in replacements if line]
    self.deletions = [line.strip() for line in deletions if line]

  
  def make_replacements(self, text):
    # Handle character replacements
    for (old, new) in  self.replacements:
      text = text.replace(old, new)
    return text

  def make_deletions(self, text):
    # Kill bad characters
    for delch in  self.deletions:
      text = text.replace(delch, " ")
    return text


  def load_extra_config(self):
    yaml_file = os.path.join(self.custom_dir, "custom.yaml")  

    # Search for the custom config yaml
    if os.path.exists(yaml_file):
      # Load config yaml if exists
      with open(yaml_file, "r") as f:
        self.custom_config = yaml.safe_load(f)
    else:
        self.custom_config = {}


  def eval_custom_config(self):
    # Validate the configuration file
    yaml_keys = self.custom_config.keys()
    list_of_keys = ["replace", "delete", "custom_code", "crop_header_footer", "keep_emoticon", "kill_foreign_chars", "has_pages"]
    assert all(key in list_of_keys for key in yaml_keys), "Custom config keys should be replace, delete, custom_code, crop_header_footer, keep_emoticon, kill_foreign_chars, has_pages"

  def configure_extras(self):
    # Configure extra settings from the config.yaml
    if not self.custom_config: return

    # Process extra replacements & deletions
    self.replace_extra = self.custom_config.get("replace", None)
    self.delete_extra = self.custom_config.get("delete", None)
    self.handle_extra_reps_dels()

    # Process extra cleaning code
    self.custom_code = self.custom_config.get("custom_code", False)
    self.handle_custom_code()

    # Process header footer parsers
    self.crophf = self.custom_config.get("crop_header_footer", [])
    self.handle_croppers()

    # Arrange keeping emojis
    self.keep_emojis = self.custom_config.get("keep_emojis", "no")
    self.kill_non_latin_chars = clean_after_latin_with_emojis if self.keep_emojis == "yes" else clean_after_latin

    # Arrange Arabic, Korean, Chinese chars procesing
    self.kill_fc = self.custom_config.get("kill_foreign_chars", [])
    self.handle_foreign_chars()

    # Set up page processing code, for the book, article and other PDF genres.
    # This method usually crop the page numbers, parse book openings and bibliography. Done in custom way for books and articles separately.
    has_pages = self.custom_config.get("has_pages", "no")
    self.pages = True if has_pages=="yes" else False
    self.handle_page_code()

  def handle_page_code(self):
    # Load page code from config dir
    if not self.pages: return
    module = importlib.import_module(self.custom_mod + ".pages", package="bella_cleaner")
    self.process_pages = module.process_pages

  def handle_custom_code(self):
    # Load custom code from config dir
    module = importlib.import_module(self.custom_mod + ".custom_clean", package="bella_cleaner")
    self.custom_clean = module.custom_clean

  def handle_croppers(self):
    # Load header footer code from config dir
    if self.crophf:
      if "footer" in self.crophf:
        module = importlib.import_module(self.custom_mod + ".footer", package="bella_cleaner")
        self.crop_footer = module.crop_footer
      
      if "header" in self.crophf:
        module = importlib.import_module(self.custom_mod + ".header", package="bella_cleaner")
        self.crop_header = module.crop_header

  def handle_foreign_chars(self):
    # Arrange foreign char killing
    def compose2(f, g):
      return lambda *a, **kw: f(g(*a, **kw))

    def compose(*fs):
      return functools.reduce(compose2, fs)

    func_list = []
    if self.kill_fc:
      if "arabic" in self.kill_fc:
        func_list.append(clean_arabic_chars)
      if "chinese" in self.kill_fc:
        func_list.append(clean_chinese_chars)
      if "korean" in self.kill_fc:
        func_list.append(clean_korean_chars)
      self.kill_foreign_chars  =  compose(func_list)

    
  def handle_extra_reps_dels(self):
    # Arrange what to do with extra replacements and deletions. 
    # Extra list of replacements and deletions can override the base ones or we can use both. 
    if self.replace_extra:
      extras = self.replace_extra[0]["extras"]
      if extras in ["append", "override"]:
        replace_file = os.path.join(self.custom_dir, "replace.txt")
        new_pairs = open(replace_file, "r").read().split("\n")
        replacements = [tuple(" ".join(line.strip().split()).split(" ")) for line in new_pairs if line]
      if extras == "append":
        self.replacements += replacements
      elif extras == "override":
        self.replacements = replacements
    if self.delete_extra:
      extras = self.delete_extra[0]["extras"]
      if extras in ["append", "override"]:
        delete_file = os.path.join(self.custom_dir, "delete.txt")
        new_dels = open(replace_file, "r").read().split("\n")
        deletions = [line.strip() for line in new_dels if line]
      if extras == "append":
        self.deletions += deletions
      elif extras == "override":
        self.deletions = deletions

  def _clean(self, text):
    text = text.strip()

    # Repacements and deletions
    text = self.make_replacements(text)  # make the replacements
    text = self.make_deletions(text)     # make the deletions
    text = common_clean(text)            # further text cleaning such as punct cleaning 
    text = text.strip()

    # Custom code if any
    text = self.custom_clean(text)

    # Unicode cleaning
    text = self.kill_foreign_chars(text)  # kill arabic, korean or chinese chars exclusively
    text = self.kill_non_latin_chars(text)   # eliminate character blocks based on unicode ranges, keep emojis or not by config
    text = unicodedata.normalize("NFKC", text)  # unicode normalization
    text = " ".join(text.split())
    return text


  def clean(self, resource):
    # if self.has_pages True, then at this point input is not a text indeed list of pages. At the end output is text, pages united.
    text = self.process_pages(resource)

    # Crop header and footer, keep an eye on newlines and structure
    text = text.strip()
    text = self.crop_footer(text)
    text = text.strip()
    text = self.crop_header(text)

    # map brutal clean to all paragraphs
    paragraphs = text.strip().split("\n")
    paragraphs = list(map(self._clean, paragraphs))
    paragraphs = [parag for parag in paragraphs if parag]

    text = "\n".join(paragraphs)
    return text
