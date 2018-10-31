import json

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = set(get_stop_words('en'))


# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

def process_review_text(text):
    raw = text.lower()
    tokens = tokenizer.tokenize(raw)
    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]

    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    return ' '.join(stemmed_tokens)

def get_processed_user_reviews(filename):
    processed_user_reviews = []
    with open(filename,'r',encoding='utf8') as f:
        i = 0
        for line in f:
            i+=1
            if i % 10000 == 0:
                print(i)
            review = json.loads(line)
            review['text'] = process_review_text(review['text'])
            processed_user_reviews.append(review)


    return processed_user_reviews


def writeListToFile(filename,l):
    with open(filename,'w',encoding='utf8') as f:
        for row in l:
            line = json.dumps(row)
            f.write(line + '\n')

processed_user_reviews = get_processed_user_reviews('input/yelp_academic_dataset_tip.json')
writeListToFile('output/stemmed_user_tips.json',processed_user_reviews)

def get_restaurants_ids(filename):
    restaurant_ids = set()
    with open(filename,'r',encoding='utf8') as f:
        i = 0
        i+=1
        if i % 10000 == 0:
            print(i)
        for line in f:
            business = json.loads(line)
            restaurant_ids.add(business['business_id'])

    return restaurant_ids


def filter_stemmed_user_reviews(filename,restaurant_ids):
    filtered_user_reviews = []
    with open(filename,'r',encoding='utf8') as f:
        i = 0
        for line in f:
            i+=1
            if i % 10000 == 0:
                print(i)

            review = json.loads(line)
            if review['business_id'] in restaurant_ids:
                filtered_user_reviews.append(review)

    return filtered_user_reviews

restaurant_ids = get_restaurants_ids('output/restaurants.json')
# takes either stemmed_user_tips or stemmed_user_reviews.json , should work for both
filtered_user_reviews = filter_stemmed_user_reviews('output/stemmed_user_tips.json',restaurant_ids)
print(len(filtered_user_reviews))
writeListToFile('output/stemmed_restaurant_tips.json',filtered_user_reviews)



