'''This is the one of the last bits of journal scrapers that we have written for this project. Here, we scrape papers from 
Environmenatal Conservation, a journal maintained by The Cambridge Press. Most of the scrapping principles across the journals are same, bar a few
features.

You can check out the broader Bias project here: https;//GitHub.com/SarthakJShetty/Bias

-Sarthak
(16/06/2019)'''

'''Importing selenium here to trigger the Chrome isntance from where the HTML is collected for scrapping'''
from selenium import webdriver, common
'''Making code readable using BeautifulSoup'''
from bs4 import BeautifulSoup as bs
'''To generate random integers for the delay function, numpy is used'''
import numpy as np
'''Sleep code, to delay pings'''
import time

'''URL to which abstract href tags are appended to'''
science_direct_url = 'https://cambridge.org'
'''Abstracts are collected from iteration of this URL'''
start_url = 'https://www.cambridge.org/core/journals/environmental-conservation/listing?pageNum=1&searchWithinIds=A218EAF4E0E042B46D28788C80419CA8'
'''The number of the current page being scrapped will be appended to this URL'''
abstract_url = 'https://www.cambridge.org/core/journals/environmental-conservation/listing?pageNum='

def selenium_driver(url):
	'''Creating Chrome instances from where the HTMl is scrapped from'''
	browser = webdriver.Chrome()
	browser.set_page_load_timeout(60)
	browser.get(url)
	html_code = browser.page_source
	
	return html_code, browser

def souper(html_code):
	'''Soupifying code, making it pretty and parsing it to be scrapped'''
	soup = bs(html_code, 'html.parser')
	
	return soup

def pages_to_scrape_number(url):
	'''Collecting the number of pages containing abstract links to be scrapped'''
	html_code, browser = selenium_driver(url)
	soup = souper(html_code)

	'''Returning the integer value of the number of pages to the main function pipeline'''
	return int(soup.find('p', {'class':'paragraph_05 margin-bottom-small'}).text.split(' ')[3])

def url_generator(abstract_url, number_of_pages):
	'''Generating URLs by appending a counter term to the ScienceDirect URL mentioned earlier'''
	urls_to_scrape = []
	for number in range(1, number_of_pages):
		if(number == 0):
			'''In order to avoid looking at ugly 000 at the end of the first URL'''
			temp_url = abstract_url + str(number)
		else:
			temp_url = abstract_url + str(number) + '&searchWithinIds=A218EAF4E0E042B46D28788C80419CA8'
		urls_to_scrape.append(temp_url)
	
	return urls_to_scrape

def abstract_link_appender(pre_abstract_links, science_direct_url):
	'''href tags do not contain the https://sciencedirect.com/ part. This function generate legit links by appending the href to the base URL'''
	abstract_links = []
	for pre_abstract_link in pre_abstract_links:
		abstract_links.append(science_direct_url+pre_abstract_link)
	
	return abstract_links

def abstract_link_scraper(url):
	'''Scrapping the URL of the abstract page from the results obtained'''
	pre_abstract_links = []
	html_code, browser = selenium_driver(url)
	soup = souper(html_code)
	
	abstracts_result_set = soup.findAll('a',{'class':'part-link'})
	for abstract_result_set in abstracts_result_set:
		pre_abstract_links.append(abstract_result_set.get('href'))
	abstract_links = abstract_link_appender(pre_abstract_links, science_direct_url)

	return abstract_links

def abstract_writer(abstract_text):
	'''Simple writer to hold the data in, before maybe feeding it into the topic modelling code'''
	abstract_write = open('EnvironmentalConservation.txt', 'a')
	abstract_write.write(abstract_text)
	abstract_write.write('\n')
	abstract_write.close()

def delay_ping():
	'''Delaying function, that delays the code randomly between 0 and 20 seconds after each page and each abstract'''
	delay_value = np.random.randint(0, 20)
	print('Delaying by: '+str(delay_value)+'\n')
	time.sleep(delay_value)

def page_refresher(browser):
	'''This function refreshes the webpage rendered by selenium, in case Chrome is unreachable'''
	browser.refresh()

'''Collecting the number of pages from the bottom of the results page'''
number_of_pages = pages_to_scrape_number(start_url)
print('Number of pages to scrape: '+str(number_of_pages))

'''Generating URLs from where the abstracts are to be scrapped'''
urls_to_scrape = url_generator(abstract_url, number_of_pages)

for page_url in urls_to_scrape:
	print('URL: '+page_url+'\n')
	html_code, browser = selenium_driver(page_url)
	abstract_soup = souper(html_code)
	abstracts = abstract_soup.findAll('div', {'class':'abstract'})
	for abstract in abstracts:
		abstract_text = abstract.text
		abstract_writer(abstract_text)
	browser.close()
	delay_ping()