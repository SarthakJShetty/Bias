'''Hello! This portion of the code that acts as the processing code corroborating with the main scripts [re: Scraper, Analyzer+NLP_Engine, Visualizer]

- Sarthak J. Shetty
06/02/2019'''

from common_functions import status_logger

def abstract_id_database_reader(abstract_id_log_name, site_url_index, status_logger_name):
	'''This function has been explicitly written to access
	the abstracts database that the given prgram generates.'''
	abstract_id_reader_temp_index = site_url_index
	abstract_id_database_reader_start_status_key = "Extracting Abstract IDs from disc"
	status_logger(status_logger_name, abstract_id_database_reader_start_status_key)

	lines_in_abstract_id_database=[line.rstrip('\n') for line in open(abstract_id_log_name+str(abstract_id_reader_temp_index+1)+'.txt')]

	abstract_id_database_reader_stop_status_key = "Extracted Abstract IDs from disc"
	status_logger(status_logger_name,abstract_id_database_reader_stop_status_key)

	return lines_in_abstract_id_database

def abstract_id_database_writer(abstract_id_log_name, abstract_input_tag_id, site_url_index):
	'''This function writes the abtract ids to a .txt file for easy access and documentation.'''
	abstract_id_writer_temp_index  = site_url_index
	abstract_id_log = open((abstract_id_log_name+str(abstract_id_writer_temp_index+1)+'.txt'), 'a')
	abstract_id_log.write(abstract_input_tag_id)
	abstract_id_log.write('\n')
	abstract_id_log.close()

def abstract_database_writer(abstract_page_url, title, author, abstract, abstracts_log_name, abstract_date, status_logger_name):
	'''This function makes text files to contain the abstracts for future reference.
	It holds: 1) Title, 2) Author(s), 3) Abstract'''
	abstract_database_writer_start_status_key = "Writing"+" "+title+" "+"by"+" "+author+" "+"to disc"
	status_logger(status_logger_name, abstract_database_writer_start_status_key)
	abstracts_csv_log = open(abstracts_log_name+'.csv', 'a')
	abstracts_txt_log = open(abstracts_log_name+'.txt', 'a')
	abstracts_txt_log.write("Title:"+" "+title)
	abstracts_txt_log.write('\n')
	abstracts_txt_log.write("Author:"+" "+author)
	abstracts_txt_log.write('\n')
	abstracts_txt_log.write("Date:"+" "+abstract_date)
	abstracts_txt_log.write('\n')
	abstracts_txt_log.write("URL:"+" "+abstract_page_url)
	abstracts_txt_log.write('\n')
	abstracts_txt_log.write("Abstract:"+" "+abstract)
	abstracts_csv_log.write(abstract)
	abstracts_csv_log.write('\n')
	abstracts_txt_log.write('\n'+'\n')
	abstracts_txt_log.close()
	abstracts_csv_log.close()
	abstract_database_writer_stop_status_key = "Written"+" "+title+" "+"to disc"
	status_logger(status_logger_name, abstract_database_writer_stop_status_key)

def abstract_word_extractor(abstract, abstract_title, abstract_year, permanent_word_sorter_dataframe, status_logger_name):
	'''This function creates the pandas dataframe that stores the text in the form of individual words
	against their year of appearence.'''
	abstract_word_sorter_start_status_key = "Adding:"+" "+abstract_title+" "+"to the permanent dataframe"
	status_logger(status_logger_name, abstract_word_sorter_start_status_key)

	'''Converting the abstract into a list of words'''
	abstract_word_list = abstract.split()
	'''This line of code lowers the entire abstract to lower case. This list is then fed into the dataframe.'''
	abstract_word_list = [element.lower() for element in abstract_word_list]
	'''This line of code sorts the elements in the word list alphabetically. Working with dataframes is harden, hence
	we are curbing this issue by modifying the list rather.'''
	abstract_word_list.sort()

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