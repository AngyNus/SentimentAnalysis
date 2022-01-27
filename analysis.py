
"""
This sample project using nltk.sentiment.vader package
and googletrans package to translate 30 Facebook statuses from Hebrew to English and define their level of the sentiments this status want to express.
If there are more negative or positive words, and what
aproximatly will be the feelling of the avarage human reading this status.

"""

#from nltk.sentiment.vader import SentimentIntensityAnalyzer

from typing import Any
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#from vaderSentiment import nltk

import nltk
from googletrans import Translator


nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


translator = Translator()

# open statuses file
with open("status.txt", 'r', encoding='utf-8') as status:
    # string for the complete status
    
    sts = " "
    count = 1
    log_file = open('AnalysisLog.txt', 'w')
    for line in status:
        #print(line)
        he_sentence = translator.translate(line)
        sts += he_sentence.text
        if len(line.strip()) == 0:
            print(count)
            log_file.write('\n')
            log_file.write(str(count) + "  - " )
            
            print(sts)
            #log_file.write(sts)
            print(sid.polarity_scores(sts), '\n')
            log_file.write(str(sid.polarity_scores(sts)))
            count += 1
            sts = " "
log_file.close()