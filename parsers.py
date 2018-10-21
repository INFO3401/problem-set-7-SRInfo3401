#Worked with Luke, Marissa, Harold
#############################################################
# PART #1
################################################################################
import os
import string

def countWordsUnstructured(filename):
    
    wordCounts={}
    Trump_file = open(filename)
    for word in Trump_file.read().split():
        if word not in wordCounts:
            wordCounts[word] = 1
        else:
            wordCounts[word] += 1
    return(wordCounts)
    Trump_file.close();
    
Trump2017 = countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Trump_2017.txt')

#############################################################
# PART 2
################################################################################
import csv
def generateSimpleCSV(targetfile, wordCounts):
    
    with open (targetfile, 'w') as csv_file:
        csvcreate = csv.writer(csv_file)
        csvcreate.writerow(['Word', 'Count'])
        for key,value in wordCounts.items():
            csvcreate.writerow([key,value])
            
    csv_file.close()
    return csv_file

WC_CSV_Trump2017 = generateSimpleCSV("targetfile.csv", Trump2017)
    # This function should transform a dictionary containing word counts to a
#generateSimpleCSV(wordCounts)
    # CSV file. The first row of the CSV should be a header noting:
    # Word, Count
    # Inputs: A word count list and a name for the target file
    # Outputs: A new CSV file named targetfile containing the wordcount data

################################################################################
# PART 3
################################################################################
from os import listdir
def countWordsMany(directory):
    
    dir_list = listdir(directory)
    countdict = {}
    for file in dir_list:
        all_wc = countWordsUnstructured(directory + "/" + file)
        countdict[file] = all_wc
         
    return countdict

all_wc_dict = countWordsMany('./state-of-the-union-corpus-1989-2017')
#print(all_wc_dict)

    # This function should create a dictionary of word count dictionaries
    # The dictionary should have one dictionary per file in the directory
    # Each entry in the dictionary should be a word count dictionary
    # Inputs: A directory containing a set of text files
    # Outputs: A dictionary containing a word count dictionary for each
    #          text file in the directory

################################################################################
# PART 4
################################################################################
def generateDirectoryCSV(wordCounts, targetfile):
    
    with open (targetfile, 'w') as csv_file:
        csvcreate = csv.writer(csv_file)
        csvcreate.writerow(['Filename', 'Word', 'Count'])
        for key,value in wordCounts.items():
            csvcreate.writerow([key,value])
            
    csv_file.close()
    return csv_file

gen_dir_csv = generateDirectoryCSV(all_wc_dict, "targetfile1.csv")
    # This function should create a CSV containing the word counts generated in
    # part 3 with the header: 
    # Filename, Word, Count
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: A CSV file named targetfile containing the word count data

################################################################################
# PART 5
################################################################################
def generateJSONFile(wordCounts, targetfile):
    JSON_file = open(targetfile, "w")
    JSON_file.write(str(wordCounts).replace("\'", "\""))
    
    JSON_file.close()
    return JSON_file

generateJSONFile(all_wc_dict, "targetfile.json")
    # This function should create an containing the word counts generated in part 3.
    # Architect your JSON file such that the hierarchy will allow the user to quickly navigate and compare word counts between files. 
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: An JSON file named targetfile containing the word count data

################################################################################
# PART 6
################################################################################
#def searchCSV(csvfile, word):
    
    #top_wordcount_doc = ""
    #top_wordcount = 0
    
    #with open (csvfile) as csv_file:
        #file = csv.reader(csv_file)
        
        #for line in file:
            #if line[1] == word and int(line[2])> int(top_wordcount):
                #top_wordcount_doc = line[0]
                #top_wordcount = line[2]
                
    #csv_file.close()
    #return top_wordcount_doc

#print(searchCSV("targetfile1.csv", "our")
    # This function should search a CSV file from part 4 and find the filename
    # with the largest count of a specified word
    # Inputs: A CSV file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
#import json
#def searchJSON(JSONfile, word):
    
    #top_wordcount_doc = ""
    #top_wordcount = 0
    
    #with open (JSONfile) as json_file:
        #data = json.load(json_file)
        
        #for file in data:
            #if data[file][word]> top_wordcount:
                #top_wordcount_doc = file
                #top_wordcount = data[file][word]
                
    #json_file.close()
    #return top_wordcount_doc
      
#print(searchCSV("targetfile.csv", "our"))
#print(searchJSON("targetfile.json", "our"))
    #Issue (JSONDecodeError: Expecting ':' delimiter) maybe due to non array json file creation format...?(countless hours on stackoverflow and asking peers questions, part 6 defeated my code)
    # This function should search a JSON file from part 5 and find the filename
    # with the largest count of a specified word
    # Inputs: An JSON file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    
# Test your part 6 code to find which file has the highest count of a given word

# +1 bonus point for figuring out how many datapoints you had to process to 
# compute this value

################################################################################
#Problem Set 6
#Part 2
################################################################################

#Table 1 = State-of-the-Union-WordCount
    #Column 1 = text "filename",
    #Column 2 = text "Word",
    #Column 3 = integer "Count",
        
#Table 2 = US-Presidents-Info
    #Column 1 = integer "Idx",
    #Column 2 = integer "number",
    #Column 3 = date "start",
    #Column 4 = date "end",
    #Column 5 = text "president",
    #Column 6 = text "prior",
    #Column 7 = text "party",
    #Column 8 = text "vice",

#Based on this database schema I could connect the tables through president names or years serving as president connecting to the start and end dates. Finding connecting data will reduce redundant information that is non present in one or the other table sets. This idea should intergrate all of the data from both sources while minimizing the amout of redundant information.

################################################################################
#Part 3
################################################################################
#import sqlite3
#conn = sqlite3.connect('sotu_speaches.db')
#c = conn.cursor()

#c.execute(''' CREATE TABLE State_of_the_Union_WordCount (filename text, Word text, Count real)''')
#c.execute(''' CREATE TABLE US_Presidents_Info (idx real, number real, start date, end date, president text, prior text, party text, vice text)''')

#conn.commit()
#conn.close()