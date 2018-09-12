# Build-Log

### Date: 28/09/2018
- The Analyzer.py code is ready.
- It can scrape abstracts off of ScienceDirect and store them in the LOGS folder, corresponding to the date when the
script was run.

### Date: 29/09/2018
- Code could not initially scrape multiple pages.
- Added a small checker, to check if the page contains content, and only then scrape IDs and then abstracts.

### Date: 30/09/2018
- Improved the documentation, added a Abstract counter.
- Code had to be modified after ScienceDirect redesign.
- Multiple abstract ID files are now generated.

### Date: 09/09/2018
- Will be part of a ```virtualenv``` environment from now on.
- Should be easier to download ```pip``` packages.
- Wrote a <a title="Packages required" href="https://github.com/SarthakJShetty/Bias/master/requirements.txt">```requirements.txt```</a> file.
- Testing on Ubuntu and Windows machines now.

### Date: 10/09/2018
- Writing a shell script to get necessary packages (although this seems unnecessary).
- Will try to get the ```Analyzer.py``` up and running by tomorrow.
- New <a title="LOGs" href="https://github.com/SarthakJShetty/Bias/master/LOGS">LOGS</a> have been added.

### Date: 12/09/2018
- Fragmenting the code into bits. Wrote a new <a title="Bias.py" href="https://github/SarthakJShetty/Bias/master/Bias.py" target="_blank">```Bias.py```</a>, script which will consilidate the different pieces of code that are a part of this project.
- <a title="pre_processing.py" href="https://github/SarthakJShetty/Bias/master/common_functions.py" target="_blank">```common_functions.py```</a> contains functions that will be borrowed by the Scraper, Analyzer & Visualizer.
- Code works by sharing functions, across different scripts. <a title="Scraper.py" href="https://github/SarthakJShetty/Bias/master/Scraper.py">```Scraper.py```</a> has specialized functions post fragmentation.