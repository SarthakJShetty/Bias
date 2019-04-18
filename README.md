# Analyzing Trends in Research Topics/Areas Across Biodiversity Hotspots

:warning: <strong>Code is buggy</strong> :warning:

## 1.0 Introduction:

In recent years, threats to biodiversity have increased as a function of changes in global climate and anthropogenic transformation of land (Cardinale et al., 2012).The tropics in particular are undergoing massive conversion of suitable habitat into agricultural land, forest plantations and industrial zones (Newbold et al., 2015). While habitat loss and climate change are ongoing and pervasive drivers of biodiversity loss, other threats (as defined under the Millenium Ecosystem Assessment Goals) include the spread of invasive species, overexploitation of natural resources and pollution (Insert MEA Citation). To prevent further loss of biodiversity, we need timely and targeted research that addresses ongoing threats in different geographic regions (Fisher et al., ?).  

More info. to follow.

A significant proportion of publications pertaining to the Western Ghats in the <em>pre-independence era</em> of India was motivated by economic benefits of the region.

- For example, a quick search on scientific repositories reveals that most of the scientific publications related to this geographic area are related to the Nilgiri hills, <strong>primarily due to the economic incentives of growing tea in the region.</strong>

- This project is a collaboration with <a title="Vijay" href="https://evolecol.weebly.com/" target="_blank">Vijay Ramesh</a>, <a title="E3B" href="http://e3b.columbia.edu/" target="_blank">Department of Ecology, Evolution & Environmental Biology</a>, <a href="https://www.columbia.edu/" title="Columbia University" target="_blank">Columbia University</a>.

- This tool is being developed to prove (quantitatively) the existence of these biases.

<strong>Note:</strong> This <a title="Latest run" href="https://github.com/SarthakJShetty/Bias/tree/master/LOGS/LOG_2019-02-14_11_13_Western_Ghats_Conservation">log</a> contains the most recent run of the program.

## 2.0 Model Overview:
- The model is made up of three parts:

	1. <strong><a title="Scraper" href="https://github.com/SarthakJShetty/Bias/tree/master/Scraper.py/">Scraper</a>:</strong> This component scrapes scientific repository for publications containing the specific combination of keywords.
	2. <strong><a title="Analyzer" href="https://github.com/SarthakJShetty/Bias/tree/master/Analyzer.py/">Analyzer</a>:</strong> This component collects and measures the frequency of select keywords in the abstracts database.
	3. <strong><a title="NLP Engine" href="https://github.com/SarthakJShetty/Bias/tree/master/NLP_Engine.py/">NLP Engine</a>:</strong> This component extracts insights from the abstracts collected by presenting topic modelling.
	4. <strong><a title="Visualizer" href="https://github.com/SarthakJShetty/Bias/tree/master/Visualizer.py/">Visualizer</a>:</strong> This component presents the results and data from the Analyzer to the end user.
		
- Check out the <a title="LOGS" href="https://github.com/SarthakJShetty/Bias/tree/master/LOGS">LOGS</a> for the results of ```Scraper.py``` and ```Analyzer.py```.

## 3.0 Installation Instructions:

### 3.1 Common instructions:

<strong>Note:</strong> These instructions are common to both Ubuntu and Windows systems. 

1.  Clone this repository:

		E:\>git clone https://github.com/SarthakJShetty/Bias.git

2. Change directory to the 'Bias' directory:

		E:\>cd Bias		

### 3.2 Virtualenv instructions:		

1. Install ```virtualenv``` using ```pip```:

		user@Ubuntu: pip install virtualenv

2. Create a ```virtualenv``` environment called "Bias" in the directory of your project:

		user@Ubuntu: virtualenv --no-site-packages Bias
	
	<strong>Note:</strong> This step usually takes about 30 seconds to a minute.

3. Activate the virtualenv enviroment:

		user@Ubuntu: ~/Bias$ source Bias/bin/activate

	You are now inside the ```Bias``` environment.

4. Install the requirements from 	<a title="Ubuntu Requirements" href="https://github.com/SarthakJShetty/Bias/blob/master/ubuntu_requirements.txt">```ubuntu_requirements.txt```</a>:
	
		(Bias) user@Ubuntu: pip3 install -r ubuntu_requirements.txt
		
	<strong>Note:</strong> This step usually takes a few minutes, depending on your network speed.

### 3.3 Conda instructions:

1. Create a new ```conda``` environment:
	
		E:\Bias conda create --name Bias python=3.5	

2. Enter the new ```Bias``` environment created:
	
		E:\Bias activate Bias

