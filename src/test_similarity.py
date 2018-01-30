#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import logging
import os.path
import sys
import numpy as np
 
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from gensim.models.word2vec import LineSentence
from scipy import spatial
from argparse import ArgumentParser
import argparse


def average_word_vectors(model, phrase):
    phrase= phrase.split()
    feature = None
    for i, word in enumerate(phrase):
        if i==0:
            feature = np.array(model.wv[word])
        else:
            feature += np.add(feature, model.wv[word])
    n_words = len(phrase)
    if (n_words > 0):
        feature = np.divide(feature, n_words)

    return feature

def get_phrase_similarity(model, phrase1, phrase2):
    vector1 = average_word_vectors(model, phrase1)
    vector2 = average_word_vectors(model, phrase2)

    return 1 - spatial.distance.cosine(vector1, vector2)

def arg_parse():


    return arg_p


def main(args):
    model = Word2Vec.load("../data/android.word2vec.model")
    parser = ArgumentParser('test script for word embeddings on android corpus')
    parser.add_argument('-w', '--word', type=str, default=None)
    parser.add_argument('-a', '--phrase_a', type=str, default = None)
    parser.add_argument('-b', '--phrase_b', type=str, default = None)
    arg_p = parser.parse_args()
    word =  arg_p.word
    phrase_a =  arg_p.phrase_a
    phrase_b = arg_p.phrase_b
    if word != None:
        print "Most relevant words to '" + word + "':  "
        results= model.wv.most_similar(word)
        for each in results:
            print each[0] +" "+str(each[1]) + "  "

    if phrase_a != None and phrase_b != None:
        print "The similarity between the phrase '" + phrase_a + "' and the phrase '" + phrase_b + "' is:" + str(get_phrase_similarity(model, phrase_a, phrase_b))

if __name__ == "__main__":
    main(sys.argv[1:])
    

    