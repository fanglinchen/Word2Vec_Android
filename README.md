## Word2Vec for Android App Corpus

Wording embeddings is a powerful tool for vector representations of words. Based on the distributional hypothesis where the context for each word is its nearby words, we can train word embeddings using some large-scale corpus to learn the vector representations. These word vectors, can be used for NLP tasks such as semantic analysis, text classification, or topic clustering.

To facilitate other researchers to perform basic language analysis using word embeddings, many NLP researchers have released some pre-trained word embeddings. This repository is for sharing our pre-trained word embeddings on the vocabulary of mobile app development, which can be used for other researchers interested in understanding the language pattern in the domain of smartphone app software engineering or analyzing mobile apps using NLP methods.  Domain-specific words such as _idx_, _ringtone_ and _phonebook_ are not easily listed in common corpus such as Wikipedia, but they can be found in our corpus. 

Archive.org has the official and the most up-to-date Stack Exchange data dump up here:
https://archive.org/details/stackexchange

The dataset is fully structured in XML, so we can use this structure information for data filtering. Since we are only interested in the language of mobile app developments, we leverage the Tag information in each post to only select the Android related posts. As of today, the number of posts with Android Tag ranks the 5th place in the whole Stackoverflow site. 


Here are some results to give you some impressions about the performance. 


Most relevant words to 'idx':  
cur 0.644603133202  
cols 0.615386128426  
cnt 0.613066792488  
index 0.605373263359  
len 0.603544354439  
charat 0.598465681076  
num 0.567819356918  
substring 0.563846111298  
arrs 0.556287288666  
hist 0.547807812691  

Most relevant words to 'val':  
str 0.660461187363  
temp 0.594926834106  
arr 0.576850533485  
var 0.573238134384  
integer 0.564527213573  
valuer 0.560020267963  
value 0.554349899292  
tempa 0.547556340694  
myint 0.541466355324  
num 0.53715968132  

Most relevant words to 'stream':  
buffered 0.62129753828  
reader 0.544205665588  
piped 0.540452182293  
byte 0.539608120918  
socket 0.532683372498  
writer 0.531789541245  
output 0.527552127838  
streams 0.523191034794  
file 0.519219636917  
bytes 0.519147992134  

The embeddings also picked up some human language too:)  

Most relevant words to 'idk':  
dunno 0.693373262882  
heck 0.617326140404  
kera 0.606379508972  
curios 0.58692407608  
hape 0.583016514778  
stubborn 0.582840323448  
happ 0.577402055264  
unclear 0.574401378632  
obv 0.569237947464  
embarassing 0.567026674747  

Most relevant words to 'suck':  
complicate 0.69784373045  
hurt 0.696538448334  
uncomfortable 0.656524300575  
clumsy 0.652829349041  
hurts 0.649841725826  
unintuitive 0.63742518425  
absurd 0.634339094162  
overwhelming 0.633394598961  
sloppy 0.629962265491  
piss 0.625393986702
