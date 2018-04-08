# -*- coding: utf-8 -*-import twitter_config
import os,fnmatch,codecs


counter = 0
x=1
h=[]
m =open("nlp/step4/stop_words.txt","w",encoding="utf-8")
for line in open("nlp/step3/word-frequency.txt","r",encoding="utf-8"):
            for word in line.split():
                h.append(word[:word.find(":")])
                if(x>20):
                    break
                else:
                    m.write(word[:word.find(":")]+"\n")
                x+=1
m.close()
for dirpath, dirs, files in os.walk('step2'):
    for filename in fnmatch.filter(files, '*.txt'):
        f=open("nlp/step4/"+filename+".txt","w",encoding="utf-8")
        with codecs.open(os.path.join(dirpath, filename), 'r', encoding="utf-8") as file:
            for word in file.read().split():
                if word not in h:
                    f.write(word+" ")
        f.close()
