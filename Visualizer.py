'''Hello! This code code is part of the Bias project, where we are trying to prove the existence
of certain biases in academic publications.
We will be displaying the results from the NLP_Engine.py code here, using primarily using pyLDAvis library.

Check out the repository build-log.md for a more detailed report of the code working.
Check out the repository README.md for a high-level overview of the project and the objective.

Sarthak J. Shetty
24/11/2018'''
from common_functions import status_logger
import pyLDAvis

def visualizer_main(lda_model, corpus, id2word, logs_folder_name, status_logger_name):
	'''This code generates the .html file with generates the visualization of the data prepared.'''
	visualizer_main_start_status_key = "Preparing the visualization"
	status_logger(status_logger_name, visualizer_main_start_status_key)
	textual_data_visualization = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
	pyLDAvis.save_html(textual_data_visualization, logs_folder_name+"/"+"Data_Visualization.html")
	visualizer_main_end_status_key = "Prepared the Visulizer"
	status_logger(status_logger_name, visualizer_main_end_status_key)