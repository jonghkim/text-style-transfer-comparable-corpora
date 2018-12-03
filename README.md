# text-style-transfer-comparable-corpora

Keras implementation of [Style Transfer in Text: Exploration and Evaluation (AAAI, 2018)](https://arxiv.org/abs/1711.06861)

# Requirements
- Python2
- Keras 2.1.6
- Tensorflow 1.5.0

# Data
- For adversarial style embedding model: Sentiment Review Dataset
    - toy_data is already included in the repository
    - get the original data at: http://jmcauley.ucsd.edu/data/amazon/links.html

# Usage
~~~
# For seq2seq auto-encoder model with adversarial network and style embedding: Solve Style Transfer Problem
python -m bin.seq2seq_adv_style_model_train
python -m bin.seq2seq_adv_style_model_test
~~~

# References
- [Style Transfer in Text: Exploration and Evaluation (AAAI, 2018)](https://arxiv.org/abs/1711.06861)
- [Theano Implementaion of "Style Transfer in Text: Exploration and Evaluation"](https://github.com/jonghkim/text-style-transfer-comparable-corpora)

# For Citation

@misc{jonghkim,
  author = {Jongho Kim},
  title = {text-style-transfer-comparable-corpora},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/jonghkim/financial-time-series-prediction-v1}},
}