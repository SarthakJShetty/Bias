'''Hello! We have decided to fragment the entire code, and run it off of one common script.
In the future, the Analyzer.py and the Visualizer.py scripts will be called here as well.

Check out the build-log.md for a detailed changes implemented.
Check out the README.md for more details about the project.

Sarthak J. Shetty
12/09/2018'''

'''Imports scraper_main() from Scraper.py'''
from Scraper import scraper_main
'''Importing the analyzer code here as well'''
from Analyzer import analyzer_main
'''Importing the visualizer and gensim code here'''
from NLP_Engine import nlp_engine_main
'''Importing the code to visualize the data interpreted by the NLP_Engine'''
from Visualizer import visualizer_main
'''Imports some of the functions required by different scripts here.'''
from common_functions import pre_processing, arguments_parser, end_process
'''Keywords from the user are extracted here'''

keywords_to_search=arguments_parser()

'''Calling the pre_processing functions here so that data is available across the code.'''
abstract_id_log_name, abstracts_log_name, start_url, abstract_url, query_string, logs_folder_name, status_logger_name = pre_processing(keywords_to_search)

'''Runs the scraper here to scrape the details from the scientific repository'''
scraper_main(abstract_id_log_name, abstracts_log_name, start_url, abstract_url, query_string, status_logger_name, keywords_to_search)

'''Calling the Analyzer Function here'''
analyzer_main(abstracts_log_name, status_logger_name)

'''Calling the visualizer code below this portion'''
lda_model, corpus, id2word = nlp_engine_main(abstracts_log_name, status_logger_name)

'''Importing the visualizer_main function to view the LDA Model built by the NLP_engine_main() function'''
visualizer_main(lda_model, corpus, id2word, logs_folder_name, status_logger_name)

'''Declaring the end of a successful run of the code'''
end_process(status_logger_name)