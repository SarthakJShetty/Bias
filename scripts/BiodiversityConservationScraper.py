#!/usr/bin/env python
# coding: utf-8

# ### Scraper Script

# This script is a stripped down version of the [Scraper.py](https://github.com/SarthakJShetty/Bias/blob/master/Scraper.py) code that is used to generate the dataset for analyses of research trends. It's a small piece of the larger [Bias](https://GitHub.com/SarthakJShetty/Bias) project.

# Specifically, this script scrapes the [Biodeiversity and Conservation Journal](https://link.springer.com/journal/10531), published by Springer. This code is reactive & unstable, and is tangential to our [Bias](https://github.com/SarthakJShetty/Bias) project.

# ### 1.0 <u>Code</u>

# Here we are importing the libraries required to run the scraping code. We are retrieving the abstacts, paper title and author names from [Springer](https://link.springer.com).

# In[1]:


from urllib.request import urlopen
''''Importing urllib.error to handle errors in HTTP pinging.'''
import urllib.error
'''BeautifulSoup is used for souping.'''
from bs4 import BeautifulSoup
'''Counter generates a dictionary from the abstract data, providing frequencies of occurences'''
from collections import Counter
'''Importing the CSV library here to dump the dictionary for further analysis and error checking if required. Will edit it out later.'''
import csv
'''Importing datetime for logging of various function executions'''
from datetime import datetime
'''Importing numpy to generate a random integer for the delay_function (see below)'''
import numpy as np
'''This library is imported to check if we can feasibly introduce delays into the processor loop to reduce instances of the remote server, shutting the connection while scrapping extraordinarily large datasets.'''
import time
'''This library is imported to build the LOG folders and directories'''
import os


# Declaring the ```keywords``` variable here, which is topic that the scrapping will take place on. It will be appended to the start and abstract URLs during retrival. Also defining the ```trend_keywords``` term here, whose frequency is to be studied using the trends chart.

# In[2]:


keywords_to_search="Biodiversity and Conservation"
keywords_to_search = keywords_to_search.split()
trend_keywords="Conservation"


# From here, we define the functions that are responsible for pinging, retriving and storing the information and the meta-data collected from the Springer scrapping.

# This function carries out a number of functions, including creating the holding directrories, declaration of variables like ```start_url``` and ```abstract_url```.

# In[3]:


def pre_processing(keywords):
	'''This function contains all the pre-processing statements related to the running of the program, including:
	1. Default starter URL of the page to scrape.
	2. Default location of LOGS, including:
		1. Location of Abstract_ID_Database
		2. Location of Abstract_Database'''

	'''Declaring the time and date variables here. Year, month, day, hours, minute & seconds.'''
	run_start_year = str(datetime.now().date().year)
	run_start_month = str(datetime.now().date().month)
	run_start_day = str(datetime.now().date().day)
	run_start_date = str(datetime.now().date())
	run_start_hour = str(datetime.now().time().hour)
	run_start_minute = str(datetime.now().time().minute)
	run_start_second = str(datetime.now().time().second)
	'''Keywords have to be written into the filename of the LOG that we are running'''
	folder_attachement = ""
	if(len(keywords)==1):
		folder_attachement = keywords[0]
	else:
		for keyword_index in range(0, len(keywords)):
			if((keyword_index+1)==len(keywords)):
				folder_attachement = folder_attachement+keywords[keyword_index]
			else:
				folder_attachement = folder_attachement+keywords[keyword_index]+"_"
	'''Declaring the LOG folder and the abstract, abstract_id & status_logger files.'''
	logs_folder_name = "LOGS"+"/"+"LOG"+"_"+run_start_date+'_'+run_start_hour+'_'+run_start_minute+"_"+folder_attachement
	abstract_id_log_name =logs_folder_name+"/"+'Abstract_ID_Database'+'_'+run_start_date+'_'+run_start_hour+'_'+run_start_minute+"_"
	abstracts_log_name = logs_folder_name+"/"+'Abstract_Database'+'_'+run_start_date+'_'+run_start_hour+'_'+run_start_minute
	status_logger_name = logs_folder_name+"/"+'Status_Logger'+'_'+run_start_date+'_'+run_start_hour+'_'+run_start_minute

	'''If the filename does not exist create the file in the LOG directory'''
	if not os.path.exists(logs_folder_name):
		os.makedirs(logs_folder_name)
	
	'''Creating the status_log and writing the session duration & date'''
	status_log = open(status_logger_name+'.txt', 'a')
	status_log.write("Session:"+" "+run_start_day+"/"+run_start_month+"/"+run_start_year+"\n")
	status_log.write("Time:"+" "+run_start_hour+":"+run_start_minute+":"+run_start_second+"\n")
	status_log.close()

	logs_folder_name_status_key = "Built LOG folder for session"
	status_logger(status_logger_name, logs_folder_name_status_key)

	query_string = ""
	if (len(keywords)==1):
		query_string = keywords[0]
	else:
		for keyword_index in range(0, len(keywords)):
			if((keyword_index+1)==len(keywords)):
				query_string = query_string+keywords[keyword_index]
			else:
				query_string = query_string+keywords[keyword_index]+"+"

	'''These variables have to be changed accordingly depending on the journal being scrapped.'''
	start_url = 'https://link.springer.com/search/page/'
	abstract_url = 'https://link.springer.com'

	return abstract_id_log_name, abstracts_log_name, start_url, abstract_url, query_string, logs_folder_name, status_logger_name