3. Install the required packages from <a href="https://github.com/SarthakJShetty/Bias/blob/master/conda_requirements.txt">```conda_requirements.txt```</a>:
		
		(Bias) E:\Bias conda install --yes --file conda_requirements.txt

	<strong>Note:</strong> This step usually takes a few minutes, depending on your network speed.

## 4.0 How it works:

### 4.1 Scraper:
- The <a title="Scraper" href="https://github.com/SarthakJShetty/Bias/blob/master/Scraper.py">```Scraper.py```</a> currently scrapes only the abstracts from <a title="Springer" href="https://www.link.Springer.com">Springer</a>.

- A default URL is provided in the code. Once the keywords are provided, the URLs are queried and the resultant webpage is souped and ```abstract_id``` is scraped.

- A new <a title="Abstract ID" target="_blank" href="https://github.com/SarthakJShetty/Bias/blob/master/LOGS/LOG_2018-08-29_15_4_Western_Ghats/Abstract_ID_Database_2018-08-29_15_4_1.txt">```abstract_id_database```</a> is prepared for each result page, and is referenced when a new paper is scraped.

- The <a title="Abstract Database" target="_blank" href="https://github.com/SarthakJShetty/Bias/blob/master/LOGS/LOG_2018-08-29_15_4_Western_Ghats/Abstract_Database_2018-08-29_15_4.txt">```abstract_database```</a> contains the abstract along with the title, author and a complete URL from where the full text can be downloaded. They are saved in a ```.txt``` file

- A <a title="Status Logger" href="https://github.com/SarthakJShetty/Bias/blob/master/LOGS/LOG_2018-08-29_15_4_Western_Ghats/Status_Logger_2018-08-29_15_4.txt" target="_blank">```status_logger```</a> is used to log the sequence of commands in the program.

### 4.2 Analyzer:
- The <a title="Analyzer" href="https://github.com/SarthakJShetty/Bias/tree/master/Analyzer.py/">```Analyzer.py```</a> analyzes the frequency of different words used in the abstract.

- It serves as an intermediary between the Scraper and the Visualizer, preparing the scraped data into a neat ```.csv``` <a title="Analyzer CSV file" href="https://github.com/SarthakJShetty/Bias/blob/master/LOGS/LOG_2019-02-14_11_13_Western_Ghats_Conservation/Abstract_Database_2019-02-14_11_13_FREQUENCY_CSV_DATA.csv">file</a>.

- This ```.csv``` file is then passed on to the Visualizer.

### 4.3 NLP Engine:

- The NLP Engine is used to generate the topic modelling charts for the [Visualizer.py](https://github.com/SarthakJShetty/Bias/tree/master/Visualizer.py) script. It generates the corpus and language model for analysis and use with other scripts.

- The corpus and model generated are then passed to the [Visualizer.py](https://github.com/SarthakJShetty/Bias/tree/master/Visualizer.py) script.

- The top modelling chart can be checked out [here](https://github.com/SarthakJShetty/Bias/blob/master/LOGS/LOG_2019-02-27_15_23_Eastern_Himalayas/Data_Visualization_Topic_Modelling.html). It is interactive and a detailed guide explaining its parts will be uploaded soon.

	**Note:** The ```.html``` file linked above has to be downloaded and opened in a JavaScript enabled browser to be viewed.

### 4.4 Visualizer:

- The <a title="Visualizer" href="https://github.com/SarthakJShetty/Bias/blob/master/Visualizer.py">```Visualizer.py```</a> code is responsible for generating the visualization associated with a specific search.

- Currently, the research theme visualization is functional. The trends histogram will soon be added.

- The research themes data visualization is stored as a <a title="Data Visualization" href="https://github.com/SarthakJShetty/Bias/blob/master/LOGS/LOG_2018-12-31_17_11_Western_Ghats_Ecology_Conservation_Policy/Data_Visualization.html">.html file</a> in the LOGS directory and can be viewed in the browser.

## 5.0 Usage:
To run the code and generate the topic distribution and trend of research graphs:
		
		(Bias) E:\Bias python Bias.py --keywords="Western Ghats" --trends="Conservation"

- This command will scrape the abstracts from Springer that are related to "Western Ghats", and calculate the frequency with which the term "Conservation" appears in their abstract.

## 6.0 Known Issues:

- The Scraper can only scrape abstracts from Springer at the moment

- Due to lack of storage, we are yet to integrate the portion of the code that scrapes information from papers.

#### Note:

- This repository is still under active development. The <a title="README" href="https://github.com/SarthakJShetty/Bias">README.md</a> is yet to be updated in detail.

- A detailed weekly build-log can be found <a href="https://github.com/SarthakJShetty/Bias/blob/master/build-log.md" title="README" target="_blank">here</a>.