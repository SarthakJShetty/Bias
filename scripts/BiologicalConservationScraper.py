from selenium import webdriver
from bs4 import BeautifulSoup as bs
import numpy as np
import time

science_direct_url = 'https://sciencedirect.com'
abstract_url = 'https://www.sciencedirect.com/search/advanced?pub=Biological%20Conservation&cid=271811&articleTypes=REV%2CFLA%2CABS&show=100&offset='

def selenium_driver(url):
	browser = webdriver.Chrome()
	browser.get(url)
	html_code = browser.page_source
	
	return html_code

def souper(html_code):
	soup = bs(html_code, 'html.parser')
	
	return soup

def pages_to_scrape_number(url):
	html_code = selenium_driver(url)
	soup = souper(html_code)
	
	return int(((soup.find('ol', {'class':'Pagination hor-separated-list'}).text).split(' ')[3])[:2])

def url_generator(abstract_url, number_of_pages):
	urls_to_scrape = []
	for number in range(0, number_of_pages):
		if(number == 0):
			temp_url = abstract_url + str(number)
		else:
			temp_url = abstract_url + str(number) + '00'
		urls_to_scrape.append(temp_url)
	
	return urls_to_scrape

def abstract_link_appender(pre_abstract_links, science_direct_url):
	abstract_links = []
	for pre_abstract_link in pre_abstract_links:
		abstract_links.append(science_direct_url+pre_abstract_link)
	
	return abstract_links

def abstract_link_scraper(url):
	pre_abstract_links = []
	html_code = selenium_driver(url)
	soup = souper(html_code)
	
	abstracts_result_set = soup.findAll('a', {'class':'result-list-title-link u-font-serif text-s'})
	for abstract_result_set in abstracts_result_set:
		pre_abstract_links.append(abstract_result_set.get('href'))
	abstract_links = abstract_link_appender(pre_abstract_links, science_direct_url)

	return abstract_links

def abstract_writer(abstract):
	abstract_write = open('BiologicalConservation.txt', 'a')
	abstract_write.write(abstract)
	abstract_write.write('\n')
	abstract_write.close()

def delay_ping():
	delay_value = np.random.randint(0, 20)
	print('Delaying by: '+str(delay_value)+'\n')
	time.sleep(delay_value)

number_of_pages = pages_to_scrape_number(abstract_url)
print('Number of pages to scrape: '+str(number_of_pages))
urls_to_scrape = url_generator(abstract_url, number_of_pages)

for page_url in urls_to_scrape:
	print('URL: '+page_url+'\n')
	abstract_links = abstract_link_scraper(page_url)
	delay_ping()
	for abstract_link in abstract_links:
		print('Abstract Link:  '+abstract_link+'\n')
		abstract_html_code = selenium_driver(abstract_link)
		abstract_soup = souper(abstract_html_code)
		abstract = abstract_soup.find('div', {'id':'as0005'}).text
		abstract_writer(abstract)
		print(abstract+'\n')
		delay_ping()