# Defining the ```status_logger()``` function here which will log the functioning of all the individual modules. Primarily designed to improve diagnostics of the code once the scrapping has commenced.

# In[4]:


def status_logger(status_logger_name, status_key):
	'''Status logger to print and log details throught the running the program.
	Declaring current_hour, current_minute & current_second.'''
	current_hour = str(datetime.now().time().hour)
	current_minute = str(datetime.now().time().minute)
	current_second = str(datetime.now().time().second)
	'''Logging the complete_status_key and printing the complete_status_key'''
	complete_status_key = "[INFO]"+current_hour+":"+current_minute+":"+current_second+" "+status_key
	print(complete_status_key)
	status_log = open(status_logger_name+'.txt', 'a')
	status_log.write(complete_status_key+"\n")
	status_log.close()


# The ```pre_processing()``` function is responsible for setting up the fundamental files and variables required to get the scrapper up and running.

# In[5]:


abstract_id_log_name, abstracts_log_name, start_url, abstract_url, query_string, logs_folder_name, status_logger_name = pre_processing(keywords_to_search)


# This function is responsible for reading the pages using the ```urlopen``` function. If an error is encountered (i.e. ```UnboundLocalError```) the encountered is passed.

# In[6]:


def url_reader(url, status_logger_name):
	'''This keyword is supplied to the URL and is hence used for souping.
	Encountered an error where some links would not open due to HTTP.error
	This is added here to try and ping the page. If it returns false the loop ignores it and
	moves on to the next PII number'''
	try:
		page=urlopen(url)
		page_status(page, status_logger_name)
		return page
	except (UnboundLocalError, urllib.error.HTTPError):
		pass


# This function determines the number of articles are to be scrapped. This value is stored in the ```number_of_results``` variable.

# In[7]:


def results_determiner(url, status_logger_name):
	'''This function determines the number of results that a particular keywords returns
	once it looks up the keyword on link.springer.com
	The function returns all the possible links containing results and then provides the total number of results
	returned by a particular keyword, or combination of keywords.'''
	first_page_to_scrape = urlopen(url)
	first_page_to_scrape_soup = BeautifulSoup(first_page_to_scrape, 'html.parser')
	number_of_results = first_page_to_scrape_soup.find('h1', {'id':'number-of-search-results-and-search-terms'}).find('strong').text


# This function generates the ```urls``` that are to be scrapped systematically. We have defined a ```determiner``` variable here as well, which retrieves the number of pages that a particular result returns.

