'''This script is part of the larger Bias project [https://github.com/SarthakJShetty/Bias]. Here, the biodiversity specific corpus generated from the rest
of the Bias pipeline is converted to a single line so that the NLP Engine can provide the distribution of topics across the entire corpus.'''

'''This directs the code to the .txt file that has to be converted to a line.'''
file_of_text = '/home/sarthak/projects/Bias/BackUp_Journal_LOGS/Training_Data/LOG_2019-12-26_12_26_Eastern_Afromontane_Conservation/Abstract_Database_2019-12-26_12_26_CLEANED.txt'
open_file = open(file_of_text, 'r')
texts = ""
for line in open_file:
    for charac in line:
        if(charac!='\n'):
            '''Concatanate all the characters that you encounter into a single string unless if a new line character is encountered.'''
            texts+=charac
        else:
            '''Even if a \n is encountered just print it. For the purpose of debugging solely.'''
            print('\n')

'''This is the new filename of the single-line file which contains the corpus data.'''
new_file_of_text = file_of_text.split(".")[0]+"_LINE.txt"

'''We introduce a start element here because the NLP Engine's indexing begins from 1.
To prevent the corpus string from being left out of the processing, we introduce a fake 0th element here,
and index the corpus string at index number 1.'''
new_list = ["Hello\n"]

'''Converting the string into a list element.'''
new_list.append(texts)

'''Open the filename specified above in write mode.'''
new_file = open(new_file_of_text, 'w')

'''Write the string to the new file declared.'''
for line in new_list:
    new_file.write(line)