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
from Visualizer import visualizer_main
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
stop_words.extend(['from', 'subject', 're', 'edu', 'use', 'com', 'https', 'url', 'link', 'xe', 'abstract', 'author', 'chapter', 'springer', 'title', "the", "of", "and", "in", "to", "a", "is", "for", "from", "with", "that",	"by", "are", "on", "was", "as", 
	"were", "url:", "abstract:", "abstract",  "author:", "title:", "at", "be", "an", "during", "have", "this", "which", "study", "been", "species", "not", "has", "between",
	"using", "its", "also", "these", "this", "used", "over", "can", "within", "into", "all","due", "use", "about", "a", 'it', 'their', "where", "we", "most", "may", "through",
	"though", "like", "or", "further", "e.g.", "along", "any", "those", "had", "toward", "due", "both", "some", "use", "even", "more", "but", "while", "pass", 
	"well", "will", "when", "only", "after", "author", "title", "there", "our", "did", "much", "as", "if", "become", "still", "various", "very", "out",
	"they", "via", "available", "such", "than", "different", "many", "areas", "no", "one", "two", "small", "first", "other", "such", "-", "could", "studies", "high",
	"provide", "among", "highly", "no", "case", "across", "given", "need", "would", "under", "found", "low", "values", "xe2\\x80\\x89", "xa", "xc", "xb", "\xc2\xa0C\xc2\xa0ha\xe2\x88\x921", "suggest", "up", "'The", "area"])

def data_reader(abstracts_log_name, status_logger_name):
	'''This wherer the file is being parsed from to the model'''
	data_reader_start_status_key = abstracts_log_name+".txt is being ported to dataframe"
	status_logger(status_logger_name, data_reader_start_status_key)

	textual_dataframe = pd.read_csv(abstracts_log_name+'_'+'CLEANED'+'.txt', delimiter="\t")

	data_reader_end_status_key = abstracts_log_name+".txt has been ported to dataframe"	
	status_logger(status_logger_name, data_reader_end_status_key)

	return textual_dataframe

def textual_data_trimmer(textual_dataframe, status_logger_name):
	'''Converts each of the abstracts in the file into a list element, of size = (number of abstracts)'''
	textual_data_trimmer_start_status_key = "Trimming data and preparing list of words"
	status_logger(status_logger_name, textual_data_trimmer_start_status_key)

	textual_data = textual_dataframe.values.tolist()

	textual_data_trimmer_end_status_key = "Trimmed data and prepared list of words"
	status_logger(status_logger_name, textual_data_trimmer_end_status_key)

	return textual_data

def sent_to_words(textual_data, status_logger_name):
	'''Removing unecessary characters and removing punctuations from the corpus. Resultant words are then tokenized.'''
	sent_to_words_start_status_key = "Tokenizing words"
	status_logger(status_logger_name, sent_to_words_start_status_key)

	for sentence in textual_data:
		yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))
	textual_data = list(sent_to_words(textual_data, status_logger_name))
	
	sent_to_words_end_status_key = "Tokenized words"
	status_logger(status_logger_name, sent_to_words_end_status_key)	

	return textual_data

def bigram_generator(textual_data, status_logger_name):
	'''Generating bigram model from the words that are in the corpus.'''
	'''Bigrams: Words that occur together with a high frequency,'''
	bigram_generator_start_status_key = "Generating word bigrams"
	status_logger(status_logger_name, bigram_generator_start_status_key)
	
	bigram = gensim.models.Phrases(textual_data, min_count=5, threshold=100)
	bigram_mod = gensim.models.phrases.Phraser(bigram)

	bigram_generator_end_status_key = "Generated word bigrams"
	status_logger(status_logger_name, bigram_generator_end_status_key)	

	return bigram_mod

def remove_stopwords(textual_data, status_logger_name):
	'''This function removes the standard set of stopwords from the corpus of abstract words.
	We've added a bunch of other words in addition.'''
	remove_stopwords_start_status_key = "Removing stopwords"
	status_logger(status_logger_name, remove_stopwords_start_status_key)
	
	return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in textual_data]
	
	remove_stopwords_end_status_key = "Removed stopwords"
	status_logger(status_logger_name, remove_stopwords_end_status_key)

def make_bigrams(textual_data, status_logger_name):
	'''Generates multiple bigrams of word pairs in phrases that commonly occuring with each other over the corpus'''
	make_bigrams_start_status_key = "Generating bigrams"
	status_logger(status_logger_name, make_bigrams_start_status_key)

	bigram_mod = bigram_generator(textual_data, status_logger_name)
	return [bigram_mod[doc] for doc in textual_data]
	
	make_bigrams_end_status_key = "Generated bigrams"
	status_logger(status_logger_name, make_bigrams_end_status_key)

def lemmatization(status_logger_name, textual_data, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
	'''Reducing a word to the root word. Running  -> Run for example'''
	lemmatization_start_status_key = "Beginning lemmatization"
	status_logger(status_logger_name, lemmatization_start_status_key)

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
	'''Running -> Run'''
	textual_data_lemmatized = lemmatization(status_logger_name, textual_data_words_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
	'''Creating a dictionary for each term as the key, and the value as their frequency in that sentence.'''
	id2word = corpora.Dictionary(textual_data_lemmatized)

	texts = textual_data_lemmatized
	'''Creating a dictionary for the entire corpus and not just individual abstracts and documents.'''
	corpus = [id2word.doc2bow(text) for text in texts]

	'''Builds the actual LDA model that will be used for the visualization and inference'''
	lda_model_generation_start_status_key = "Generating the LDA model using default parameter set"
	status_logger(status_logger_name, lda_model_generation_start_status_key)

	lda_model = gensim.models.ldamodel.LdaModel(corpus = corpus, id2word = id2word, num_topics = 10, random_state = 100, update_every = 1, chunksize = 100, passes = 10, alpha = 'auto', per_word_topics = True)

	lda_model_generation_end_status_key = "Generated the LDA model using default parameter set"
	status_logger(status_logger_name, lda_model_generation_end_status_key)

	perplexity_score = lda_model.log_perplexity(corpus)

	perplexity_status_key = "Issued perplexity:"+" "+str(perplexity_score)
	status_logger(status_logger_name, perplexity_status_key)

	nlp_engine_main_end_status_key = "Idling the NLP Engine"
	status_logger(status_logger_name, nlp_engine_main_end_status_key)

	'''Importing the visualizer_main function to view the LDA Model built by the NLP_engine_main() function'''
	visualizer_main(lda_model, corpus, id2word, logs_folder_name, status_logger_name)

	return 0