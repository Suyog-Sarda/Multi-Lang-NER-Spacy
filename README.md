# Multi-Lang-NER-Spacy

Pre-requisites:

1. Install latest spacy package (3.3.0 at the time of creating this file) : `pip install --upgrade spacy`
2. Install the required spacy language models : `python -m spacy download <language_model_name>`.
      Choose language_model from the following:
      ```
          {
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
     ```
     Note: If your language is not in the mapping above, install the following multilanguage model : `python -m spacy download xx_ent_wiki_sm`
