'''Hello! This is the third (UPDATE 1.0: Correction, IT IS THE FOURTH PROJECT!) project that I've started in two months.
Feels great to learn so many new concepts.
Here's to never stop learning.

The aim of the project is to measure (quantitatively) the disparity in the the publications
pertaining to the natural history and ecology of specific geographical regions.

More info will be added here. Soon.

Sarthak J. Shetty
04/08/2018'''

'''Adding the libraries to be used here.'''

'''urllib2 has since lost support and urllib.request has replaced it. urlopen has been borrowed from there.'''
from urllib.request import urlopen
''''Importing urllib.error to handle errors in HTTP pinging.'''
import urllib.error
'''BeautifulSoup is used for souping.'''
from bs4 import BeautifulSoup
'''datetime is used while building the database logs'''
from datetime import datetime
'''Used to create the database log'''
import os
'''argparse has been imported to extract keyword(s)'''
import argparse

def arguments_parser():
	'''This function is used to read the initial keyword that will be queried in ScienceDirect (for now).
	We will be scrapping Science, Nature etc later, as long as generic URLs are supported.'''
	parser = argparse.ArgumentParser()
	parser.add_argument("--keywords", help="Keyword to search on ScienceDirect", default="Tiger")
	arguments = parser.parse_args()
	if arguments.keywords:
		keywords = arguments.keywords
	keywords = keywords.split()
	return keywords

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
				query_string = query_string+keywords[keyword_index]+"%20"
	start_url = "https://www.sciencedirect.com/search?qs="+query_string+"&show=100&sortBy=relevance&accessTypes=openaccess%2Copenarchive&offset="
	urls_to_scrape = url_generator(start_url, status_logger_name)
	abstract_url = 'https://www.sciencedirect.com/science/article/pii/'

	return abstract_url, urls_to_scrape, abstract_id_log_name, abstracts_log_name, status_logger_name

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

def url_reader(url):
	'''This keyword is supplied to the URL and is hence used for souping.''' 
	'''Encountered an error where some links would not open due to HTTP.error
	This is added here to try and ping the page. If it returns false the loop ignores it and
	moves on to the next PII number'''
	try:
		page=urlopen(url)
		page_status(page)
		return page
	except (UnboundLocalError, urllib.error.HTTPError):
		pass

def url_generator(start_url, status_logger_name):
	'''This function is written to scrape all possible webpages of a given topic
	The search for the URLs truncates when determiner doesn't return a positive value'''
	url_generator_start_status_key = start_url+" "+"start_url has been received"
	status_logger(status_logger_name, url_generator_start_status_key)
	urls_to_scrape=[]
	counter = 0
	total_url = start_url+str(counter)
	initial_url_status_key = total_url+" "+"has been obtained"
	status_logger(status_logger_name, initial_url_status_key)
	urls_to_scrape.append(total_url)
	test_soup = BeautifulSoup(urlopen(total_url), 'html.parser')
	determiner = test_soup.find('ol', {'class':'search-result-wrapper'})
	'''This while loop continuously pings and checks for new webpages, then stores them for scraping'''
	while(determiner):
		counter = counter+100
		total_url = start_url+str(counter)
		url_generator_while_status_key=total_url+" "+"has been obtained"
		status_logger(status_logger_name, url_generator_while_status_key)
		soup = BeautifulSoup(urlopen(total_url), 'html.parser')
		determiner = soup.find('ol', {'class':'search-result-wrapper'})
		urls_to_scrape.append(total_url)
	urls_to_scrape.pop(len(urls_to_scrape)-1)
	#print(urls_to_scrape)
	url_generator_stop_status_key = "URLs have been obtained"
	return urls_to_scrape

def abstract_id_database_writer(abstract_id_log_name, abstract_input_tag_id, site_url_index):
	'''This function writes the abtract ids to a .txt file for easy access and documentation.'''
	abstract_id_log = open((abstract_id_log_name+str(site_url_index+1)+'.txt'), 'a')
	abstract_id_log.write(abstract_input_tag_id)
	abstract_id_log.write('\n')
	abstract_id_log.close()

def abstract_database_writer(abstract_page_url, title, author, abstract, abstracts_log_name):
	'''This function makes text files'''
	abstract_database_writer_start_status_key = "Writing"+" "+title+" "+"by"+" "+author+" "+"to disc"
	status_logger(status_logger_name, abstract_database_writer_start_status_key)
	abstracts_log = open(abstracts_log_name+'.txt', 'a')
	abstracts_log.write("Title:"+" "+title)
	abstracts_log.write('\n')
	abstracts_log.write("Author:"+" "+author)
	abstracts_log.write('\n')
	abstracts_log.write("URL:"+" "+abstract_page_url)
	abstracts_log.write('\n')
	abstracts_log.write("Abstract:"+" "+abstract)
	abstracts_log.write('\n'+'\n')
	abstracts_log.close()
	abstract_database_writer_stop_status_key = "Written"+" "+title+" "+"to disc"
	status_logger(status_logger_name, abstract_database_writer_stop_status_key)

def abstract_id_database_reader(abstract_id_log_name, site_url_index):
	'''This function has been explicitly written to access
	the abstracts database that the given prgram generates.'''
	abstract_id_database_reader_start_status_key = "Extracting Abstract IDs from disc"
	status_logger(status_logger_name, abstract_id_database_reader_start_status_key)

	lines_in_abstract_id_database=[line.rstrip('\n') for line in open(abstract_id_log_name+str(site_url_index+1)+'.txt')]

	abstract_id_database_reader_stop_status_key = "Extracted Abstract IDs from disc"
	status_logger(status_logger_name,abstract_id_database_reader_stop_status_key)

	return lines_in_abstract_id_database

