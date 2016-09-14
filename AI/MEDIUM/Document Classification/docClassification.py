#!/usr/bin/python
# http://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/
## Open the file with read only permit
f = open('trainingdata.txt')

## Read the first line 
T = int(f.readline())

response = [None] * T
text = [None] * T 
for i in range(T):
    data = f.readline().split()
    response[i] = int(data[0])
    text[i] = data[1:len(data) -1]
    
    
## close the file after reading the lines.
f.close()

import pandas as pd
import numpy as np


d = {'text': text, 'response': response}
df = pd.DataFrame(data=d)


# ANALYSIS
import nltk
import string
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer


### NLP
# The maps have been generated following -
# http://stackoverflow.com/questions/11692199/string-translate-with-unicode-data-in-python
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
remove_number_map = dict((ord(char), None) for char in string.digits)

def remove_numbers_in_string(s):
    '''
    Function to remove numbers in a string.
    Input: string
    Output: string
    '''
#     print(type(s))
    return s.translate(None, string.digits)
#     return s.translate(remove_number_map)

def lowercase_remove_punctuation(s):
    '''
    Function to lowercase string and remove punctuation marks
    Input: string
    Output: string
    '''
    s = s.lower()
    return s.translate(None, string.punctuation)
#     return s.translate(remove_punctuation_map)

# NLTK_STOPWORDS = set(stopwords.words('english'))

STANFORD_STOPWORDS = {'!',
 '!!',
 '!?',
 '"',
 '#',
 '###',
 '$',
 '%',
 '&',
 "'",
 "''",
 "'ll",
 "'m",
 "'s",
 '(',
 ')',
 '*',
 '+',
 ',',
 '-',
 '-lrb-',
 '-lsb-',
 '-rrb-',
 '-rsb-',
 '.',
 '..',
 '...',
 ':',
 ';',
 '<',
 '>',
 '?',
 '?!',
 '??',
 '@',
 '[',
 ']',
 '^',
 '`',
 '``',
 'a',
 'about',
 'above',
 'after',
 'again',
 'against',
 'all',
 'am',
 'an',
 'and',
 'any',
 'are',
 "aren't",
 'arent',
 'as',
 'at',
 'be',
 'because',
 'been',
 'before',
 'being',
 'below',
 'between',
 'both',
 'but',
 'by',
 'can',
 "can't",
 'cannot',
 'cant',
 'could',
 "couldn't",
 'couldnt',
 'did',
 "didn't",
 'didnt',
 'do',
 'does',
 "doesn't",
 'doesnt',
 'doing',
 "don't",
 'dont',
 'down',
 'during',
 'each',
 'few',
 'for',
 'from',
 'further',
 'had',
 "hadn't",
 'hadnt',
 'has',
 "hasn't",
 'hasnt',
 'have',
 "haven't",
 'havent',
 'having',
 'he',
 "he'd",
 "he'll",
 "he's",
 'her',
 'here',
 "here's",
 'heres',
 'hers',
 'herself',
 'hes',
 'him',
 'himself',
 'his',
 'how',
 "how's",
 'hows',
 'i',
 "i'd",
 "i'll",
 "i'm",
 "i've",
 'if',
 'im',
 'in',
 'into',
 'is',
 "isn't",
 'isnt',
 'it',
 "it's",
 'its',
 'itself',
 "let's",
 'lets',
 'me',
 'more',
 'most',
 "mustn't",
 'mustnt',
 'my',
 'myself',
 'no',
 'nor',
 'not',
 'of',
 'off',
 'on',
 'once',
 'only',
 'or',
 'other',
 'ought',
 'our',
 'ours ',
 'ourselves',
 'out',
 'over',
 'own',
 'return',
 'same',
 "shan't",
 'shant',
 'she',
 "she'd",
 "she'll",
 "she's",
 'shes',
 'should',
 "shouldn't",
 'shouldnt',
 'so',
 'some',
 'such',
 'than',
 'that',
 "that's",
 'thats',
 'the',
 'their',
 'theirs',
 'them',
 'themselves',
 'then',
 'there',
 "there's",
 'theres',
 'these',
 'they',
 "they'd",
 "they'll",
 "they're",
 "they've",
 'theyll',
 'theyre',
 'theyve',
 'this',
 'those',
 'through',
 'to',
 'too',
 'under',
 'until',
 'up',
 'very',
 'was',
 "wasn't",
 'wasnt',
 'we',
 "we'd",
 "we'll",
 "we're",
 "we've",
 'were',
 "weren't",
 'werent',
 'what',
 "what's",
 'whats',
 'when',
 "when's",
 'whens',
 'where',
 "where's",
 'wheres',
 'which',
 'while',
 'who',
 "who's",
 'whom',
 'whos',
 'why',
 "why's",
 'whys',
 'with',
 "won't",
 'wont',
 'would',
 "wouldn't",
 'wouldnt',
 'you',
 "you'd",
 "you'll",
 "you're",
 "you've",
 'youd',
 'youll',
 'your',
 'youre',
 'yours',
 'yourself',
 'yourselves',
 'youve',
 '{',
 '}'} 

