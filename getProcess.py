'''
Getting a shorter Python Text file
- helpers:
- https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
- https://stackoverflow.com/questions/33726361/counting-the-number-of-unique-words-in-a-list
- https://stackoverflow.com/questions/9394803/python-combine-two-for-loops
- http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/
- [sA -10/24/2017]    Added Pickle functionality , Currently using the en_US.news.txt and filtering to 5% of the data only
- [sA -10/27/2017]    Extract Bigrams/n-grams as a list of tuples
'''
import os
import nltk,re,string
from nltk import word_tokenize
import time
import pickle
import numpy as np

class parsecorpus(object):
    """docstring for parsecorpus."""
    def __init__(self):
        super(parsecorpus, self).__init__()
        self.dict = {}
        self.v_count = 0
        self.unique_words = set()

    def filtercorpus(self, path1 = './en_US.news.txt', path2 = None, path3 = None, filtersize = 0.05):
        f1 = open(path1,'r+',encoding="utf-8")
        f2 = open(path2,'w+',encoding="utf-8")
        #f1 = open(path1,'r+')
        #f2 = open(path2,'w+')
        #f3 = open(path3,'wb')
        x = f1.readlines()

        sizehere = int(filtersize*len(x))
        for i in range(0, sizehere):
            f2.write(x[i])

        f1.close()
        f2.close()
        #f3.close()

        return x[:sizehere]

    def clean1(self,lines):
        cleanedLines = [re.sub(r'[^(a-z|A-Z|\s+)]','',line) for line in lines]
        return cleanedLines

    def tokenize(self, lines):
        # tokensperline_cleaned = []
        # regex = re.compile('[%s]' % re.escape(string.punctuation))
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

    def ngram(self, sentencelist, n):
        temp = [list(zip(*[s[i:] for i in range(n)])) for s in sentencelist]
        res = [tup for x1 in temp for tup in x1]
        return res

    def uniquewords(self, tokens):
        for word in tokens:
            for item in word:
                if item not in self.unique_words:
                    self.dict[item] = self.v_count
                    self.v_count += 1
                self.unique_words.add(item)
        return len(self.unique_words)

    def vectorize(self, X):
        """
        input: n-gram string vectors
        e.g. X = [['the', 'quick', 'fox'], ['quick', 'fox', 'jumped']]
        output: centerWord-contextWord vector pairs. X_vec, y_vec
        """
        N = len(X)
        M = self.v_count
        C = len(X[0]) - 1   # number of context words
        X_vec = np.zeros(shape = (N, M))
        y_vec = np.zeros(shape = (N, M, C))
        for i, tup in enumerate(X):
            for j, w in enumerate(tup):
                if j == 0:
                    X_vec[i][self.dict[w]] = 1
                else:
                    y_vec[i][self.dict[w]][j-1] = 1
        return X_vec, y_vec

def dataProcessing(parser, corpus_path, filter_size = 0.03, n_gram = 2):
    """
    Params:
        input:
            Corpus parser object, document path, filter size and number of grams
        output:
            One-hot vectors X, y, ready for training neural networks
    """
    parser.filtercorpus(corpus_path, filtersize = filter_size)
    cleanedLines = parser.clean1(res)
    cleaned_tokens = parser.tokenize(cleanedLines)
    print ('Volcabulary size is %d' % parser.uniquewords(cleaned_tokens))
    ngrams_vec = parser.ngram(cleaned_tokens, n)
    return parser.vectorize(ngram_vecs)
