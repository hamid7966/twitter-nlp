#name: hamidreza khosravi
#ID: 9511211140
# -*- coding: utf-8 -*-import twitter_config
import os, fnmatch, codecs

counter = 0
inverted_indext = {}
for dirpath, dirs, files in os.walk('nlp/step2'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename), 'r', encoding="utf-8")as f:

            for word in f.read().split():
                if word not in inverted_indext:
                    list = []
                    list.append(str(filename).replace(".txt", ""))
                    data = {"c": 1, "l": list}
                    inverted_indext[word] = data

                else:
                    list = []
                    inverted_indext[word]["c"] += 1
                    for a in inverted_indext[word]["l"]:
                        list.append(a)

                    list.append(str(filename).replace(".txt", ""))
                    inverted_indext[word]["l"] = list;

            f.close();

h = input("******lotfan yek ebarat ra vared konid******* : ")
list = []
commonList = []

for v in h.split():
    if (v in inverted_indext) :
        if (len(list) > 0):
            List = set(List) & set(inverted_indext[v]["l"])
        else:
            List = inverted_indext[v]["l"]

        commonList = set(commonList) | set(inverted_indext[v]["l"])

twitter_nlp="nlp/step2/"

if (len(List) > 0) :
    for a in List:
        f = codecs.open(os.path.join(twitter_nlp, a + ".txt"), 'r', encoding="utf-8")
        print(f.read() + "\n" + "*" * 20)


commonList = set(commonList) - set(List)

if (len(commonList) > 0):
    for a in commonList:
        f = codecs.open(os.path.join(twitter_nlp, a + ".txt"), 'r', encoding="utf-8")
        print(f.read() + "\n" + "*" * 20)