def remove_stopwords(token_list):
    '''
    Function to remove stopwords. Stopwords list is used from NLTK package.
    Source: 
    https://github.com/kevin11h/YelpDatasetChallengeDataScienceAndMachineLearningUCSD/blob/master/Yelp%20Predictive%20Analytics.ipynb
    Input: string 
    Output: string
    '''    
#     token_list = nltk.word_tokenize(s)
#     exclude_stopwords = lambda token : token not in NLTK_STOPWORDS
    exclude_stopwords = lambda token : token not in STANFORD_STOPWORDS
    return ' '.join(filter(exclude_stopwords, token_list))

def stem_token_list(token_list):
    '''
    Function to stem words
    Input: list 
    Output: list 
    '''    
    STEMMER = PorterStemmer()
#     return [STEMMER.stem(tok.decode('utf-8')) for tok in token_list]
    return [STEMMER.stem(tok) for tok in token_list]

def restring_tokens(token_list):
    '''
    Function to convert the the tokenized words to string
    Input: list
    Output: string
    '''    
    return ' '.join(token_list)

def remove_stop_words_and_restring_and_lowercase_and_remove_punctuation_and_remove_numbers(token_list):
    '''
    Function to lowercase, remove punctuation, remove numbers, stem each token in a string
    Input: string
    Output: string
    '''    
    s = remove_stopwords(token_list)
    s = remove_numbers_in_string(s)
    s = lowercase_remove_punctuation(s)
#     return s
    token_list = nltk.word_tokenize(s)
#     #token_list = filter_out_more_stopwords(token_list)
    token_list = stem_token_list(token_list)
    return restring_tokens(token_list)


df_preprocessed = df.copy();
df_preprocessed['text'] = df['text'].apply(\
                            remove_stop_words_and_restring_and_lowercase_and_remove_punctuation_and_remove_numbers)

#READ TEST DATA
N =  int(raw_input())

ip_text = [None]  * N

for i in range(N):
    ip_text[i] = raw_input()
    
df_test = pd.DataFrame({'text' : ip_text})

#MACHINE LEARNING
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer

vectorizer_train = CountVectorizer(analyzer = "word",
                                 tokenizer = None,
                                 preprocessor = None,
                                 ngram_range = (1, 1),
                                 strip_accents = 'unicode',
                                 max_features = 100
                            )
feature_matrix_train = vectorizer_train.fit_transform(df_preprocessed.text)

vectorizer_test = CountVectorizer(analyzer = "word",
                                 tokenizer = None,
                                 preprocessor = None,
                                 ngram_range = (1, 1),
                                 strip_accents = 'unicode',
                                 max_features = 100,
                                 vocabulary = vectorizer_train.vocabulary_
                            )

feature_matrix_test = vectorizer_test.fit_transform(df_test.text)

def mySVC(feature_matrix_train, y_train, feature_matrix_test):
    '''
    Function to apply SVC from sklearn to build model on train data and get results on test data
    Input:
        feature_matrix_train: numpy.ndarray
        y_train: numpy.ndarray
        feature_matrix_test: numpy.ndarray
    Output:
        list: [train_accuracy, test_accuracy]
    '''
    clf = SVC()
    clf.fit(feature_matrix_train, y_train)  #.set_params(kernel='linear')

    clf_predictions = clf.predict(feature_matrix_test)
    
    for val in clf_predictions:
        print str(val)

y = np.array(df_preprocessed.response.copy(), dtype='int32')        
mySVC(feature_matrix_train, y, feature_matrix_test)