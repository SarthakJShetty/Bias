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
	abstracts_csv_file_name=(os.path.splitext(abstracts_log_name)[0])+"_"+"CSV_DATA"+".csv"
	abstracts_txt_file_name = abstracts_log_name+".txt"
	
	analyzer_pre_processing_status_key = "Carried out pre-processing functions for analyzer"
	status_logger(status_logger_name, analyzer_pre_processing_status_key)
	return abstracts_txt_file_name, abstracts_csv_file_name

def transfer_function(abstracts_txt_file_name, abstracts_csv_file_name, status_logger_name):
	'''This function is involved in the actual transfer of data from the .txt file to the .csv file'''
	#transfer_function_status_key="Copying data from"+" "+ str(abstracts_txt_file_name)+" "+"to"+" "+str(abstracts_csv_file_name)

	transfer_function_status_key = "Copying data from"+" "+str(abstracts_txt_file_name)+" "+"to"+" "+"pandas dataframe"
	status_logger(status_logger_name, transfer_function_status_key)

	'''This list will contain all the words extracted from the .txt abstract file'''
	list_of_words_in_abstract=[]

	'''Each word is appended to the list, from the .txt file'''
	with open(abstracts_txt_file_name, 'r') as abstracts_txt_data:
		for line in abstracts_txt_data:
			for word in line.split():
				list_of_words_in_abstract.append(word)

	'''A Counte is a dictionary, where the value is the frequency of term, which is the key'''
	dictionary_of_abstract_list = Counter(list_of_words_in_abstract)

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