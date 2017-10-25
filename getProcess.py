'''
Getting a shorter Python Text file
- helpers:
- https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
- https://stackoverflow.com/questions/33726361/counting-the-number-of-unique-words-in-a-list

- [sA -10/24/2017]    Added Pickle functionality , Currently using the en_US.news.txt and filtering to 5% of the data only
'''
import os
import nltk,re,string
from nltk import word_tokenize
import time
import pickle

class parsecorpus(object):
    """docstring for parsecorpus."""
    def __init__(self):
        super(parsecorpus, self).__init__()

    def filtercorpus(self, path1, path2, path3, filtersize):
        #f1 = open(path1,'r+',encoding="utf-8")
        #f2 = open(path2,'w+',encoding="utf-8")
        f1 = open(path1,'r+')
        f2 = open(path2,'w+')
        #f3 = open(path3,'wb')
        x = f1.readlines()

        sizehere = int(filtersize*len(x))
        for i in range(0, int(filtersize*len(x))):
            f2.write(x[i])

        #pickle.dump(x[0:sizehere],f3)


        f1.close()
        f2.close()
        #f3.close()

        return x[0:sizehere]

    def clean1(self,lines):
        cleanedLines = [re.sub(r'[^(a-z|A-Z|\s+)]','',line) for line in lines]
        return cleanedLines

    def tokenize(self, lines):
        tokensperline_cleaned = []
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        tokenized = [word_tokenize(line) for line in lines]
        # you need the below if you choose to not use clean1
        # for line in tokenized:
        #     newline = []
        #     for token in line:
        #         new_token = regex.sub(u'', token)
        #         if not new_token == u'':
        #             newline.append(new_token)
        #     tokensperline_cleaned.append(newline)
        #return tokensperline_cleaned.append
        return tokenized

    def uniquewords(self, tokens):
        uniquewords = set()
        for word in tokens:
            for item in word:
                uniquewords.add(item)
        return len(uniquewords)


obj = parsecorpus()

#path1 = "C://Public//Data-Science[JHU-Coursera]//project_nlp//final//en_US//en_US.news.txt"
#path2 = "C://Public//Data-Science[JHU-Coursera]//project_nlp//final//en_US//en_US_new_flt.txt"

path1= "C://Dropbox//Delete_Me//nlp//en_US.news.txt"
path2= "C://Dropbox//Delete_Me//nlp//en_US_new_flt.txt"
path3= "C://Dropbox//Delete_Me//nlp//en_US_new_flt.pkl"

start = time.clock()
filtersize = 0.05 #user input , change to make the filter bigger or smaller for the corpus
res = obj.filtercorpus(path1, path2, path3, filtersize)
cleanedLines = obj.clean1(res)
cleaned_tokens = obj.tokenize(cleanedLines)
uniqWords = obj.uniquewords(cleaned_tokens)
print("Get the Unique Words",uniqWords)
print("time taken for filtering with filtersize = {:+f}".format(filtersize), time.clock()-start)