# In[8]:


def url_generator(start_url, query_string, status_logger_name):
	'''This function is written to scrape all possible webpages of a given topic
	The search for the URLs truncates when determiner variable doesn't return a positive value'''
	'''Initiallizing a list here in order to contain the URLs. Even if a URL does not return valid results,
	it is popped later on from the list.'''
	urls_to_scrape=[]
	counter = 0
	total_url = start_url+str(counter)+"?search-within=Journal&facet-journal-id=10531&query="
	initial_url_status_key = total_url+" "+"has been obtained"
	status_logger(status_logger_name, initial_url_status_key)
	urls_to_scrape.append(total_url)
	test_soup = BeautifulSoup(urlopen(total_url), 'html.parser')
	determiner = int(test_soup.find('span', {'class':'number-of-pages'}).text)
	'''This while loop continuously pings and checks for new webpages, then stores them for scraping'''
	while(counter <= determiner):
		counter = counter+1
		total_url = start_url+str(counter)+"?search-within=Journal&facet-journal-id=10531&query="
		url_generator_while_status_key=total_url+" "+"has been obtained"
		status_logger(status_logger_name, url_generator_while_status_key)
		soup = BeautifulSoup(urlopen(total_url), 'html.parser')
		urls_to_scrape.append(total_url)
	urls_to_scrape.pop(len(urls_to_scrape)-1)
	return urls_to_scrape


# This function checks the publishes the status of the page, borrowing functionality from the ```page.status``` tool available with ```urllib.request```

# In[9]:


def page_status(page, status_logger_name):
	'''Prints the page status. Will be used whenever a new webpage is picked for scraping.'''
	page_status_key = "Page status:"+" "+str(page.status)
	status_logger(status_logger_name, page_status_key)


# This function soups the page before retrieving the abstracts of the publications.

# In[10]:


def page_souper(page, status_logger_name):
	'''Function soups the webpage elements and provided the tags for search.
	Note: Appropriate encoding has to be picked up beenfore souping'''
	page_souper_start_status_key = "Souping page"
	status_logger(status_logger_name, page_souper_start_status_key)
	page_soup = BeautifulSoup(page, 'html.parser')
	page_souper_stop_status_key = "Souped page"
	status_logger(status_logger_name, page_souper_stop_status_key)
	return page_soup


# This function stores each word encountered in an abstract against the year of occurance. Pre-processing within the function includes lowereing all words and sorting.

# In[11]:


def abstract_word_extractor(abstract, abstract_title, abstract_year, permanent_word_sorter_list, trend_keywords, status_logger_name):
	'''This function creates the list that stores the text in the form of individual words
	against their year of appearence.'''
	abstract_word_sorter_start_status_key = "Adding:"+" "+abstract_title+" "+"to the archival list"
	status_logger(status_logger_name, abstract_word_sorter_start_status_key)
	'''This line of code converts the entire abstract into lower case'''
	abstract = abstract.lower()
	'''Converting the abstract into a list of words'''
	abstract_word_list = abstract.split()
	'''This line of code sorts the elements in the word list alphabetically. Working with dataframes is harden, hence
	we are curbing this issue by modifying the list rather.'''
	abstract_word_list.sort()
	'''If the word currently being looped in the abstract list matches the trend word being investigated for, the year it appears
	is appended to the permanent word sorter list'''
	for element in abstract_word_list:
		if(element==trend_keywords[0]):
			permanent_word_sorter_list.append(abstract_year[:4])

	abstract_word_sorter_end_status_key = "Added:"+" "+abstract_title+" "+"to the archival list"
	status_logger(status_logger_name, abstract_word_sorter_end_status_key)


# This function counts the occurance of each term, in each year and forms a well organized form, comprising of keywords, against their year for different years. This is used for the trends plotter function as well.

# In[12]:


