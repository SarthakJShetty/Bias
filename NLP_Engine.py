import nltk; nltk.download('stopwords')
import re
import numpy as np
import pandas as pd
from pprint import pprint

import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

import spacy

import pyLDAvis
import pyLDAvis.gensim
import matplotlib as plt

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use'])

df = pd.read_json('https://raw.githubusercontent.com/selva86/datasets/master/newsgroups.json')
print(df.target_names.unique())
df.head()

data = df.content.values.tolist()
data = [re.sub('\S*@\S*\s?','', sent) for sent in data]
data = [re.sub('\s+', ' ', sent) for sent in data]
data = [re.sub("\'", "", sent) for sent in data]
pprint(data[:1])

def sent_to_words(sentences):
 for sentence in sentences:
  yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))

data_words = list(sent_to_words(data))

print(data_words[:1])

bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100)
trigram = gensim.models.Phrases(bigram[data_words], threshold=100)

bigram_mod = gensim.models.phrases.Phraser(bigram)
trigram_mod = gensim.models.phrases.Phraser(trigram)

print(trigram_mod[bigram_mod[data_words[0]]])

def remove_stopwords(texts):
 return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

def make_diagrams(texts):
 return [bigram_mod[doc] for doc in texts]

def make_trigrams(texts):
 return [trigram_mod[bigram_mod[doc]] for doc in texts]

def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
 """https://spacy.io/api/annotation"""
 texts_out = []
 for sent in texts:
  doc = nlp(" ".join(sent))
  texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
 return texts_out

data_words_nostops = remove_stopwords(data_words)
data_words_bigrams = make_diagrams(data_words_nostops)

nlp = spacy.load('en', disable=['parser', 'ner'])

data_lemmatized = lemmatization(data_words_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
print(data_lemmatized[:1])

id2word = corpora.Dictionary(data_lemmatized)

texts = data_lemmatized
corpus = [id2word.doc2bow(text) for text in texts]
print(corpus[:1])

[[(id2word[id], freq) for id, freq in cp] for cp in corpus[:1]]

lda_model = gensim.models.ldamodel.LdaModel(corpus = corpus, id2word = id2word, num_topics = 20, random_state = 100, update_every = 1, chunksize = 100, passes = 10, alpha = 'auto', per_word_topics = True)

pprint(lda_model.print_topics())
doc_lda = lda_model[corpus]

print("\nPerplexity: ", lda_model.log_perplexity(corpus))
coherence_model_lda=CoherenceModel(model = lda_model, texts = data_lemmatized, dictionary = id2word, coherence='c_v')

coherence_lda = coherence_model_lda.get_coherence()
print('\nCoherence Score: ', coherence_lda)