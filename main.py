import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
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



#turn every paragraph line into a list of unique character values
all_list = list(dict.fromkeys(all_text))



#join them all into one list
corpus =" ".join(all_list)

#turn them into a  numpy array
array = np.array([corpus])



#turn the characters into a list of chatacters
corpus = list(corpus)

#fine the most common pair in the list of characters
def most_pairs(corpus):
    #takes the corpus i and corpus i+1 for every item in coprus, creating pairs
    pairs = [(corpus[i], corpus[i + 1]) for i in range(len(corpus) - 1)]
    #count the number of pairs
    pair_counts = Counter(pairs)
    #find the most common pair
    most_common_pair = pair_counts.most_common(1)[0]
    #return the most common pair
    return most_common_pair


def merge(corpus,pair):
    #create a new list of corpus
    new_corpus = []
    #start the index at 0
    i=0
    #while loop across the entire list
    while i<len(corpus):
        #if statement to find  where the most common pair is

        if i < len(corpus) -1 and corpus[i] == pair[0][0] and corpus[i + 1] == pair[0][1]:

	    #where the pair is found, we replace the pair with a tightended version of it
            new_corpus.append(pair[0][0]+pair[0][1])
            #we run i +=2 since were pairing two elements
            i+=2
        else:
	    #for all other cases, we just append the normal corpus
            new_corpus.append(corpus[i])
            i+=1

    corpus = new_corpus
    return corpus



target = 150
vocab_size = 0
while vocab_size < target:
    most = most_pairs(corpus)
    print(most)
    corpus = merge(corpus,most)
    print(corpus)
    vocab_size += 1

print(corpus)