def abstract_year_list_post_processor(permanent_word_sorter_list, status_logger_name):
	'''Because of this function we have a dictionary containing the frequency of occurrence of terms in specific years'''
	abstract_year_list_post_processor_start_status_key = "Post processing of permanent word sorter list has commenced"
	status_logger(status_logger_name, abstract_year_list_post_processor_start_status_key)

	starting_year = min(permanent_word_sorter_list)
	ending_year = max(permanent_word_sorter_list)

	abstract_year_dictionary = Counter(permanent_word_sorter_list)

	abstract_year_list_post_processor_end_status_key = "Post processing of permanent word sorter list has completed"
	status_logger(status_logger_name, abstract_year_list_post_processor_end_status_key)

	return abstract_year_dictionary, starting_year, ending_year


# The abstract dictionary returned by the previous function is dumped as a ```.csv``` file to the disc.

# In[13]:


def abstract_year_dictionary_dumper(abstract_word_dictionary, abstracts_log_name, status_logger_name):
	'''This function saves the abstract word dumper to the disc for further inspection.
	The file is saved as a CSV bucket and then dumped.'''
	permanent_word_sorter_list_start_status_key = "Dumping the entire dictionary to the disc"
	status_logger(status_logger_name, permanent_word_sorter_list_start_status_key)
	with open(abstracts_log_name+"_"+"DICTIONARY.csv", 'w') as dictionary_to_csv:
		writer = csv.writer(dictionary_to_csv)
		for key, value in abstract_word_dictionary.items():
			year = key
			writer.writerow([year, value])
	
	permanent_word_sorter_list_end_status_key = "Dumped the entire dictionary to the disc"
	status_logger(status_logger_name, permanent_word_sorter_list_end_status_key)


# Moving away from the post processing function, in this function we scrape meta-data including title, data and author name. This function is a container that connects a number of other functions spread across the notebook.

# In[14]:


def abstract_page_scraper(abstract_url, abstract_input_tag_id, abstracts_log_name, permanent_word_sorter_list, trend_keywords, site_url_index, status_logger_name):
	'''This function is written to scrape the actual abstract of the specific paper,
	 that is being referenced within the list of abstracts'''
	abstract_page_scraper_status_key="Abstract ID:"+" "+abstract_input_tag_id
	status_logger(status_logger_name, abstract_page_scraper_status_key)
	abstract_page_url = abstract_url+abstract_input_tag_id
	abstract_page = url_reader(abstract_page_url, status_logger_name)
	abstract_soup = page_souper(abstract_page, status_logger_name)
	title = title_scraper(abstract_soup, status_logger_name)
	abstract_date = abstract_date_scraper(title, abstract_soup, status_logger_name)

	'''Due to repeated attribute errors with respect to scraping the authors name, these failsafes had to be put in place.'''
	try:
		author = author_scraper(abstract_soup, status_logger_name)
	except AttributeError:
		author = "Author not available"

	'''Due to repeated attribute errors with respect to scraping the abstract, these failsafes had to be put in place.'''
	try:
		abstract = abstract_scraper(abstract_soup)
		abstract_word_extractor(abstract, title, abstract_date, permanent_word_sorter_list, trend_keywords, status_logger_name)
	except AttributeError:
		abstract = "Abstract not available"

	abstract_database_writer(abstract_page_url, title, author, abstract, abstracts_log_name, abstract_date, status_logger_name)
	analytical_abstract_database_writer(title, author, abstract, abstracts_log_name, status_logger_name)


# This is the main function which organizes the scrapping, and coordinates with the above function. The ```delay_function()``` is also inscribed here.

# In[15]:


