# Build-Log

<strong>Note:</strong> This build-log is updated chronologically, latest to old, top to bottom.

### Date: 17/04/2019
- Fixed the Journal title scrapping error. Server code crashed midway after 3700ish scrapes.
- ```tarballer()``` and ```rm_original_folder()``` function work well. Check out latest [LOGS](https://github.com/SarthakJShetty/Bias/tree/master/LOGS/LOG_2019-04-16_2_49_Atlantic_Forest_Conservation).
- Currently working on generating more datasets and figuring out topic-modelling representation of papers.

### Date: 16/04/2019
- Added a [system_functions.py](https://github.com/SarthakJShetty/Bias/blob/master/system_functions.py) script that contains a ```tarballer()``` and ```rm_original_folder()```.
- ```tarballer()``` packages the LOG file generated as a ```<file_name>.tar.gz```.
- ```rm_original_folder()``` deleted the LOG folder generated during run after tarballing.

### Date: 08/04/2019
- The code has been [broken up](https://github.com/SarthakJShetty/Bias/blob/master/scripts/) into smaller modules that can be run independent of each other.
- The modules run on Jupyter Notebooks for ease of use and improved readability.
- Currently looking at better visualization alternatives to existing charts.

### Date: 03/04/2019
- Splitting the main components of the code into smaller scripts. Scripts for the ```NLP_Engine.ipynb``` and ```Visualization.ipynb``` have been [uploaded](https://github.com/SarthakJShetty/Bias/blob/master/scripts/) as Jupyter Notebooks. Almost done with the ```Scraper.py``` code as well.
- Overhauled the representation of the research trends chart. The new version can be viewed [here](https://raw.githubusercontent.com/SarthakJShetty/Bias/master/LOGS/LOG_2019-02-27_15_23_Eastern_Himalayas/Data_Visualization_Trends_Graph_conservation.png). Ideas to improve readability are being tested as well.

### Date: 24/02/2019
- Improved the readability of the trends graph by incorporating the ```plt.text()``` function which enables labelling of each
nodal point in the graph. Results will be posted shortly.
- Also updated the <a title="Updated ubuntu requirements file" href="https://github.com/SarthakJShetty/Bias/blob/master/ubuntu_requirements.txt">ubuntu requirements</a>. Scraped a lot of unecessary requirements from the list.

### Date: 22/02/2019
- A delay function has been integrated into the scraping process, in order to bypass termination by the remote host.
- The <a title="Trends Graph" href="https://github.com/SarthakJShetty/Bias/blob/master/LOGS/LOG_2019-02-20_23_4_Western_Ghats_Biodiversity/Data_Visualization_Trends_Graph_biodiversity.png">trends graph</a> has been formatted to improve readability of the ticks across X and Y axes.

### Date: 14/02/2019
- <a title="Visualizer.py" href="https://github.com/SarthakJShetty/Bias/blob/master/Visualizer.py">```Visualizer.py```</a> code has been fixed to generate the trends visualization.
- The user provides a ```--trends``` which will be checked in the abstracts of the papers scraped as part of the broad theme provided under ```--keywords``` argument.
- The trends visualization is generated using ```matplotlib``` and is saved as a ```.png``` in the respective ```LOGS``` folder.

### Date: 06/02/2019
- ```Scraper.py``` code has been rehauled to generate temporal dataframes prescribing the occurences of the keywords. This portion of the code will
be integrated with functions in the ```Analyzer.py``` and ```Visualizer.py``` scripts.
- Since Chapters on Springer are not indexed with date of publication, we are currently scraping abstracts of articles only. This modification
can be reverted by changing a single line of code. Check the commit corresponding to this date for the same.
- The temporally assorted dataframe will be used to generate the trends histogram.

### Date: 14/01/2019
- The code was broken following a update to the UI of Springer. The attribute pertaining to the number of results found had to changed from ```class``` to ```id```.
- Happy New Year 2019!

### Date: 31/12/2018
- The ```status_logger()``` function has been incorporated into the <a title="Analyzer.py" href="https://github.com/SarthakJShetty/Bias/blob/master/Analyzer.py">```Analyzer.py```</a> and <a title="NLP_Engine.py" href="https://github/com/SarthakJShetty/Bias/blob/master/NLP_Engine.py">```NLP_Engine.py```</a> code. The functions working is now being logged into the logger file.
- A new ```results_determiner()``` function has been writter than presents the number of results returned and to be scraped.
- New set of runs results alongwith visualizations have been put up <a title="Latest run LOG file" href="Latest run log files" href="https://github.com/SarthakJShetty/Bias/blob/master/LOGS/LOG_2018-12-31_13_45_Western_Ghats_Ecology_Conservation_Policy">here</a>.

### Date: 29/12/2018
- Long time since updates were posted. The code has been moved to ```conda```.
- An <a title="NLP_Engine.py" href="https://github.com/SarthakJShetty/Bias/blob/master/NLP_Engine.py">NLP Engine</a> has been put in place to analyze the relation between different words and build the LDA model.
- Analyzer functionality has largely been ported to the NLP Engine.
- The latest run complete with the visualization of the LDA Model can be found <a title="Latest run log files" href="https://github.com/SarthakJShetty/Bias/blob/master/LOGS/LOG_2018-12-29_16_50_Western_Ghats_Endemic_Crocodiles_Marshes/">here</a>.

### Date: 08/10/2018
- The code employs a ```conda``` environment on Windows, and ```virtualenv``` on Ubuntu. Code has been tested on both environments successfully.
- Instructions on the <a title="README.md" href="https://github.com/SarthakJShetty/Bias#analyzing-biases-in-academic-publications">```README.md```</a> has been updateed accordingly.

### Date: 24/09/2018
- Changed the manner in which the abstract_id's are scraped.
- Change from ```download-link``` to ```preview-link```.
- Script can scrap once again.

### Date: 15/09/2018
- The ```Analyzer.py``` code is almost ready.
- Data from the ```Abstracts.txt``` file is being converted into a ```pandas``` dataframe for ease of analysis.
- ```pandas``` works better than the native ```csv``` library. Tried to work it out with ```csv```, but could not.
- Will add a few newer LOGS here.
- <strong>Update:</strong> <a title="Analyzer" href="https://github.com/SarthakJShetty/Bias/blob/master//Analyzer.py">```Analyzer.py```</a> code is ready. Next stop, ```Visualizer.py```.

### Date: 12/09/2018
- Fragmenting the code into bits. Wrote a new <a title="Bias.py" href="https://github.com/SarthakJShetty/Bias/blob/master/Bias.py" target="_blank">```Bias.py```</a>, script which will consilidate the different pieces of code that are a part of this project.
- <a title="pre_processing.py" href="https://github.com/SarthakJShetty/Bias/blob/master/common_functions.py" target="_blank">```common_functions.py```</a> contains functions that will be borrowed by the Scraper, Analyzer & Visualizer.
- Code works by sharing functions, across different scripts. <a title="Scraper.py" href="https://github.com/SarthakJShetty/Bias/blob/master/Scraper.py">```Scraper.py```</a> has specialized functions post fragmentation.

### Date: 10/09/2018
- Writing a shell script to get necessary packages (although this seems unnecessary).
- Will try to get the ```Analyzer.py``` up and running by tomorrow.
- New <a title="LOGs" href="https://github.com/SarthakJShetty/Bias/blob/master/LOGS">LOGS</a> have been added.

### Date: 09/09/2018
- Will be part of a ```virtualenv``` environment from now on.
- Should be easier to download ```pip``` packages.
- Wrote a <a title="Packages required" href="https://github.com/SarthakJShetty/Bias/blob/master/requirements.txt">```requirements.txt```</a> file.
- Testing on Ubuntu and Windows machines now.

### Date: 30/08/2018
- Improved the documentation, added a Abstract counter.
- Code had to be modified after ScienceDirect redesign.
- Multiple abstract ID files are now generated.

### Date: 29/08/2018
- Code could not initially scrape multiple pages.
- Added a small checker, to check if the page contains content, and only then scrape IDs and then abstracts.

### Date: 28/08/2018
- The Scraper.py code is ready.
- It can scrape abstracts off of ScienceDirect and store them in the LOGS folder, corresponding to the date when the  script was run.
