'''Hello! This module of code is a part of the larger Bias project.
This file was earlier named as Temp_Gensim_Code; code is now bifurcated into Gensim code (this) and a seperate
visualization code that will be added to the repository as well.

Checkout the build-log.md file for a more detailed explanation of the changes.
Checkout the Bias README.md for an overview of the project.

Sarthak J. Shetty
24/11/2018'''

'''Natural Language toolkit. Here we download the commonly used English stopwords'''
import nltk; nltk.download('stopwords')
'''Standard set of functions for reading and appending files'''
import re
'''Pandas and numpy is a dependency used by other portions of the code.'''
import numpy as np
import pandas as pd
'''Think this stands for pretty print. Prints out stuff to the terminal in a prettier way'''
from pprint import pprint

'''Contains the language model that has to be developed.'''
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
from common_functions import status_logger
'''Industrial level toolkit for NLP'''
import spacy

import pyLDAvis
import pyLDAvis.gensim

'''Make pretty visualizations'''
import matplotlib as plt

'''Library to log any errors. Came across this in the tutorial.'''
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use', 'com', 'https', 'url', 'link', 'xe', 'abstract', 'author', 'chapter', 'springer', 'title'])

#This is where the data is obtained by the nlp engine
def data_reader(abstracts_log_name, status_logger_name):
	data_reader_start_status_key = abstracts_log_name+".txt is being ported to dataframe"
	status_logger(status_logger_name, data_reader_start_status_key)
	textual_dataframe = pd.read_csv(abstracts_log_name+'_'+'ANALYTICAL'+'.txt', delimiter="\t")
	data_reader_end_status_key = abstracts_log_name+".txt has been ported to dataframe"	
	status_logger(status_logger_name, data_reader_end_status_key)
	return textual_dataframe
#Code to check if the data being obtained is legit or not
#print(df.target_names.unique())

def textual_data_trimmer(textual_dataframe, status_logger_name):
	textual_data_trimmer_start_status_key = "Trimming data and preparing list of words"
	status_logger(status_logger_name, textual_data_trimmer_start_status_key)
	'''This function converts the textual data into a list and removes special characters, virtue of email correspondence'''
	textual_data = textual_dataframe.values.tolist()
	textual_data_trimmer_end_status_key = "Trimmed data and prepared list of words"
	status_logger(status_logger_name, textual_data_trimmer_end_status_key)
	#pprint(data[:1])
	return textual_data

def sent_to_words(textual_data, status_logger_name):
	sent_to_words_start_status_key = "Tokenizing words"
	status_logger(status_logger_name, sent_to_words_start_status_key)
	'''This function tokenizes each sentence into individual words; also called tokens'''
	for sentence in textual_data:
		yield(gensim.utils.simple_preprocess(str(textual_data), deacc=True))
	textual_data = list(sent_to_words(textual_data))
	#print(textual_data[:1])
	sent_to_words_end_status_key = "Tokenized words"
	status_logger(status_logger_name, sent_to_words_end_status_key)	
	return textual_data

def bigram_generator(textual_data, status_logger_name):
	bigram_generator_start_status_key = "Generating word bigrams"
	status_logger(status_logger_name, bigram_generator_start_status_key)	
	'''Takes the textual data and prepares the bigram, two collectively high frequency words'''
	bigram = gensim.models.Phrases(textual_data, min_count=5, threshold=100)
	bigram_mod = gensim.models.phrases.Phraser(bigram)
	bigram_generator_end_status_key = "Generated word bigrams"
	status_logger(status_logger_name, bigram_generator_end_status_key)	
	return bigram_mod

def trigram_generator(textual_data, status_logger_name):
	'''Takes the textual data and prepares the trigram, three collectively high frequency words'''
	trigram_generator_start_status_key = "Generating word trigrams"
	status_logger(status_logger_name, trigram_generator_start_status_key)
	trigram = gensim.models.Phrases(bigram[textual_data], threshold=100)
	trigram_mod = gensim.models.phrases.Phraser(trigram)
	print("Printing the trigram_mod\n")
	pprint(trigram_mod[bigram_mod[textual_data[0]]])
	print("Print of the trigram_mod has concluded\n")
	trigram_generator_end_status_key = "Generating word trigrams"
	status_logger(status_logger_name, trigram_generator_end_status_key)
	return trigram_mod