def page_status(page):
	'''Prints the page status. Will be used whenever a new webpage is picked for scraping.'''
	page_status_key = "Page status:"+" "+str(page.status)
	status_logger(status_logger_name, page_status_key)

def page_souper(page):
	'''Function soups the webpage elements and provided the tags for search.
	Note: Appropriate encoding has to be picked up before souping'''
	page_souper_start_status_key = "Souping page"
	status_logger(status_logger_name, page_souper_start_status_key)
	page_soup = BeautifulSoup(page, 'html.parser')
	page_souper_stop_status_key = "Souped page"
	status_logger(status_logger_name, page_souper_stop_status_key)
	return page_soup

def abstract_page_scraper(abstract_url, abstract_input_tag_id, abstracts_log_name):
	'''This function is written to scrape the actual abstract of the specific paper,
	 that is being referenced within the list of abstracts'''
	abstract_page_scraper_status_key="Abstract ID:"+" "+abstract_input_tag_id
	status_logger(status_logger_name, abstract_page_scraper_status_key)
	abstract_page_url = abstract_url+abstract_input_tag_id
	abstract_page = url_reader(abstract_page_url)
	abstract_soup = page_souper(abstract_page)
	title = title_scraper(abstract_soup)
	
	'''Due to repeated attribute errors, these failsafes had to be put in place'''
	try:
		author = author_scraper(abstract_soup)
	except AttributeError:
		author = "Author not available"
	try:
		abstract = abstract_scraper(abstract_soup)
	except AttributeError:
		abstract = "Abstract not available"
	
	abstract_database_writer(abstract_page_url, title, author, abstract, abstracts_log_name)
	#print(abstract_soup_text)

def abstract_crawler(abstract_url, abstract_id_log_name, abstracts_log_name, site_url_index):
	'''This function crawls the page and access each and every abstract'''
	abstract_input_tag_ids = abstract_id_database_reader(abstract_id_log_name, site_url_index)
	for abstract_input_tag_id in abstract_input_tag_ids:
		try:
			abstract_crawler_accept_status_key="Abstract Number:"+" "+str((abstract_input_tag_ids.index(abstract_input_tag_id)+1)+site_url_index*100)
			status_logger(status_logger_name, abstract_crawler_accept_status_key)
			abstract_page_scraper(abstract_url, abstract_input_tag_id, abstracts_log_name)
		except TypeError:
			abstract_crawler_reject_status_key="Abstract Number:"+" "+str(abstract_input_tag_ids.index(abstract_input_tag_id)+1)+" "+"could not be processed"
			status_logger(status_logger_name, abstract_crawler_reject_status_key)
			pass

def abstract_scraper(abstract_soup):
	'''This function scrapes the abstract from the soup and returns to the page scraper'''
	abstract = str(abstract_soup.find('div', {'class':'Abstracts'}).text.encode('utf-8'))[1:]
	return abstract

def author_scraper(abstract_soup):
	'''This function scrapes the author of the text, for easy navigation and search'''
	author = str(abstract_soup.find('span', {'class':'text given-name'}).text.encode('utf-8'))[1:]
	return author

def title_scraper(abstract_soup):
	'''This function scrapes the title of the text'''
	title = str(abstract_soup.find('h1',{'class':'Head'}).text.encode('utf-8'))[1:]
	return title

def abstract_id_scraper(abstract_id_log_name, page_soup, site_url_index):
	'''This function helps in obtaining the PII number of the abstract.
	This number is then coupled with the dynamic url and provides'''

	abstract_id_scraper_start_status_key="Scraping IDs"
	status_logger(status_logger_name, abstract_id_scraper_start_status_key)
	''''This statement collects all the input tags that have the abstract ids in them'''
	abstract_input_tags = page_soup.findAll('a', {'class':'download-link'})
	for abstract_input_tag in abstract_input_tags:
		abstract_input_tag_id=abstract_input_tag.get('aria-describedby')
		abstract_id_database_writer(abstract_id_log_name, abstract_input_tag_id, site_url_index)

	abstract_id_scraper_stop_status_key="Scraped IDs"
	status_logger(status_logger_name, abstract_id_scraper_stop_status_key)

def end_process(status_logger_name):
	end_process_status_key="Process has successfully ended"
	status_logger(end_process_status_key, status_logger_name)

def processor(abstract_url, urls_to_scrape, abstract_id_log_name, abstracts_log_name, status_logger_name, keywords_to_search):
	for site_url_index in range(0, len(urls_to_scrape)):
		'''Collects the web-page from the url for souping'''
		page_to_soup = url_reader(urls_to_scrape[site_url_index])
		'''Souping the page for collection of data and tags'''
		page_soup = page_souper(page_to_soup)
		'''Scrapping the page to extract all the abstract IDs'''
		abstract_id_scraper(abstract_id_log_name, page_soup, site_url_index)
		'''Actually obtaining the abstracts after combining ID with the abstract_url'''
		abstract_crawler(abstract_url, abstract_id_log_name, abstracts_log_name, site_url_index)

'''This function collects keywords'''
keywords_to_search = arguments_parser()
'''Keyword is passed on to pre_processing() declares the url of the site and the abstract collection url'''
abstract_url, urls_to_scrape, abstract_id_log_name, abstracts_log_name, status_logger_name = pre_processing(keywords_to_search)
'''Calling the processor() function here'''
processor(abstract_url, urls_to_scrape, abstract_id_log_name, abstracts_log_name, status_logger_name, keywords_to_search)
'''End process function'''
end_process(status_logger_name)