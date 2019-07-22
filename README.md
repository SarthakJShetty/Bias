# Analyzing biases in academic publications

:warning: <strong>Code is buggy</strong> :warning:

## 1.0 Introduction:
*This branch is contains code specifically for our "Threats to Themes" project. Here is the main [repository](https://github.com/SarthakJShetty/Bias).*

- A significant proportion of publications pertaining to the Western Ghats in the <em>pre-independence era</em> of India was motivated by economic benefits of the region.

- For example, a quick search on scientific repositories reveals that most of the scientific publications related to this geographic area are related to the Nilgiri hills, <strong>primarily due to the economic incentives of growing tea in the region.</strong>

- This project is a collaboration with <a title="Vijay" href="https://evolecol.weebly.com/" target="_blank">Vijay Ramesh</a> & <a title="Anand" href="https://www.earth.columbia.edu/articles/view/58#Osuri" target="_blank">Anand MO</a> from the <a title="E3B" href="http://e3b.columbia.edu/" target="_blank">Department of Ecology, Evolution & Environmental Biology</a>, <a href="https://www.columbia.edu/" title="Columbia University" target="_blank">Columbia University</a>.

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
<img src="assets/BiasFlow.png" alt="Bias Pipeline">
<i>Diagramatic representation of pipeline for collecting papers and generating visualizations.</i>

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

- This command will scrape the abstracts from <a title="Springer" href="https://link.springer.com/" target="_blank">Springer</a> that are related to "Western Ghats", and calculate the frequency with which the term "Conservation" appears in their abstract.

## 6.0 Results:

Currently, the <a title="LOGS" href="https://github.com/SarthakJShetty/Bias/blob/master/LOGS/" target="_blank">results</a> from the various biodiversity runs are stored as tarballs, in the <a title="LOGS" href="https://github.com/SarthakJShetty/Bias/blob/master/LOGS/" target="_blank">LOGS</a>  folder, primarily to save space.

To view the logs, topic-modelling results & trends chart from the tarballs, run the following commands:

		tar zxvf <log_folder_to_be_unarchived>.tar.gz

**Example:**

To view the logs & results generated from the run on <a title="east Melanesian Islands" target="_blank" href="https://github.com/SarthakJShetty/Bias/blob/master/LOGS/LOG_2019-04-24_19_35_East_Melanesian_Islands.tar.gz">"East Melanesian Islands"</a>:

		tar zxvf LOG_2019-04-24_19_35_East_Melanesian_Islands.tar.gz

### 6.1 Topic Modelling Results:

The ```NLP_Engine.py``` module creates topic modelling charts such as the one shown below.

<img src='https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/Topic_Modelling_Results.jpg' alt='Topic Modelling Chart'>

<i>Distribution of topics discussed in publications about <a title = 'Eastern Himalayas  tarball' href =" https://github.com/SarthakJShetty/Bias/blob/master/LOGS/LOG_2019-02-27_15_23_Eastern_Himalayas.tar.gz" target="_blank">Eastern Himalayas</a>.</i>

- Circles indicate topics generated from the ```.txt``` file supplied to the ```NLP_Engine.py```, as part of the ```Bias``` pipeline.
- Each topic is made of a number of top keywords that are seen on the right, with an adjustable relevancy metric on top.
- More details regarding the visualizations and the udnerlying mechanics can be checked out [here](https://nlp.stanford.edu/events/illvi2014/papers/sievert-illvi2014.pdf).

### 6.2 Trends Result:

<img src = "https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/Trends_Chart.png" alt = 'Trends Chart for Eastern '>

- Here, abstracts pertaining to [Eastern Himalayas](https://github.com/SarthakJShetty/Bias/blob/master/LOGS/LOG_2019-02-27_15_23_Eastern_Himalayas.tar.gz) were scrapped and temporally trend of occurance for "Conservation" was checked.
- The frequency is presented alongisde the bubble for each year on the chart.
- Still working on the presentability. [This](https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/XKCD_Rendering.png) is an alternative that we're personally excited about.

**Note:**

- This repository is still under active development. The <a title="README" href="https://github.com/SarthakJShetty/Bias">README.md</a> is yet to be updated in detail.

- A detailed weekly (almost) build-log can be found <a href="https://github.com/SarthakJShetty/Bias/blob/master/build-log.md" title="build-log" target="_blank">here</a>.