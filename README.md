## Word2Vec for Android App Corpus

Wording embeddings is a powerful tool for vector representations of words. Based on the distributional hypothesis where the context for each word is its nearby words, we can train word embeddings using some large-scale corpus to learn the vector representations. These word vectors, can be used for NLP tasks such as semantic analysis, text classification, or topic clustering.

To facilitate other researchers to perform basic language analysis using word embeddings, many NLP researchers have released some pre-trained word embeddings. This repository is for sharing our pre-trained word embeddings on the vocabulary of mobile app development, which can be used for other researchers interested in understanding the language pattern in the domain smartphone app software engineering or analyzing mobile apps using NLP methods.  Domain-specific words such as _idx_, _ringtone_ and _phonebook_ are not easily listed in common corpus such as Wikipeida, but they can be found in our corpus. 

Archive.org has the official and the most up-to-date Stack Exchange data dump up here:
https://archive.org/details/stackexchange

The dataset is fully structured in XML, so we can use this structure information for data filtering. Since we are only interested in the language of mobile app developments, we leverage the Tag information in each post to only select the Android related posts. As of today, the number of posts with Android Tag ranks the 5th place in the whole Stackoverflow site. 


Examples:

Most similar words to 'evernote':  
icloud 0.644747257233  
instagram 0.630041241646  
dropbox 0.616084516048  
outlook 0.6095713377  
linkedin 0.606443405151  
gmail 0.590190827847  
ebay 0.573595881462  
spotify 0.573144376278  
katana 0.563836157322  
netflix 0.563594222069  

Most relevant words to 'png':  
jpg 0.77312374115  
imagestyle 0.619917273521  
jpeg 0.577209472656  
logo 0.565427184105  
mdpi 0.555353403091  
desert 0.553858458996  
gif 0.551429510117  
psd 0.547872543335  
lrg 0.545428574085  
anaglyph 0.537024497986  

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

Most relevant words to 'calendar':  
cal 0.788251042366  
calender 0.751141250134  
hijri 0.623105466366  
jalali 0.611498951912  
chronology 0.593332648277  
month 0.583001077175  
day 0.57461977005  
year 0.574377954006  
lastyear 0.569179534912  
hour 0.537207901478  

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

