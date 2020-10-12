class PreProcessing(object):
    def __init__(self):
        self._steps = []
        
    def append(self, preproc, kwargs=None):
        self._steps.append([preproc, kwargs])
        
    def execute(self, text):
        for pair in self._steps:
            methodx = pair[0]
            kwargs = pair[1]
            
            if kwargs is None:
                text = methodx(text)
            else:
                text = methodx(text, **kwargs)
        return text
    
    def pop(self):
        self._steps.pop()
        
        
import re
import nltk
import pandas as pd

############################################
# PreProcessing methods
############################################

def to_lower(x):
    return x.lower()

def to_upper(x):
    return x.to_upper()

def unlist(x):
    return sum(x, [])

def remove_special_char(x, replacement=' '):
    return re.sub('[^a-zA-Z0-9]', replacement, x)

def remove_punctuation(x, punctuation):
    for p in punctuation:
        x = x.replace(p, ' ')
    return x

def remove_double_blank(x):
    return re.sub(' +', ' ', x)

def remove_single_digit(x, tokenizer):
    return ' '.join(['' if y.isdigit() else y for y in tokenizer(x)])

def remove_by_regex(x, regex, ignore_keywords, tokenizer):
    
    if tokenizer is None:
        return re.sub
    
    return ' '.join(['' 
                     if (len(re.findall(regex, y)) > 0 and y not in ignore_keywords)
                     else y 
                     for y in tokenizer(x)
                    ])

def apply_stemming(x, tokenizer, stemmer):
    return ' '.join([stemmer.lemmatize(y) for y in tokenizer(x)])

def remove_stopwords(x, stopwords):
    x = nltk.word_tokenize(x)
    x = [i for i in x if i not in stopwords]
    return ' '.join(x)

def replace_texts(x, replacements):
    for i, j in replacements.items():
        x = re.sub(i,j,x)
    return x

def remove_comma(x):
    return x.replace(',','')

def remove_dot(x):
    return x.replace('.','')