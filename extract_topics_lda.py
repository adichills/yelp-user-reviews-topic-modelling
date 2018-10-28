from gensim import corpora, models
import gensim
from gensim.test.utils import datapath
import json
import time

def get_texts_from_file(filename):
    texts = []
    with open(filename,'r',encoding='utf8') as f:
        i = 0
        for line in f:
            i+=1
            if i % 10000 == 0:
                print(i)
            row = json.loads(line)
            texts.append(row['text'].split(' '))

    return texts

def extract_topics_lda(texts,model_path,no_topics,passes):

    print('###### Converting to dictionary ########')
    dictionary = corpora.Dictionary(texts)

    print('###### Converting to document-term matrix ########')
    #convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]



    print('#######Training########')
    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus,num_topics=no_topics,chunksize=10000,
                                               id2word=dictionary, passes=passes)
    #ldamodel = gensim.models.ldamodel.LdaModel
    temp_file  = datapath(model_path)
    ldamodel.save(temp_file)
    topics = ldamodel.print_topics(50)
    return topics

texts = get_texts_from_file('output/stemmed_restaurant_reviews.json')
start_time = time.time()
topics = extract_topics_lda(texts,'yelp_reviews_50_topics.model',50,1)
print("--- %s seconds ---" % (time.time() - start_time))
for topic in topics:
    print(topic)


