def NER(text,lang_code):
  
  import spacy
  
  lang_models = {
    'ca': 'ca_core_news_sm',
    'zh': 'zh_core_web_sm',
    'da': 'da_core_news_sm',
    'nl': 'nl_core_news_sm',
    'en': 'en_core_web_sm',
    'fi': 'fi_core_news_sm',
    'fr': 'fr_core_news_sm',
    'de': 'de_core_news_sm',
    'el': 'el_core_news_sm',
    'it': 'it_core_news_sm',
    'ja': 'ja_core_news_sm',
    'ko': 'ko_core_news_sm',
    'lt': 'lt_core_news_sm',
    'mk': 'mk_core_news_sm',
    'nb': 'nb_core_news_sm',
    'pl': 'pl_core_news_sm',
    'pt': 'pt_core_news_sm',
  }
  nlp = spacy.load(lang_models.get(lang_code,'xx_ent_wiki_sm'))
  doc = nlp(text)
  ans = list()
  if doc.ents:
    for ent in doc.ents:
      ans.append({
          'text': ent.text,
          'type': ent.label_,
          'start_pos': ent.start_char,
          'end_pos': ent.end_char
      })
  return ans
