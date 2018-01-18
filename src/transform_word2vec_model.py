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
    model.wv.save_word2vec_format("android.en.text.vector", binary=False)