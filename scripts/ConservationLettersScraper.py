'''This script is used to scrape the Conservation Letters Journals to generate the abstract corpus for the Threats to Themes project.
You can check out the broader Bias project here: https;//GitHub.com/SarthakJShetty/Bias

-Sarthak
(14/06/2019)'''

'''Selenium is a web toolkit for carrying out large scale automated tests. We use it here to bypass the JavaScript elements that are injected into the webpage.'''
from selenium import webdriver
'''Selenium prepares the HTML code, that is in turn passed onto BeautifulSoup to prettify it and make it searchable'''
from bs4 import BeautifulSoup as bs
'''From time library we are importing sleep to delay intermittent pings.'''
import time
'''To randomise the delay, introducing the numpy randint function here'''
import numpy as np

'''Wiley URL remains consistent throughout, for accessing the journal and the abstracts'''
wiley_url = 'https://onlinelibrary.wiley.com'
'''Specific journal URL from where the different issues are collected'''
journal_url = 'https://onlinelibrary.wiley.com/loi/1755263x'

def selenium_driver(url):
	'''This function triggers a Chrome testbet from where the HTML is collected, using Selenium'''
	browser = webdriver.Chrome()
	browser.get(url)
	'''Collecting the HTML of the triggered page'''
	page = browser.page_source
	return page

def delay_ping():
	'''This function delays the time between intermittent pings of the website, to elude serverside tracking scripts'''
	delay_time = np.random.randint(0, 20)
	time.sleep(delay_time)

def url_appender(wiley_url, appendee):
	'''This is a simple list appender which attaches the extracted href tags with the standard wiley_url declared above'''
	return wiley_url + appendee

def souper(page):
	'''Simple souper page that uses BeautifulSoup to soup the page to prettify it and make its tags searchable'''
	soup = bs(page, 'html.parser')
	return soup

def journal_years_scraper(journal_url):
	'''Scrapping years where the different volumes of the journal are held.'''
	journal_years = []
	page = selenium_driver(journal_url)
	soup = souper(page)

	'''Finding a tags and then collect the href parameters that contain /year in them'''
	a_tags = soup.findAll('a')
	for a_tag in a_tags:
		if '/year' in a_tag.get('href'):
			'''Appending the href to the wiley_url, handeled by the url_appender()'''
			journal_years.append(url_appender(wiley_url, a_tag.get('href')))

	return journal_years

def journal_months_scraper(journal_year):
	'''Given a specific year, retreive all the journals in that year, by the year'''
	journal_months = []
	page = selenium_driver(journal_year)
	soup = souper(page)

	temp_journal_months = soup.findAll('a', {'class':'visitable'})
	for temp_journal_month in temp_journal_months:
		'''Appending the incomplete href tags to the wiley_url'''
		journal_months.append(url_appender(wiley_url, temp_journal_month.get('href')))

	return journal_months

def abstract_url_scraper(journal_month):
	'''Given a specific journal, collect all the publication that are contained within'''
	abstract_urls = []
	page = selenium_driver(journal_month)
	soup = souper(page)

	'''Extracting the abstract link, not the text. That happens within the indented for loop'''
	temp_abstract_urls = soup.findAll('a', {'title':'Abstract'})
	for temp_abstract_url in temp_abstract_urls:
		abstract_urls.append(url_appender(wiley_url, temp_abstract_url.get('href')))
	
	return abstract_urls

def abstract_writer(abstract):
	'''Simple file writer. Creates an Abstracts.txt and appends the read abstract here'''
	abstract_log = open('ConservationLetters.txt', 'a')
	abstract_log.write(abstract)
	abstract_log.write('\n')
	abstract_log.close()

'''Collecting the journal years first, then the recursion starts below'''
journal_years = journal_years_scraper(journal_url)
'''Abstract will be appended to this list'''
abstracts = []

for journal_year in journal_years:
	'''Delaying the ping between successive year scrappings'''
	delay_ping()
	'''Collected the years here from the main journal page and looping through them now'''
	print('Year:' + journal_year)
	'''Collecting the months from each of the years here.'''
	journal_months = journal_months_scraper(journal_year)
	delay_ping()
	for journal_month in journal_months:
		'''Scrapping each of the abstracts in each of the month'''
		print('Month:' + journal_month)
		abstract_urls = abstract_url_scraper(journal_month)
		delay_ping()
		for abstract_url in abstract_urls:
			'''Collecting the abstract from the URL that was scrapped before'''
			print('URL:' + abstract_url)
			abstract_page = selenium_driver(abstract_url)
			abstract_soup = souper(abstract_page)
			try:
				'''Edge case has been coded here. If this one does not work, then goes to the except statement'''
				abstract = abstract_soup.find('div',{'class':'article-section__content en main'}).text
				abstract_writer(abstract)
			except AttributeError:
				try:
					abstract = abstract_soup.find('div',{'class':'article-section__content en short'}).text
					abstract_writer(abstract)
				except:
					abstract = 'Not available!'
			abstracts.append(abstract)
			print('Abstract:' + abstract)