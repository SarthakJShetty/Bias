'''Hello! This code code is part of the Bias project, where we are trying to prove the existence
of certain biases in academic publications.
We will be displaying the results from the NLP_Engine.py code here, using primarily using pyLDAvis library.

Check out the repository build-log.md for a more detailed report of the code working.
Check out the repository README.md for a high-level overview of the project and the objective.

Sarthak J. Shetty
24/11/2018'''
from common_functions import status_logger
'''import matplotlib as plt'''
import matplotlib.pyplot as plt
import pyLDAvis

def visualizer_generator(lda_model, corpus, id2word, logs_folder_name, status_logger_name):
	'''This code generates the .html file with generates the visualization of the data prepared.'''
	visualizer_generator_start_status_key = "Preparing the visualization"
	status_logger(status_logger_name, visualizer_generator_start_status_key)
	textual_data_visualization = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
	pyLDAvis.save_html(textual_data_visualization, logs_folder_name+"/"+"Data_Visualization.html")
	visualizer_generator_end_status_key = "Prepared the visualization"
	status_logger(status_logger_name, visualizer_generator_end_status_key)		

def trends_histogram(abstract_word_dictionary, trend_keywords, status_logger_name):
	#This function is responsible for generating the histograms to visualizations the trends in research topics.'''
	trends_histogram_start_status_key = "Generating the trends histogram"
	status_logger(status_logger_name, trends_histogram_start_status_key)
	'''What's happening here?
	a) The key of the dictionary is being looped over by the for statement.
	b) The key is split at the comma to get two values, i) word, ii) year.
	c) The word is used as an element of the comporator function; i.e. checking if the trend keyword is the word that is being
	checked for in the dictionary.
	d) If the element is equal to the element in the dictionary, then the year and the frequency is transferred to the plot function.'''
	'''print(type(abstract_word_dictionary))'''
	list_of_years = []
	for element in abstract_word_dictionary:
		abstract_word = element.split(',')[0]
		year_of_occurence = element.split(',')[1]
		if(abstract_word==trend_keywords):
			list_of_years.append(year_of_occurence+','+abstract_word_dictionary[element])
		else:
			list_of_years.append(year_of_occurence+','+str(0))
	list_of_years.sort()
	print(list_of_years)

	sorted_list_of_years = []
	frequncy_in_years = []
	for element in list_of_years:
		occuring_year = element.split(',')[0]
		frequency_of_occurence = element.split(',')[1]
		sorted_list_of_years.append(occuring_year)
		frequncy_in_years.append(frequency_of_occurence)
	print(sorted_list_of_years)
	print(frequncy_in_years)
	plt.plot(sorted_list_of_years, frequncy_in_years, 'ro')
	plt.show()

	trends_histogram_end_status_key = "Generating the trends histogram"
	status_logger(status_logger_name, trends_histogram_end_status_key)
			
def visualizer_main(abstract_word_dictionary, trend_keywords, lda_model, corpus, id2word, logs_folder_name, status_logger_name):
	visualizer_main_start_status_key = "Entering the visualizer_main() code"
	status_logger(status_logger_name, visualizer_main_start_status_key)

	'''This the main visualizer code. Reorging this portion of the code to ensure modularity later on as well.'''
	visualizer_generator(lda_model, corpus, id2word, logs_folder_name, status_logger_name)
	'''Trends visualizer is called to generate the '''
	trends_histogram(abstract_word_dictionary, trend_keywords, status_logger_name)

	visualizer_main_end_status_key = "Exiting the visualizer_main() code"
	status_logger(status_logger_name, visualizer_main_end_status_key)