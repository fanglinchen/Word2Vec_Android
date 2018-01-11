# Word2Vec for Android App Corpus

Wording embeddings is a powerful tool that provide vector representations of word meanings. Based on the distributional hypothesis where the context for each word is its nearby words, we can train word embeddings using some large-scale corpus to learn the vector representations. These word vectors, can be used for semantic analysis and other languange classification tasks. 

To facilitate other researchers for basic languange analysis task, many NLP researchers have released some pretrained word embeddings. This repository is for sharing our pretrained word embeddings on the vocabulary of mobile app development, which can be used for other researchers interested in understanding the language pattern in the domain smartphone app software engineering or analyzing mobile apps using NLP methods. 

Archive.org has the official and the most up-to-date Stack Exchange data dump up here:

https://archive.org/details/stackexchange

The dataset is fully structured in XML, so we can use this structure information for data filtering. Since we are only interested in the language of mobile app developments, we leverage the Tag information in each post to only select the Android related posts. 
