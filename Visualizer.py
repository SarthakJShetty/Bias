'''Hello! This code code is part of the Bias project, where we are trying to prove the existence
of certain biases in academic publications.
We will be displaying the results from the NLP_Engine.py code here, using primarily using pyLDAvis library.

Check out the repository build-log.md for a more detailed report of the code working.
Check out the repository README.md for a high-level overview of the project and the objective.

Sarthak J. Shetty
24/11/2018'''
from common_functions import status_logger
'''import matplotlib as plt'''
import matplotlib.pyplot as plt
'''Library necessary to develop the html visualizations'''
import pyLDAvis

def visualizer_generator(lda_model, corpus, id2word, logs_folder_name, status_logger_name):
	'''This code generates the .html file with generates the visualization of the data prepared.'''
	visualizer_generator_start_status_key = "Preparing the topic modeling visualization"
	status_logger(status_logger_name, visualizer_generator_start_status_key)

	textual_data_visualization = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
	pyLDAvis.save_html(textual_data_visualization, logs_folder_name+"/"+"Data_Visualization_Topic_Modelling.html")

	visualizer_generator_end_status_key = "Prepared the topic modeling visualization"+" "+logs_folder_name+"/"+"Data_Visualization_Topic_Modelling.html"
	status_logger(status_logger_name, visualizer_generator_end_status_key)		

def trends_histogram(abstract_word_dictionary, starting_year, ending_year, trend_keywords, logs_folder_name, status_logger_name):
	'''This function is responsible for generating the histograms to visualizations the trends in research topics.'''
	trends_histogram_start_status_key = "Generating the trends histogram"
	status_logger(status_logger_name, trends_histogram_start_status_key)

	'''What's happening here?
	a) trends function receives the dictionary prepared by the Scraper code.
	b) Information is organized in a conventional key and value form; key=year, value=frequency.
	c) We extract the key from the dictionary and generate a new list comprising of the years in which the trend keywords occurs.
	d) We calculate the max and min years in this new list and convert them to int and extract the complete set of years that lie between these extremes.
	e) We cycle through the keys in the dictionary and extract frequency of occurrence for each year in the list of years.
	f) If the term does not appear in that year, then it's assigned zero (that's how dictionaries work).
	g) The two lists (list of years and list of frequencies) are submitted to the plot function for plotting.'''

	'''This list will hold the abstract years which contain occurrences of the word that we are investigating'''
	list_of_years=[]
	for element in abstract_word_dictionary:
		list_of_years.append(element)
	list_of_years_to_be_plotted = [year for year in range(int(starting_year), int(ending_year)+1)]
	'''Here we generate the corresponding frequencies'''
	frequencies_to_be_plotted = [int(abstract_word_dictionary[str(year)]) for year in range(int(starting_year), int(ending_year)+1)]
	'''Here, we will generate a list of frequencies to be plotted along the Y axis, using the Y ticks function'''
	y_ticks_frequency = []
	'''Extracting the largest frequency value in the list to generate the Y ticks list'''
	max_frequency_value = max(frequencies_to_be_plotted)
	for frequency_element in range(0, max_frequency_value+1):
		y_ticks_frequency.append(frequency_element)

	'''Varying the size of the figure to accommodate the entire trends graph generated'''
	plt.figure(figsize=[15,10])
	'''Plotting the years along the X axis and the frequency along the Y axis'''
	plt.plot(list_of_years_to_be_plotted, frequencies_to_be_plotted)
	'''Plotting the frequencies again to make the frequency pivots visible'''
	plt.plot(list_of_years_to_be_plotted, frequencies_to_be_plotted, 'ro')
	'''Here, we are labeling each of the frequencies plotted to ensure better readability, instead of second-guessing Y axis values'''
	for element in range(0, len(list_of_years_to_be_plotted)):
		'''Avoiding the unnecessary clutter in the visualization by removing text boxes for frequency=0'''
		if(frequencies_to_be_plotted[element]!=0):
			plt.text(list_of_years_to_be_plotted[element], frequencies_to_be_plotted[element], "Frequency: "+str(frequencies_to_be_plotted[element]), bbox=dict(facecolor='orange', alpha=0.3), horizontalalignment='right', verticalalignment='top',size=8)

	'''Adds a label to the element being represented across the Y-axis (frequency of occurrence)'''
	plt.ylabel("Frequency of occurrence:"+" "+trend_keywords[0])
	'''Adds a label to the element being represented across the X-axis (years)'''
	plt.xlabel("Year of occurrence:"+" "+trend_keywords[0])
	'''Adds an overall title to the trends chart'''
	plt.title("Trends Chart:"+" "+trend_keywords[0])
	'''xticks() ensures that each and every year is plotted along the x axis and changing the rotation to ensure better readability'''
	plt.xticks(list_of_years_to_be_plotted, rotation=45)
	'''yticks() ensures that each and every frequency is plotted to ensure better readability in the resulting figure'''
	plt.yticks(y_ticks_frequency)
	'''Saves the graph generated to the disc for further analysis'''
	plt.savefig(logs_folder_name+"/"+"Data_Visualization_Trends_Graph"+"_"+trend_keywords[0]+".png")

	trends_histogram_end_status_key = "Generated the trends graph"+" "+logs_folder_name+"/"+"Data_Visualization_Trends_Graph"+"_"+trend_keywords[0]+".png"
	status_logger(status_logger_name, trends_histogram_end_status_key)

def visualizer_main(lda_model, corpus, id2word, logs_folder_name, status_logger_name):
	visualizer_main_start_status_key = "Entering the visualizer_main() code"
	status_logger(status_logger_name, visualizer_main_start_status_key)

	'''This the main visualizer code. Reorging this portion of the code to ensure modularity later on as well.'''
	visualizer_generator(lda_model, corpus, id2word, logs_folder_name, status_logger_name)

	visualizer_main_end_status_key = "Exiting the visualizer_main() code"
	status_logger(status_logger_name, visualizer_main_end_status_key)