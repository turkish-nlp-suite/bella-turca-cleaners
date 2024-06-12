import re
import pycld2 as cld2
from sentence_splitter import split_into_sentences


def is_english(text):
  try:
    isReliable, textBytesFound, details = cld2.detect(text)
    lang = details[0]
    if lang[0] == "ENGLISH":
      return True
  except:
    return False
  return False

def cut_heading(sentences):
  first_sent, rest = sentences[0], sentences[1:]

  orcid_span = re.search(r"ORCID( ID)?: [\w-]+ öz(et)?\b", first_sent, flags=re.I)
  if orcid_span:
    ost, oend = orcid_span.span()
    first_sent = first_sent[oend+1:]
    return [first_sent] + rest

  all_indices = []
  ozetler = r"(ÖZET|ÖZ|Özet:|Özet )"
  ozet_span = re.search(ozetler, first_sent)
  if ozet_span:
    ozet_s, ozet_e = ozet_span.span()
    all_indices.append(ozet_e)

  orcids = r"(ORCID ID:|ORCID|orcid)"
  orcid_span = re.search(orcids, first_sent)
  if orcid_span:
    orcid_s, orcid_e = orcid_span.span()
    all_indices.append(orcid_e)

  girisler = ["AMAÇ:", "GİRİŞ:"]
  giris_end = 0
  for giris in girisler:
    if giris in first_sent:
      ind = first_sent.index(giris)
      giris_end = max(giris_end, ind)
  if giris_end:
    all_indices.append(giris_end)

  if all_indices:
    endind = max(all_indices)
    first_sent = first_sent[endind+1:]
  return [first_sent] + rest



def kill_ending_capitals(sentences):
  if not sentences: return []
  final_sent = sentences[-1]
  if final_sent.isupper():
    return sentences[:-1]
  return sentences




def cut_english_sentences(sentences):
  index=None
  for i,sentence in enumerate(sentences):
    if is_english(sentence):
      index =i
      break
  if index:
    sentences = sentences[:index-1]
  return sentences


def crop_header(text):
  sentences = split_into_sentences(text)
  sentences = cut_heading(sentences)
  sentences = cut_english_sentences(sentences)
  sentences = kill_ending_capitals(sentences)
  sentences = [sent for sent in sentences if sent and not sent.isspace()]
  return " ".join(sentences)
