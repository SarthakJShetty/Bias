file_of_text = '/home/sarthak/projects/Bias/BackUp_Journal_LOGS/Training_Data/LOG_2019-12-26_12_26_Eastern_Afromontane_Conservation/Abstract_Database_2019-12-26_12_26_CLEANED.txt'
open_file = open(file_of_text, 'r')
texts = ""
for line in open_file:
    for charac in line:
        if(charac!='\n'):
            #print(charac)
            texts+=charac
        else:
            print('\n')
new_texts = 'new.txt'
hello_list = []
hello_list.append(texts)
new_file = open(new_texts, 'w')
counter  = 0
for line in texts:
    counter += 1
    new_file.write(line)
    #print(counter)  
print(type(texts))
print(len(hello_list))