def abstract_crawler(abstract_url, abstract_id_log_name, abstracts_log_name, permanent_word_sorter_list, trend_keywords, site_url_index, status_logger_name):
	abstract_crawler_temp_index  = site_url_index
	'''This function crawls the page and access each and every abstract'''
	abstract_input_tag_ids = abstract_id_database_reader(abstract_id_log_name, abstract_crawler_temp_index, status_logger_name)
	for abstract_input_tag_id in abstract_input_tag_ids:
		try:
			abstract_crawler_accept_status_key="Abstract Number:"+" "+str((abstract_input_tag_ids.index(abstract_input_tag_id)+1)+abstract_crawler_temp_index*20)
			status_logger(status_logger_name, abstract_crawler_accept_status_key)
			abstract_page_scraper(abstract_url, abstract_input_tag_id, abstracts_log_name, permanent_word_sorter_list, trend_keywords, site_url_index, status_logger_name)
			'''Introduces a 5 second delay between successive pings.'''
			delay_function(status_logger_name)
		except TypeError:
			abstract_crawler_reject_status_key="Abstract Number:"+" "+str(abstract_input_tag_ids.index(abstract_input_tag_id)+1)+" "+"could not be processed"
			status_logger(status_logger_name, abstract_crawler_reject_status_key)
			pass


# This ```.txt``` file contains only the abstract and passes it over to the ```NLP_Engine``` script before plotting the visualizations. This way, a lot of edge cases in formatting are avoided.

# In[16]:


def analytical_abstract_database_writer(title, author, abstract, abstracts_log_name, status_logger_name):
	'''This function will generate a secondary abstract file that will contain only the abstract.
	The  abstract file generated will be passed onto the Visualizer and Analyzer function, as opposed to the complete 
	abstract log file containing lot of garbage words in addition to the abstract text.'''
	analytical_abstract_database_writer_start_status_key = "Writing"+" "+title+" "+"by"+" "+author+" "+"to analytical abstracts file"
	status_logger(status_logger_name, analytical_abstract_database_writer_start_status_key)

	analytical_abstracts_txt_log = open(abstracts_log_name+'_'+'ANALYTICAL'+'.txt', 'a')
	analytical_abstracts_txt_log.write(abstract)
	analytical_abstracts_txt_log.write('\n'+'\n')
	analytical_abstracts_txt_log.close()

	analytical_abstract_database_writer_stop_status_key = "Written"+" "+title+" "+"to disc"
	status_logger(status_logger_name, analytical_abstract_database_writer_stop_status_key)


# This is the ```.txt``` and ```.csv``` writers that holds all the data, including meta-data alongwith abstracts; Primarily for readability.

# In[17]:


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


# This function reads the abstract ID's from the .txt file where they are saved. Retrieved values are appended  to the ```abstract_start_urls``` to scrape the abstract and meta-data.

# In[18]:


def abstract_id_database_reader(abstract_id_log_name, site_url_index, status_logger_name):
	'''This function has been explicitly written to access
	the abstracts database that the given prgram generates.'''
	abstract_id_reader_temp_index = site_url_index
	abstract_id_database_reader_start_status_key = "Extracting Abstract IDs from disc"
	status_logger(status_logger_name, abstract_id_database_reader_start_status_key)

	lines_in_abstract_id_database=[line.rstrip('\n') for line in open(abstract_id_log_name+str(abstract_id_reader_temp_index+1)+'.txt')]

	abstract_id_database_reader_stop_status_key = "Extracted Abstract IDs from disc"
	status_logger(status_logger_name, abstract_id_database_reader_stop_status_key)

	return lines_in_abstract_id_database


# This function stores the ```abstract_ids``` for reference, and also for accessing across functions. This ensures reusability of stored values.

# In[19]:


def abstract_id_database_writer(abstract_id_log_name, abstract_input_tag_id, site_url_index):
	'''This function writes the abtract ids to a .txt file for easy access and documentation.'''
	abstract_id_writer_temp_index  = site_url_index
	abstract_id_log = open((abstract_id_log_name+str(abstract_id_writer_temp_index+1)+'.txt'), 'a')
	abstract_id_log.write(abstract_input_tag_id)
	abstract_id_log.write('\n')
	abstract_id_log.close()


# Seld-explanatory, scrapes the abstract data as meta-data.

# In[20]:


