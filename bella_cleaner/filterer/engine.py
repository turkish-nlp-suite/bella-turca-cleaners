import re, os, yaml, importlib, functools
import pycld2 as cld2
import unicodedata

from split_into_sentences import split_into_sentences



class Filterer:
  def __init__(self, base_dir= "turkish_corpus_cleaner", config_name=None):
    # Setup some dirs
    filterer_dir = os.path.join(base_dir,  "bella_cleaner", "filterer")
    configs_dir = os.path.join(cleaner_dir, "configs")


    # Setup defaults
    id_func = lambda x: x

    # Load and arrange custom config
    self.sent_char_lim, self.sent_word_lim = 0, 0
    self.doc_char_lim, self.doc_word_lim, self.doc_sent_lim = 0, 0, 0
    self.sent_qual_filterer, self.sent_topic_filterer  = id_func, id_func
    self.doc_qual_filterer, self.doc_topic_filterer  = id_func, id_func

    
    if config_name is not None:
      self.custom_dir =  os.path.join(configs_dir, config_name)
      self.custom_mod = "bella_cleaner.filterer.configs." + config_name 
      self.load_config()
      self.eval_config()
      self.configure()

  def is_english(self, text):
    try:
      isReliable, textBytesFound, details = cld2.detect(text)
      lang = details[0]
      if lang[0] == "ENGLISH":
        return True
    except:
      return False
    return False


  def filter_by_lang(self, text):
    return is_english(text) # to filter or not to filter

  def filter_sent_by_length(self, sentence):
    if len(sentence) <= self.sent_char_lim:
      return True
    if self.sent_word_lim:
      words = sentence.split()
      if len(words) <= self.sent_word_lim:
        return True
    return False

  def filter_sent(self, sentence):
    return self.filter_sent_by_length(sentence) or self.filter_by_lang(sentence) \\
           self.sent_qual_filterer(sentence) or self.sent_topic_filterer(sentence)


  def filter_doc_by_length(self, doc, sentences):
    if len(doc) <= self.doc_char_lim:
      return True
    if self.doc_word_lim:
      words = doc.split()
      if len(words) <= self.doc_word_lim:
        return True
    if len(sentences) <= self.doc_sent_lim:
      return True
    return False


  def filter_doc(self, doc, sentences):
    return self.filter_doc_by_length(doc, sentences) or self.filter_by_lang(doc) \\
           self.doc_qual_filterer(doc) or self.doc_topic_filterer(doc)


  def load_config(self):
    yaml_file = os.path.join(self.custom_dir, "custom.yaml")  

    with open(yaml_file, "r") as f:
      self.custom_config = yaml.safe_load(f)


  def eval_config(self):
    yaml_keys = self.custom_config.keys()
    list_of_keys = ["topic", "length", "quality", "lang"]
    assert all(key in list_of_keys for key in yaml_keys), "Custom config keys should be topic, quality, length, lang."

  def configure(self):
    self.topic_filt = self.custom_config.get("topic", [])
    self.handle_topic_filt()

    self.langf = self.custom_config.get("lang", [])
    self.handle_lang()

    self.qual_filt = self.custom_config.get("quality", [])
    self.handle_quality_filt()

    self.len_lims = self.custom_config.get("length", {})
    self.handle_length_lims()

    # Arrange keeping emojis


  def handle_topic_filt():
    if self.topic_filt:
      if "document" in sellf.topic_filt:
       module = importlib.import_module(self.custom_mod + "topic_document", package="bella_cleaner")
       self.doc_topic_filterer = module.filter
      if "sentence" in self.topic_filt:
       module = importlib.import_module(self.custom_mod + "topic_sentence", package="bella_cleaner")
       self.sent_topic_filterer = module.filter

  def handle_quality_filt():
    if self.qual_filt:
      if "document" in self.qual_filt:
       module = importlib.import_module(self.custom_mod + "quality_document", package="bella_cleaner")
       self.doc_qual_filterer = module.filter
      if "sentence" in self.qual_filt:
       module = importlib.import_module(self.custom_mod + "quality_sentence", package="bella_cleaner")
       self.sent_qual_filterer = module.filter


  def handle_lang(self):
    if self.langf:
      if "sentence" in self.langf:
          self.filter_sents_by_lang = True

      if "document" in self.langf:
          self.filter_docs_by_lang = True

  def hande_length_lims(self):
    if self.len_lims:
      for part, details in self.len_lims.items():
        if part == "sentence":
          for elt in details:
            if "char_limit" in elt:
              self.sent_char_lim = elt["char_limit"]
            elif "word_limit" in elt:
              self.sent_word_lim = elt["word_limit"]
        elif part == "document":
          for elt in details:
            if "char_limit" in elt:
              self.doc_char_lim = elt["char_limit"]
            elif "word_limit" in elt:
              self.doc_word_lim = elt["word_limit"]
            elif "sent_limit" in elt:
              self.doc_sent_lim = elt["sent_limit"]
        
      


  def _filter(self, paragraph):
    sentences = split_into_sentences(paragraph)
    sentences = [sentence for sentence in sentences if not self.filter_sentence(sentence)]
    parg = " ".join(sentences)
    return parg



  def filter(self, doc):
    sentences = split_into_sentences(doc)
    fd = sef.filter_doc(doc, sentences)

    if fd: return None  # Kill this doc completely

    paragraphs = doc.split("\n")
    paragraphs = list(map(_filter, paragraphs))
    paragraphs = [parg for parg in paragraphs if parg and not parg.isspace()] # filter possiby empty paragraphs
    doc = "\n".join(paragraphs)
    return doc

