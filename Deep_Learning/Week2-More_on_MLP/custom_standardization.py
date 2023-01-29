# Custom standardization function for the TextVectorizer Layer 



import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras import layers
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import plot_model 

import nltk
import numpy 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))

import re
import string



def custom_standardization(input_string):
    """ Remove html line-break tags and handle punctuation """

    no_uppercased = tf.strings.lower(input_string, encoding='utf-8')
    no_html = tf.strings.regex_replace(no_uppercased, "<br />", "")
    no_digits = tf.strings.regex_replace(no_html, "\w*\d\w*","")
    no_punctuations = tf.strings.regex_replace(no_digits, f"([{string.punctuation}])", r" ")
    no_emojis = tf.strings.regex_replace(no_punctuations, "[^\x00-\x7F]+", "")

    #remove stop words
    no_stop_words = ' '+no_emojis+ ' '
    for each in stop_words:
      no_stop_words = tf.strings.regex_replace(no_stop_words, ' '+each[0]+' ' , r" ")
    no_extra_space = tf.strings.regex_replace(no_stop_words, " +"," ")

    return no_extra_space


input_string = "I love it!!! I absolutely love it!! 👌👍"
print("input:  ", input_string)
output_string= custom_standardization(input_string)
print("output: ", output_string.numpy().decode("utf-8"))