def abstract_date_scraper(title, abstract_soup, status_logger_name):
	'''This function scrapes the date associated with each of the abstracts.
	This function will play a crucial role in the functionality that we are trying to build into our project.'''
	date_scraper_entry_status_key = "Scraping date of the abstract titled:"+" "+title
	status_logger(status_logger_name, date_scraper_entry_status_key)
	try:
		abstract_date = abstract_soup.find('time').get('datetime')
		date_scraper_exit_status_key = title+" "+"was published on"+" "+abstract_date
	except AttributeError:
		abstract_date = "Date for abstract titled:"+" "+title+" "+"was not available"
		date_scraper_exit_status_key = abstract_date
		pass
	
	status_logger(status_logger_name, date_scraper_exit_status_key)
	return abstract_date


# Checks for the ```<p>``` tag corresponding to the abstract and returns them to the main function where it's being called.

# In[21]:


def abstract_scraper(abstract_soup):
	'''This function scrapes the abstract from the soup and returns to the page scraper'''
	try:
		abstract = str(abstract_soup.find('p', {'id':'Par1'}).text.encode('utf-8'))[1:]
	except AttributeError:
		abstract = str(abstract_soup.find('p', {'class':'Para'}).text.encode('utf-8'))[1:]
	return abstract


# Once again, self-explanatory, meta-data component scrapping the author of the publication.

# In[22]:


def author_scraper(abstract_soup, status_logger_name):
	'''This function scrapes the author of the text, for easy navigation and search'''
	author_scraper_start_status_key = "Scraping the author name"
	status_logger(status_logger_name, author_scraper_start_status_key)
	author = str(abstract_soup.find('span', {'class':'authors__name'}).text.encode('utf-8'))[1:]
	author_scraper_end_status_key = "Scraped the author name"
	status_logger(status_logger_name, author_scraper_end_status_key)
	return author


# Once again, self-explanatory, meta-data component scrapping the title of the publication.

# In[23]:


def title_scraper(abstract_soup, status_logger_name):
	'''This function scrapes the title of the text'''
	title_scraper_start_status_key = "Scraping the title of the abstract"
	status_logger(status_logger_name, title_scraper_start_status_key)
	try:
		title = str(abstract_soup.find('h1',{'class':'ArticleTitle'}).text.encode('utf-8'))[1:]
	except AttributeError:
		title = str(abstract_soup.find('h1',{'class':'ChapterTitle'}).text.encode('utf-8'))[1:]
	title_scraper_end_status_key = "Scraped the title of the abstract"
	status_logger(status_logger_name, title_scraper_end_status_key)
	return title


# Scrapes the ```abstract_id``` from the results page and passes them over to the writers for reference by other functions.

# In[ ]:


def abstract_id_scraper(abstract_id_log_name, page_soup, site_url_index, status_logger_name):
	'''This function helps in obtaining the PII number of the abstract.
	This number is then coupled with the dynamic URL and provides'''

	abstract_id_scraper_start_status_key="Scraping IDs"
	status_logger(status_logger_name, abstract_id_scraper_start_status_key)
	''''This statement collects all the input tags that have the abstract ids in them'''
	abstract_input_tags = page_soup.findAll('a', {'class':'title'})
	for abstract_input_tag in abstract_input_tags:
		abstract_input_tag_id=abstract_input_tag.get('href')
		abstract_id_database_writer(abstract_id_log_name, abstract_input_tag_id, site_url_index)

	abstract_id_scraper_stop_status_key="Scraped IDs"
	status_logger(status_logger_name, abstract_id_scraper_stop_status_key)


# Creating the list that saves the words occuring in each and every abstract.

# In[ ]:


def word_sorter_list_generator(status_logger_name):
	word_sorter_list_generator_start_status_key = "Generating the permanent archival list"
	status_logger(status_logger_name, word_sorter_list_generator_start_status_key)
	'''This function generates the list that hold the Words and corresponding Years of the
	abstract data words before the actual recursion of scrapping data from the website begins.'''
	word_sorter_list = []

	word_sorter_list_generator_exit_status_key = "Generated the permanent archival list"
	status_logger(status_logger_name, word_sorter_list_generator_exit_status_key)
	return word_sorter_list


