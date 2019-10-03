'''
Hello! This script is part of the larger Bias project that you can check out here: https://github.com/SarthakJShetty/Bias
We are trying to use NLP to understand skewed research themes across biodiversity hotspots.
-Sarthak
(03/10/2019)

Purpose of this script:
Clean the corpus of special character'''

file = '/home/sarthak/projects/Bias/BackUp_Journal_LOGS/Test_Bed_Master_Copy/Cleaned_Corpus.txt'
folder = open(file, 'r')
abstracts = []

for line in folder:
    abstracts.append(line)

#This holds the elements of the abstract after it has been split at the spaces
elements = []
#Holds the dirty elements that contain the \\ and // in them
dirty_elements = []
#Holds the clean members of the abstract elements
cleaned_str_list = []
#Holds the screened abstracts, null of any special character occurances
cleaned_texts = []

'''What needs to be implemented here?
1. A way for each element containing \\ to be put into a list.
2. subtract said list from elements'''

def dirty_element_generator(texts):
    for text in texts:
        elements = text.split(" ")
        for element in elements:
            if('\\' in element):
                dirty_elements.append(element)
    return dirty_elements

def dirty_element_weeder(texts, dirty_elements):
    for text in texts:
        elements = text.split(" ")
        for element in elements:
            if element not in dirty_elements:
                cleaned_str_list.append(element)
        cleaned_texts.append(" ".join(lol for lol in cleaned_str_list))
        cleaned_str_list = []
    return cleaned_texts

def cleaner_main():
    dirty_element_generator(abstracts)
    dirty_element_weeder(abstracts, dirty_elements)