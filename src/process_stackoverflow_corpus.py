from __future__ import print_function
 
import logging
import os.path
import six
import sys
from db_connector import DBConnector
import re
from math import log

# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
words = open("enwiki_vocab_min200.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))
# string = "I am currently starting a game engine in Android  first foray into the platform and have the basics in place however i am unsure of the best way to approach resolution independence when using SurfaceView to draw graphics    Looking for pointers as to how to keep the game   sprites etc all looking the same independent of the screen  obviously it wouldn t be efficient to scale all the sprites every frame or store many variations for differing resolutions"
# for word in string.lower().split(" "):
#     print(infer_spaces(word))
#
tag_regex = re.compile('<.*?>')
def remove_tags(string):
    removed = re.sub(tag_regex, '', string)
    return removed

non_english_regex = re.compile('[^A-Za-z]')
def remove_none_english_characters(string):
    string = string.replace("&lt", "")
    string = string.replace("&gt", "")
    
    return " ".join(non_english_regex.split(string))

def remove_extra_spaces(string):
    return re.sub(' +',' ',string)

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) != 2:
        print("Using: python process_stackoverflow_corpus.py stackoverflow_corpus.en")
        sys.exit(1)

    space = " "
    i = 0
    output = open(sys.argv[1], 'w')

    db = DBConnector()
    # sql_query = "SELECT Body from android_posts;"
    sql_query = "SELECT Body from android_answers;"
    cursor = db.get_cursor()
    cursor.execute(sql_query)
    batch_size = 1000
    i = 0
    while True:
        batch = cursor.fetchmany(batch_size)
        if batch == ():
            break
        
        print("new batch..."+str(i))
        i+=1

        for text in batch:
            text = remove_tags(text[0])
            text = remove_none_english_characters(text)
            text = remove_extra_spaces(text)
            text = text.lower()
            words = []
            for originalWord in text.split(" "):
                words.extend(infer_spaces(originalWord).split(" "))
            
            if six.PY3:
                output.write(b' '.join(words).decode('utf-8') + '\n')
            else:
                output.write(space.join(words) + "\n")
            i = i + 1
            if (i % 10000 == 0):
                logger.info("Saved " + str(i) + " posts")

    output.close()
    logger.info("Finished Saved " + str(i) + " posts")