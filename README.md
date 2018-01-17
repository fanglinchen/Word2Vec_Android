## Word2Vec for Android App Corpus

Wording embeddings is a powerful tool for vector representations of words. Based on the distributional hypothesis where the context for each word is its nearby words, we can train word embeddings using some large-scale corpus to learn the vector representations. These word vectors, can be used for NLP tasks such as semantic analysis, text classification, or topic clustering.

To facilitate other researchers to perform basic language analysis using word embeddings, many NLP researchers have released some pre-trained word embeddings. This repository is for sharing our pre-trained word embeddings on the vocabulary of mobile app development, which can be used for other researchers interested in understanding the language pattern in the domain smartphone app software engineering or analyzing mobile apps using NLP methods.  Domain-specific words such as _idx_, _ringtone_ and _phonebook_ are not easily listed in common corpus such as Wikipeida, but they can be found in our corpus. 

Archive.org has the official and the most up-to-date Stack Exchange data dump up here:
https://archive.org/details/stackexchange

The dataset is fully structured in XML, so we can use this structure information for data filtering. Since we are only interested in the language of mobile app developments, we leverage the Tag information in each post to only select the Android related posts. As of today, the number of posts with Android Tag ranks the 5th place in the whole Stackoverflow site. 

Commands:
mysql --user=root --password=Ugdvqh#1372 --database=stackoverflow < create_answer_table.sql


