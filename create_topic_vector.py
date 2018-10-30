import json
from collections import defaultdict
from gensim import corpora, models
import gensim
from gensim.test.utils import datapath

def get_business_id_stars(filename):
    business_id_stars = defaultdict(float)
    with open(filename,'r',encoding='utf8') as f:
        i = 0
        for line in f:
            i+=1
            if i % 10000 == 0:
                print(i)
            row = json.loads(line)
            business_id_stars[row['business_id']] = row['stars']

    return business_id_stars

def write_dict_to_file(filename,d):
    with open(filename,'w',encoding='utf8') as f:
        for key in d:
            f.write(json.dumps({key:d[key]}) + '\n')


def get_id_stemmed_text(filename, key):
    id_stemmed_text = defaultdict(list)
    all_texts = []
    with open(filename,'r') as f:
        i = 0
        for line in f:
            i+=1
            if i % 10000 == 0:
                print(i)
            row = json.loads(line)
            id = row[key]
            text = row['text'].split()
            id_stemmed_text[id].append(text)
            all_texts.append(text)

    return id_stemmed_text,all_texts




def convert_list_of_tuples_to_dict(list_of_tuples,no_of_topics):
    d = {x[0]:x[1] for x in list_of_tuples}
    for i in range(no_of_topics):
        if i not in d:
            d[i] = 0
    return d

def get_business_topic_vector(business_id,model,dictionary,business_topic_vector,business_id_stemmed_text,n):
    business_texts = business_id_stemmed_text[business_id]
    doc_term_texts = [dictionary.doc2bow(text) for text in business_texts]
    topic_vectors = [model[doc_term_text] for doc_term_text in doc_term_texts]
    topic_vectors = [convert_list_of_tuples_to_dict(x,50) for x in topic_vectors]
    topic_vector_for_business = [0 for x in range(n)]
    for i in range(n):

        topic_vector_for_business[i] = sum([x[i] for x in topic_vectors ])/len(topic_vectors)

    business_topic_vector[business_id] = topic_vector_for_business
    return business_topic_vector




#business_id_stars = get_business_id_stars('output/restaurants.json')

# Should work for both tips and restaurant files.
id_stemmed_text, all_texts = get_id_stemmed_text('output/stemmed_restaurant_tips.json', 'business_id')

print('###### Converting to dictionary ########')
dictionary = corpora.Dictionary(all_texts)

ldamodel = gensim.models.ldamodel.LdaModel
# for restaurant take the modle for yelp_reviews_50_topics.model
temp_file  = datapath('yelp_tips_50_topics.model')
print(temp_file)
model = ldamodel.load(temp_file)

def get_topic_vector_for_text(stemmed_text_list,model,dictionary):
    doc_term_text = dictionary.doc2bow(stemmed_text_list)
    topic_vector = model[doc_term_text]
    topic_vector = convert_list_of_tuples_to_dict(topic_vector,50)
    return topic_vector


def get_review_topic_vector(id_stemmed_text):
    review_topic_vector = defaultdict(list)
    i = 0
    for id in id_stemmed_text:
        i+=1
        if i % 10000 == 0:
            print(i)
        review_topic_vector[id] = get_topic_vector_for_text(id_stemmed_text[id],model,dictionary)

    return review_topic_vector



#business_topic_vector = defaultdict(list)
def get_business_topc_vector(id_stemmed_text):
    business_topic_vector = defaultdict(list)
    i = 0
    for business_id in id_stemmed_text.keys():
        i+=1
        if i % 10000 == 0:
            print(i)
        business_topic_vector = get_business_topic_vector(business_id, model, dictionary,
                                                          business_topic_vector, id_stemmed_text, 50)

    return business_topic_vector

business_topic_vector = get_business_topc_vector(id_stemmed_text)
#review_topic_vector = get_review_topic_vector(id_stemmed_text)

write_dict_to_file('output/business_tips_topic_vector.json',business_topic_vector)




