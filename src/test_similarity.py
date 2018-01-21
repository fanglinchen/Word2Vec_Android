#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import logging
import os.path
import sys
import multiprocessing
 
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from gensim.models.word2vec import LineSentence
 
if __name__ == '__main__':
    # model = Word2Vec.load("../data/android.word2vec.model")
    model = KeyedVectors.load_word2vec_format('/Users/fanglinchen/Downloads/GoogleNews-vectors-negative300.bin', binary=True)
    if len(sys.argv) < 2:
        print globals()['__doc__'] % locals()
        sys.exit(1)
    word = sys.argv[1]
    print "Most relevant words to '" + word + "':  "

    results= model.wv.most_similar(word)
    for each in results:
        print each[0] +" "+str(each[1]) + "  "
