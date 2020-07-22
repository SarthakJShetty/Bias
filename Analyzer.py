'''This code is part of the larger Bias project, where we aim
to study the biases that exist in academic publications, and are building a 
web-tool to visualize these biases.

This portion of the code analyzes the contents of the .txt file developed
by the Scraper.py and saves it to a .csv for later visualization by the
soon to be built Visualizer.py script

Sarthak J. Shetty
01/09/2018'''

'''Importing OS here to split the filename at the extension'''
import os
'''Importing status_logger here to log the details of the process run.'''
from common_functions import status_logger
'''Importing the collections which contains the Counter function'''
from collections import Counter
'''Importing pandas here to build the dataframe'''
import pandas as pd
'''Importing numpy here to build the index of the pandas frameword'''
import numpy as np

def analyzer_pre_processing(abstracts_log_name, status_logger_name):
	'''Carries out the pre-processing tasks, such as folder creation'''
	analyzer_pre_processing_status_key="Carrying out pre-processing functions for analyzer"
	status_logger(status_logger_name, analyzer_pre_processing_status_key)
	
	'''This code strips the abstracts_log_name of its extension and adds a .csv to it'''
	abstracts_csv_file_name=(os.path.splitext(abstracts_log_name)[0])+"_"+"FREQUENCY_CSV_DATA"+".csv"
	abstracts_txt_file_name = abstracts_log_name+"_"+"CLEANED"+".txt"
	
	analyzer_pre_processing_status_key = "Carried out pre-processing functions for analyzer"
	status_logger(status_logger_name, analyzer_pre_processing_status_key)
	return abstracts_txt_file_name, abstracts_csv_file_name

def list_cleaner(list_to_be_cleaned, status_logger_name):
	list_cleaner_start_status_key = "Cleaning the list of words generated"
	status_logger(status_logger_name, list_cleaner_start_status_key)
	
	'''This function cleans the list containing the words found in the abstract. It eliminates words found in
	another pre-defined list of words.'''
	words_to_be_eliminated = ["the", "of", "and", "in", "to", "a", "is", "for", "from", "with", "that",	"by", "are", "on", "was", "as", "were", "url:", "abstract:",
	"abstract",  "author:", "title:", "at", "be", "an", "during", "have", "this", "which", "study", "been", "species", "not", "has", "between",
	"using", "its", "also", "these", "this", "used", "over", "can", "within", "into", "all","due", "use", "about", "a", 'it', 'their', "where", "we", "most", "may", "through",
	"though", "like", "or", "further", "e.g.", "along", "any", "those", "had", "toward", "due", "both", "some", "use", "even", "more", "but", "while", "pass", 
	"well", "will", "when", "only", "after", "author", "title", "there", "our", "did", "much", "as", "if", "become", "still", "various", "very", "out",
	"they", "via", "available", "such", "than", "different", "many", "areas", "no", "one", "two", "small", "first", "other", "such", "-", "could", "studies", "high",
	"provide", "among", "highly", "no", "case", "across", "given", "need", "would", "under", "found", "low", "values", "xe2\\x80\\x89", "xa", "xc", "xb", "\xc2\xa0C\xc2\xa0ha\xe2\x88\x921", "suggest", "up", "'The", "area"] 
	cleaned_list_of_words_in_abstract = [item for item in list_to_be_cleaned if item not in words_to_be_eliminated]

	list_cleaner_end_status_key = "Cleaned the list of words generated"
	status_logger(status_logger_name, list_cleaner_end_status_key)	

	return cleaned_list_of_words_in_abstract

def transfer_function(abstracts_txt_file_name, abstracts_csv_file_name, status_logger_name):
	'''This function is involved in the actual transfer of data from the .txt file to the .csv file'''
	transfer_function_status_key = "Copying data from"+" "+str(abstracts_txt_file_name)+" "+"to"+" "+"pandas dataframe"
	status_logger(status_logger_name, transfer_function_status_key)

	'''This list will contain all the words extracted from the .txt abstract file'''
	list_of_words_in_abstract=[]

	'''Each word is appended to the list, from the .txt file'''
	with open(abstracts_txt_file_name, 'r') as abstracts_txt_data:
		for line in abstracts_txt_data:
			for word in line.split():
				list_of_words_in_abstract.append(word)

	'''This function cleans up the data of uneccessary words'''
	cleaned_list_of_words_in_abstract = list_cleaner(list_of_words_in_abstract, status_logger_name)

	'''A Counter is a dictionary, where the value is the frequency of term, which is the key'''
	dictionary_of_abstract_list = Counter(cleaned_list_of_words_in_abstract)

	length_of_abstract_list = len(dictionary_of_abstract_list)

	'''Building a dataframe to hold the data from the list, which in turn contains the data from '''
	dataframe_of_abstract_words=pd.DataFrame(index=np.arange(0, length_of_abstract_list), columns=['Words', 'Frequency'])

	'''An element to keep tab of the number of elements being added to the list'''
	dictionary_counter = 0

	'''Copying elements from the dictionary to the pandas file'''
	for dictionary_element in dictionary_of_abstract_list:
		if(dictionary_counter==length_of_abstract_list):
			pass
		else:
			dataframe_of_abstract_words.loc[dictionary_counter, 'Words'] = dictionary_element
			dataframe_of_abstract_words.loc[dictionary_counter, 'Frequency'] = dictionary_of_abstract_list[dictionary_element]
			dictionary_counter = dictionary_counter+1

	transfer_function_status_key = "Copied data from"+" "+str(abstracts_txt_file_name)+" "+"to"+" "+"pandas dataframe"
	status_logger(status_logger_name, transfer_function_status_key)

	transfer_function_status_key = "Copying data from pandas dataframe to"+" "+str(abstracts_csv_file_name)
	status_logger(status_logger_name, transfer_function_status_key)

	'''Saving dataframe to csv file, without the index column'''
	dataframe_of_abstract_words.to_csv(abstracts_csv_file_name, index=False)

	transfer_function_status_key = "Copied data from pandas dataframe to"+" "+str(abstracts_csv_file_name)
	status_logger(status_logger_name, transfer_function_status_key)

def analyzer_main(abstracts_log_name, status_logger_name):
	'''Declaring the actual analyzer_main function is integrated to Bias.py code'''
	analyzer_main_status_key="Entered the Analyzer.py code."
	status_logger(status_logger_name, analyzer_main_status_key)

	'''Calling the pre-processing and transfer functions here'''
	abstracts_txt_file_name, abstracts_csv_file_name = analyzer_pre_processing(abstracts_log_name, status_logger_name)
	transfer_function(abstracts_txt_file_name, abstracts_csv_file_name, status_logger_name)

	'''Logs the end of the process Analyzer code in the status_logger'''
	analyzer_main_status_key="Exiting the Analyzer.py code."
	status_logger(status_logger_name, analyzer_main_status_key)