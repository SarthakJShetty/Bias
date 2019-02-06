'''Hello! This portion of the code that acts as the processing code, it generates the dataframes suitable for visualization.

Sarthak J. Shetty
06/02/2019'''

from common_functions import status_logger

def abstract_word_sorter(abstract, abstract_title, abstract_year, permanent_word_sorter_dataframe, status_logger_name):
	abstract_word_sorter_start_status_key = "Adding:"+" "+abstract_title+" "+"to the permanent dataframe"
	status_logger(status_logger_name, abstract_word_sorter_start_status_key)
	'''This function creates the pandas dataframe that stores the text in the form of individual words
	against their year of appearence.'''

	'''Converting the abstract into a list of words'''
	abstract_word_list = abstract.split()
	'''We are directly porting the words from the list containing the abstract words to the permanent dataframe.
	We have resolved the issue involving the appending of the temporary dataframe onto the permanent dataframe.
	It works. It works.
	Edit: It did not work. The length of the permanent dataframe kept getting updated and hence we had to store its length in a seperate variable 
	before utilizing it as a counter in the for loop. An efficieny, but we cannot progress without it for now. 06/02/2019 -Sarthak '''
	length_of_permanent_word_sorter_dataframe = len(permanent_word_sorter_dataframe)
	for abstract_word_list_index in range(length_of_permanent_word_sorter_dataframe, (length_of_permanent_word_sorter_dataframe+len(abstract_word_list))):
		permanent_word_sorter_dataframe.loc[abstract_word_list_index, 'Words'] = abstract_word_list[abstract_word_list_index-length_of_permanent_word_sorter_dataframe]
		permanent_word_sorter_dataframe.loc[abstract_word_list_index, 'Year'] = abstract_year[:4]

	#print(len(abstract_word_list))
	#print(permanent_word_sorter_dataframe)
	abstract_word_sorter_end_status_key = "Added:"+" "+abstract_title+" "+"to the permanent dataframe"
	status_logger(status_logger_name, abstract_word_sorter_end_status_key)