from selenium import webdriver
from bs4 import BeautifulSoup as bs

wiley_url = 'https://onlinelibrary.wiley.com'
journal_url = 'https://onlinelibrary.wiley.com/loi/15231739'

def selenium_driver(url):
	browser = webdriver.Chrome()
	browser.get(url)
	page = browser.page_source
	return page

def url_appender(wiley_url, appendee):
	return wiley_url + appendee

def souper(page):
	soup = bs(page, 'html.parser')
	return soup

def journal_years_scraper(journal_url):
	journal_years = []
	page = selenium_driver(journal_url)
	soup = souper(page)

	a_tags = soup.findAll('a')
	for a_tag in a_tags:
		if '/year' in a_tag.get('href'):
			journal_years.append(url_appender(wiley_url, a_tag.get('href')))

	return journal_years

def journal_months_scraper(journal_year):
	journal_months = []
	page = selenium_driver(journal_year)
	soup = souper(page)

	temp_journal_months = soup.findAll('a', {'class':'visitable'})
	for temp_journal_month in temp_journal_months:
		journal_months.append(url_appender(wiley_url, temp_journal_month.get('href')))

	return journal_months

def abstract_url_scraper(journal_month):
	abstract_urls = []
	page = selenium_driver(journal_month)
	soup = souper(page)

	temp_abstract_urls = soup.findAll('a', {'title':'Abstract'})
	for temp_abstract_url in temp_abstract_urls:
		abstract_urls.append(url_appender(wiley_url, temp_abstract_url.get('href')))
	
	return abstract_urls


journal_years = journal_years_scraper(journal_url)
abstracts = []

'''Recursion is bae'''

for journal_year in journal_years:
	print('Year:' + journal_year)
	journal_months = journal_months_scraper(journal_year)
	for journal_month in journal_months:
		print('Month:' + journal_month)
		abstract_urls = abstract_url_scraper(journal_month)
		for abstract_url in abstract_urls:
			print('URL:' + abstract_url)
			abstract_page = selenium_driver(abstract_url)
			abstract_soup = souper(abstract_page)
			abstract = abstract_soup.find('div',{'class':'article-section__content en main'}).text 
			abstracts.append(abstract)
			print('Abstract:' + abstract)