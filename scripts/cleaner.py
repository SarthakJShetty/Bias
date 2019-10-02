file = '/home/sarthak/projects/Bias/BackUp_Journal_LOGS/Test_Bed_Master_Copy/Cleaned_Corpus.txt'
folder = open(file, 'r')
texts = []

for line in folder:
    texts.append(line)

elements = []
cleaned_texts = []
dirty_elements = []

'''What needs to be implemented here?
1. A way for each element containing \\ to be put into a list.
2. subtract said list from elements'''

for text in texts:
    elements = text.split(" ")
    for element in elements:
        if('\\' in element):
            dirty_elements.append(element)
        cleaned_texts.append(new_element for new_element in elements if new_element not in dirty_elements)
    cleaned_texts.append('\n')