#name: hamidreza khosravi
#ID: 9511211140
# -*- coding: utf-8 -*-import twitter_config

import os, fnmatch, codecs
import pathlib

counter = 0
inverted_indext = {}

for dirpath, dirs, files in os.walk('nlp/step2'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename), 'r', encoding="utf-8")as file:

            for word in file.read().split():
                if word not in inverted_indext:
                    list= []
                    list.append(str(filename).replace(".txt" , ""))
                    data = {
                        'str' :
                            1 , "l" : list
                    }
                    inverted_indext[word] = data

                else:

                    list = []
                    inverted_indext[word]["str"] += 1
                    for a in inverted_indext[word]["l"]:
                        list.append(a)

                    list.append(str(filename).replace(".txt" , ""))
                    inverted_indext[word]["l"] = list


            file.close()


f = open("nlp/step5/inverted-index.txt","w",encoding="utf-8")
for x in inverted_indext:
    f.write(x + "," +  str(inverted_indext[x]["str"]))
    for a in inverted_indext[x]["l"]:
        f.write(","+str(a))
    f.write("\n")

