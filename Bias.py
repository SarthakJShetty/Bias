'''Hello!
We have decided to fragment the entire code, and run it off of one common script.
In the future, the Analyzer.py and the Visualizer.py scripts will be called here as well.

Check out the build-log.md for a detailed changes implemented.
Check out the README.md for more details about the project.

Sarthak J. Shetty
12/09/2018'''

'''Imports scraper_main() from Scraper.py'''
from Scraper import scraper_main
'''Imports some of the functions required by different scripts here.'''
from pre_processing_functions import pre_processing, arguments_parser

'''Keywords from the user are extracted here'''
keywords_to_search=arguments_parser()
'''Runs the scraper here to scrape the details from the scientific repository'''
scraper_main(keywords_to_search)