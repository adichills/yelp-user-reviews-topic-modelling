# Effect of Latent Topics in Online User Reviews and Tips on Restaurant Star Rating using Yelp Dataset

## Pre-processing

### Reviews

- Useful > 0
- Stop words removal
- Tokenization
- Stemming

### Approach

![alt text](https://github.com/adichills/yelp-user-reviews-topic-modelling/blob/master/figures/Approach.PNG)


### How to run the notebooks

The notebooks in the notebook basically implement the above pipeline diagram post the data processing layer. The inputs to the notebooks can be found [here](https://drive.google.com/drive/folders/1MZ5BT_GJVqFHdUMY9Bdvb2uu9ipx7_I9?usp=sharing).
Please replace the data paths in the first cell with the above data downloaded in your machine.

- This notebook Topic_modeling_analysis_nmf_az.ipynb runs the nmf topic modelling algorithm for the state of AZ
- This notebook Topic_modeling_analysis_v4.ipynb runs the lda topic modelling algorithm for state of NV
- To run the graphs use the graph_generator.ipynb notebook and replace the input data for the graph's path with the ones in the experiment folder.



### All the runs were done on a massive ec2-instance m5.2xlarge and takes about 6 hrs for each run with all the iterations and topic variations

### Required Python software
- gensim
- nltk
- seaborn
- matplotlib
- scikit
- scipy
- numpy
