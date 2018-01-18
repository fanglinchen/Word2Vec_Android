#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import logging
import os.path
import sys
import multiprocessing
 
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
 
if __name__ == '__main__':
    model = Word2Vec.load("android.word2vec.model")
    
    print "most similar word to pic:"
    print model.wv.most_similar("pic")
    print "most similar words to blob:"
    print model.wv.most_similar("blob")
    print "most similar word to proto:"
    print model.wv.most_similar("proto")
    print "most similar word to gregorian"
    print model.wv.most_similar("gregorian")
    