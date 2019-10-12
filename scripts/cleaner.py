'''
Hello! This script is part of the larger Bias project that you can check out here: https://github.com/SarthakJShetty/Bias
We are trying to use NLP to understand skewed research themes across biodiversity hotspots.
-Sarthak
(03/10/2019)

Purpose of this script:
Clean the corpus of special character'''

# This holds the elements of the abstract after it has been split at the spaces
elements = []
# Holds the dirty elements that contain the \\ and // in them
dirty_elements = []
# Holds the clean members of the abstract elements
cleaned_str_list = []
# Holds the screened abstracts, null of any special character occurances
cleaned_texts = []

'''What needs to be implemented here?
1. A way for each element containing \\ to be put into a list.
2. Subtract said list from elements'''

def txt_to_list(abstract_directory):
    folder = open(abstract_directory, 'r')
    abstracts = []

    for line in folder:
        abstracts.append(line)

    return abstracts

def dirty_element_generator(texts):
    '''Finds all the elements which have the special character in them, makes a list and
    referes through them durng the next phases'''
    for text in texts:
        elements = text.split(" ")
        for element in elements:
            if('\\' in element):
                dirty_elements.append(element)
    return dirty_elements

def dirty_element_weeder(texts, dirty_elements):
    '''Refers to the list of dirty variables and cleans the abstracts'''
    cleaned_str_list =[]
    for text in texts:
        elements = text.split(" ")
        for element in elements:
            if element not in dirty_elements:
                cleaned_str_list.append(element)
        cleaned_texts.append(" ".join(lol for lol in cleaned_str_list))
        cleaned_str_list = []
    return cleaned_texts

def cleaned_abstract_dumper(abstract_directory, cleaned_texts):
    '''Dumping the cleaned abstracts to the disc and will be referring to it henceforth in the code'''
    pre_new_cleaned_texts_folder = abstract_directory.split(".txt")[0]
    new_cleaned_texts_folder = open(pre_new_cleaned_texts_folder + "_CLEANED.txt", 'w')

    for cleaned_text in cleaned_texts:
        new_cleaned_texts_folder.write(cleaned_text)
        new_cleaned_texts_folder.write('\n')
    return new_cleaned_texts_folder

def cleaner_main(abstract_directory):
    abstracts = txt_to_list(abstract_directory)
    dirty_elements = dirty_element_generator(abstracts)
    cleaned_texts = dirty_element_weeder(abstracts, dirty_elements)
    new_cleaned_texts_folder = cleaned_abstract_dumper(abstract_directory, cleaned_texts)
    '''Main contribution from this block of the code is the new cleaned .txt folder and cleaned abstracts. Just in case.'''
    return cleaned_texts, new_cleaned_texts_folder

abstract_directory = '/home/sarthak/projects/Bias/BackUp_Journal_LOGS/Corpus_Bio_Hotspot_Data/WesternGhats_Springer_ScienceDirectOnly.txt'
cleaner_main(abstract_directory)