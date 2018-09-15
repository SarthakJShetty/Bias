
# Analyzing biases in academic publications

:warning: <strong>Code is buggy</strong>:warning:

## Introduction:

- A significant proportion of publications pertaining to the Western Ghats in the <em>pre-independence era</em> of India was motivated by economic benefits of the region.

- For example, a quick search on scientific repositories reveals that most of the scientific publications related to this geographic area are related to the Nilgiri hills, <strong>primarily due to the economic incentives of growing tea in the region.</strong>

- This project is a collaboration with <a title="Vijay" href="https://evolecol.weebly.com/" target="_blank">Vijay Ramesh</a>, <a title="E3B" href="http://e3b.columbia.edu/" target="_blank">Department of Ecology, Evolution & Environmental Biology</a> (or E3B for short), <a href="https://www.columbia.edu/" title="Columbia University" target="_blank">Columbia University</a>.

- This tool is being developed to prove (quantitatively) the existence of these biases.

<strong>Note:</strong> This <a title="Latest run" href="https://github.com/SarthakJShetty/Bias/tree/master/LOGS/LOG_2018-08-29_15_4_Western_Ghats">log</a> contains the most recent run of the program.

## Model Overview:
- The model is made up of three parts:
	1. <strong><a title="Scraper.py" href="https://github.com/SarthakJShetty/Bias/tree/master/Scraper.py/">Scraper</a>:</strong> This component scrapes scientific repository for publications containing the specific combination of keywords.
	2. <strong>Analyzer:</strong> This component scrapes the ```.txt``` file containing the abstract (and eventually ```.pdf```) for specific keywords.
	3. <strong>Visualizer:</strong> This component presents the results and data from the Analyzer to the end user.
		
- Scraper is ready as of now (somewhat). The text-analyzer is still under development and work on the data-visualizer is yet to begin. Stay tuned for more developments.
- Check out the <a title="LOGS" href="https://github.com/SarthakJShetty/Bias/tree/master/LOGS">LOGS</a> for the results of ```Scraper.py```

## Virtual environment setup:
<strong>Note:</strong> These instructions are the same for Windows and Ubuntu users. However, while installing the packages, Ubuntu users have to use ```pip3``` instead of ```pip```, and ```python3``` instead of ```python```.

1.  Clone this repository:

		E:\>git clone https://github.com/SarthakJShetty/Bias.git

2. Change directory to the 'Bias' directory:

		E:\>cd Bias		
		
3. Install ```virtualenv``` using ```pip```:

		E:\Bias>pip install virtualenv

4. Create a ```virtualenv``` environment called "Bias" in the directory of your project:

		E:\Bias>virtualenv Bias
	
	<strong>Note:</strong> This step usually takes about 30 seconds to a minute.
	
5. Activate the "Bias" environment using ```virtualenv```:

		E:\Bias>.\Bias\Scripts\activate

	<strong>Note:</strong> If you are running this code on Ubuntu, the code will be as follows:

		user@Ubuntu: ~/Bias$ source Bias/bin/activate

	You are now inside the ```Bias``` environment.

## Instructions:
<strong>Note:</strong> These instructions are the same for Windows and Ubuntu users. However, while installing the packages, Ubuntu users have to use ```pip3``` instead of ```pip```, and ```python3``` instead of ```python```.

- Install the required packages using the <a title="Package Requirements" target="_blank" href="https://github.com/SarthakJShetty/Bias/blob/master/requirements.txt">```requirements.txt```</a> file available in the cloned repository.
		
		(Bias) E:\Bias>pip install -r requirements.txt

- Run the code from the repository directory:

		(Bias) E:\Bias>python Bias.py --keywords="Western Ghats"

- A LOG folder is created in the folder that contains the code. Within this folder, another directory, specific to the current run of the Scraper will be written, containing:
	- ```status_logger.txt``` file will be generated, which logs all the process executed by the Scraper.

	- ```Abstract_ID_Database.txt``` containing all the Abstract_IDs of the page being souped.

	- ```Abstract_Database.txt``` containing all the abstracts, relevant to the ```--keywords``` entered by the user.


### Scraper:
- The <a title="Scraper.py" href="https://github.com/SarthakJShetty/Bias/blob/master/Scraper.py">```Scraper.py```</a> currently scrapes only the abstracts from <a title="ScienceDirect" href="https://www.ScienceDirect.com">ScienceDirect</a>.

- A default URL is provided in the code. Once the keywords are provided, the URLs are queried and the resultant webpage is souped and ```abstract_id``` is scraped.

- A new <a title="Abstract ID" target="_blank" href="https://github.com/SarthakJShetty/Bias/blob/master/LOGS/LOG_2018-08-29_15_4_Western_Ghats/Abstract_ID_Database_2018-08-29_15_4_1.txt">```abstract_id_database```</a> is prepared for each result page, and is referenced when a new paper is scraped.

- The <a title="Abstract Database" target="_blank" href="https://github.com/SarthakJShetty/Bias/blob/master/LOGS/LOG_2018-08-29_15_4_Western_Ghats/Abstract_Database_2018-08-29_15_4.txt">```abstract_database```</a> contains the abstract along with the title, author and a complete URL from where the full text can be downloaded. They are saved in a ```.txt``` file

- A <a title="Status Logger" href="https://github.com/SarthakJShetty/Bias/blob/master/LOGS/LOG_2018-08-29_15_4_Western_Ghats/Status_Logger_2018-08-29_15_4.txt" target="_blank">```status_logger```</a> is used to log the sequence of commands in the program.

## Known Issues:
- The Scraper can only scrape abstracts from ScienceDirect at the moment, since ScienceDirect does not allow users to view publications in native ```.pdf``` format, but instead loads a ```.html``` document with the contents embedded in it.

#### Note:
- This repository is still under active development. The <a title="README" href="https://github.com/SarthakJShetty/Bias">README.md</a> is yet to be updated in detail.
- A detailed build-log can be found <a href="https://github.com/SarthakJShetty/Bias/blob/master/build-log.md" title="README" target="_blank">here</a>.