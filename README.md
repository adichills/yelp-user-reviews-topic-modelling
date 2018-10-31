# Effect of Latent Topics in Online User Reviews and Tips on Restaurant Star Rating using Yelp Dataset

## Pre-processing

### Reviews

- Useful > 0
- Stop words removal
- Tokenization
- Stemming

### Approach

- Topic Modelling
- Per topic rating (using sentiment analysis)
- Supervised Learning to realize which topics are most imp
- Supervised Learning to predict the original review star rating
- (If metrics are nice) Use the per topic weights to **predict the most relevant tips** for a given restaurant