def remove_stopwords(textual_data, status_logger_name):
	remove_stopwords_start_status_key = "Removing stopwords"
	status_logger(status_logger_name, remove_stopwords_start_status_key)
	return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in textual_data]
	remove_stopwords_end_status_key = "Removed stopwords"
	status_logger(status_logger_name, remove_stopwords_end_status_key)

def make_bigrams(textual_data, status_logger_name):
	make_bigrams_start_status_key = "Generating bigrams"
	status_logger(status_logger_name, make_bigrams_start_status_key)
	bigram_mod = bigram_generator(textual_data, status_logger_name)
	return [bigram_mod[doc] for doc in textual_data]
	make_bigrams_end_status_key = "Generated bigrams"
	status_logger(status_logger_name, make_bigrams_end_status_key)

def make_trigram(textual_data, status_logger_name):
	make_trigrams_start_status_key = "Generating trigrams"
	status_logger(status_logger_name, make_trigrams_start_status_key)
	trigram_mod = trigram_generator(textual_data)
	return [trigram_mod[bigram_mod[doc]] for doc in textual_data]
	make_trigrams_end_status_key = "Generated trigrams"
	status_logger(status_logger_name, make_trigrams_end_status_key)

def lemmatization(status_logger_name, textual_data, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
	lemmatization_start_status_key = "Beginning lemmatization"
	status_logger(status_logger_name, lemmatization_start_status_key)
	"""https://spacy.io/api/annotation"""
	texts_out = []
	nlp = spacy.load('en', disable=['parser', 'ner'])
	for sent in textual_data:
		doc = nlp(" ".join(sent))
		texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
	lemmatization_end_status_key = "Ending lemmatization"
	status_logger(status_logger_name, lemmatization_end_status_key)
	return texts_out

def nlp_engine_main(abstracts_log_name, status_logger_name):
	nlp_engine_main_start_status_key = "Initiating the NLP Engine"
	status_logger(status_logger_name, nlp_engine_main_start_status_key)

	'''Extracts the data from the .txt file and puts them into a Pandas dataframe buckets'''
	textual_dataframe = data_reader(abstracts_log_name, status_logger_name)
	'''Rids the symbols and special characters from the textual_data'''
	textual_data = textual_data_trimmer(textual_dataframe, status_logger_name)
	'''Removes stopwords that were earlier downloaded from the textual_data'''
	textual_data_no_stops = remove_stopwords(textual_data, status_logger_name)
	'''Prepares bigrams'''
	textual_data_words_bigrams = make_bigrams(textual_data_no_stops, status_logger_name)
	'''Loads the English model from spaCy'''
	nlp = spacy.load('en', disable=['parser', 'ner'])

	textual_data_lemmatized = lemmatization(status_logger_name, textual_data_words_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
	#print(textual_data_lemmatized[:1])

	id2word = corpora.Dictionary(textual_data_lemmatized)

	texts = textual_data_lemmatized
	corpus = [id2word.doc2bow(text) for text in texts]
	#print(corpus[:1])

	[[(id2word[id], freq) for id, freq in cp] for cp in corpus[:1]]

	'''Builds the actual LDA model that will be used for the visualization and inference'''
	lda_model = gensim.models.ldamodel.LdaModel(corpus = corpus, id2word = id2word, num_topics = 20, random_state = 100, update_every = 1, chunksize = 100, passes = 10, alpha = 'auto', per_word_topics = True)

	#pprint(lda_model.print_topics())
	doc_lda = lda_model[corpus]

	perplexity_score = lda_model.log_perplexity(corpus)

	#print("\nPerplexity: ", str(perplexity_score))

	perplexity_status_key = "Issued perplexity:"+" "+str(perplexity_score)

	status_logger(status_logger_name, perplexity_status_key)
	
	"""coherence_model_lda=CoherenceModel(model = lda_model, texts = textual_data_lemmatized, dictionary = id2word, coherence='c_v')

	coherence_lda = coherence_model_lda.get_coherence()
	print('\nCoherence Score: ', coherence_lda)"""

	nlp_engine_main_end_status_key = "Idling the NLP Engine"
	status_logger(status_logger_name, nlp_engine_main_end_status_key)

	return lda_model, corpus, id2word