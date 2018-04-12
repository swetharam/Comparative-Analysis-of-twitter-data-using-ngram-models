import nltk
from nltk.util import ngrams

def word_grams(words, min=1, max=4):
    print(words)
    s=[]
    s1=[]
    s2=[]
    s3=[]
    for n in range(min, max):
        if n == 1:
            for ngram in ngrams(words, n):
                s1.append(' '.join(str(i) for i in ngram))
        if n==2:
            for ngram in ngrams(words, n):
                s2.append(' '.join(str(i) for i in ngram))
        else:
            for ngram in ngrams(words, n):
                s3.append(' '.join(str(i) for i in ngram))
    s.append(s1)
    s.append(s2)
    s.append(s3)
    return s

print (word_grams('one two three four'.split(' ')))
# uni_test_sent={}
# i=0
# for sent in editedtest:
#     temp=1
#     for word in sent:
#         # print(word)
#         if word in unigram_prob:
#             temp = temp* unigram_prob[word]
#         else:
#             continue
#     i+=1
#     uni_test_sent[i]=temp
# print(uni_test_sent)
# for nos in bigrams1count_test:
#     temp = 1
#     k = 0
#     for val in nos:
#         temp=(temp*int(val))/test_count[i]
#     i+=1
#     bigramprob.append(temp)
# print(bigramprob)