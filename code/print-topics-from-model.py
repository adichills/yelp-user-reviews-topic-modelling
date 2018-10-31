
import gensim

def print_topics(model_path):
    lda = gensim.models.ldamodel.LdaModel.load(model_path)
    for topic in lda.print_topics(50):
        print(topic)


if __name__ == '__main__':
    MODEL_PATH = "/Users/sahilgandhi/Datasets/6120-project/model_50_topic_restaurant/yelp_reviews_50_topics.model"
    print_topics(MODEL_PATH)
