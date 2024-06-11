from bella_cleaner.cleaner.commons import common_clean

import unicodedata
import re, os



class Cleaner:
  def __init__(self, base_dir= "turkish_corpus_cleaner", config_file=None):
    cleaner_dir = os.path.join(base_dir,  "bella_cleaner", "cleaner")
    self.commons_dir = os.path.join(cleaner_dir,  "commons")
    self.configs_dir = os.path.join(cleaner_dir, "configs")
    self.config = None  # cleaning configuration
    self.custom_config = False  # 
    self.custom_code = False

    self.load_commons()
    '''
    if config_file is not None:
      self.load_config(config_file)
      self.configure_extras()
    '''




  def load_commons(self):
    # Load common config files
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
    # Kill some characters
    for delch in  self.deletions:
      text = text.replace(delch, " ")
    return text


  def crop_heading(self, text):
    pass


  def crop_footer(self, text):
    pass

  def configure_extras(self):
    pass

  def load_config(self, cfg_file):
    pass

  def clean(self, text):
    text = self.make_replacements(text)
    text = self.make_deletions(text)
    text = common_clean(text)
    #text = self.custom_clean(text)
    text = unicodedata.normalize("NFKC", text)
    text = " ".join(text.split())
    return text
