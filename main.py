import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
import sklearn
from collections import Counter
from itertools import combinations


url = 'https://www.dominos.com/en?utm_campaign=52477568%7Cc%7CBG%7CBing_NB_Pizza_Generic&utm_source=Bing&utm_medium=p_search&utm_content=kwd-73598965867833:loc-190%7C52477568%7C4745841861&utm_term=pizza&matchtype=be&msclkid=b8a95eb35a0916d83d02372b9fadcae1'


r = requests.get(url)


text = r.text 




soup = BeautifulSoup(text, 'html.parser')

paragraphs = soup.find_all("p") 


all_text = []

for p in paragraphs:

    text = p.get_text().replace(u'\xa0', u' ')

    clean = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    
    all_text.append(clean)


    
    


all_list = list(dict.fromkeys(all_text))


corpus =" ".join(all_list)


array = np.array([corpus])



corpus = list(corpus)

def pairs(corpus)
    pairs = [(corpus[i], corpus[i + 1]) for i in range(len(corpus) - 1)]

    pair_counts = Counter(pairs)
    most_common_pair = pair_counts.most_common(1)[0]
    return most_common_pair



def merge(corpus,pair):
    new_corpus = []
    i=0
    while i<len(corpus):
        
        if i < len(corpus) -1 and corpus[i] == pair[0] and corpus[i + 1] == pair[1]:   
            new_corpus.append(pair[0]+pair[1])
            i+=2 
 
          
        else:
            new_corpus.append(corpus[i])
            
            i+=1
    return new_corpus 

merged = merge(corpus,most_common_pair[0])

target = 100
vocab_size = 0 
while vocab_size < target:
    pair = pairs(corpus)
    merge(new_corpus,pair)
 