# Delays pings between intermediary pings to the webpage server. Makes it more human, not bot-ish.

# In[ ]:


def delay_function(status_logger_name):
	'''Since the Springer servers are contstantly shutting down the remote connection, we introduce
	this function in the processor function in order to reduce the number of pings it delivers to the remote.'''
	delay_variable = np.random.randint(0, 20)
	'''Sleep parameter causes the code to be be delayed by random number of seconds'''
	delay_function_start_status_key = "Delaying remote server ping:"+' '+str(delay_variable)+' '+" seconds"
	status_logger(status_logger_name, delay_function_start_status_key)
	time.sleep(delay_variable)
	delay_function_end_status_key = "Delayed remote server ping:"+' '+str(delay_variable)+' '+" seconds"
	status_logger(status_logger_name, delay_function_end_status_key)


# Collects the site urls and cycles through them one by one. Penultimate main function in the script.

# In[ ]:


def processor(abstract_url, urls_to_scrape, abstract_id_log_name, abstracts_log_name, status_logger_name, trend_keywords, keywords_to_search):
	''''Multiple page-cycling function to scrape multiple result pages returned from Springer.
	print(len(urls_to_scrape))'''
	
	'''This list will hold all the words mentioned in all the abstracts. It will be later passed on to the
	visualizer code to generate the trends histogram.'''
	permanent_word_sorter_list = word_sorter_list_generator(status_logger_name)

	for site_url_index in range(0, len(urls_to_scrape)):

		if(site_url_index==0):
			results_determiner(urls_to_scrape[site_url_index], status_logger_name)
		'''Collects the web-page from the url for souping'''
		page_to_soup = url_reader(urls_to_scrape[site_url_index], status_logger_name)
		'''Souping the page for collection of data and tags'''
		page_soup = page_souper(page_to_soup, status_logger_name)
		'''Scrapping the page to extract all the abstract IDs'''
		abstract_id_scraper(abstract_id_log_name, page_soup, site_url_index, status_logger_name)
		'''Actually obtaining the abstracts after combining ID with the abstract_url'''
		abstract_crawler(abstract_url, abstract_id_log_name, abstracts_log_name, permanent_word_sorter_list, trend_keywords, site_url_index, status_logger_name)

	'''This line of code processes and generates a dictionary from the abstract data'''
	
	abstract_year_dictionary, starting_year, ending_year = abstract_year_list_post_processor(permanent_word_sorter_list, status_logger_name)

	return abstract_year_dictionary, starting_year, ending_year


# Main function where all the magic happens. URLs are scrapped and collected, passed over to the ```processor()``` and then the data obtained are dumped into the database.

# In[ ]:


def scraper_main(abstract_id_log_name, abstracts_log_name, start_url, abstract_url, query_string, trend_keywords, keywords_to_search, status_logger_name):
	''''This function contains all the functions and contains this entire script here, so that it can be imported later to the main function'''

	'''Provides the links for the URLs to be scraped by the scraper'''
	urls_to_scrape = url_generator(start_url, query_string, status_logger_name)
	'''Calling the processor() function here'''
	abstract_year_dictionary, starting_year, ending_year = processor(abstract_url, urls_to_scrape, abstract_id_log_name, abstracts_log_name, status_logger_name, trend_keywords, keywords_to_search)
	'''This function dumps the entire dictionary onto the disc for further analysis and inference.'''
	abstract_year_dictionary_dumper(abstract_year_dictionary, abstracts_log_name, status_logger_name)
	'''Returning the abstract word dictionary here'''
	return abstract_year_dictionary, starting_year, ending_year


# Calling the ```scraper_main()``` function here.

# In[ ]:


scraper_main(abstract_id_log_name, abstracts_log_name, start_url, abstract_url, query_string, trend_keywords, keywords_to_search, status_logger_name)

