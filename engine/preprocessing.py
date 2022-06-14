import nltk
import textblob


class Preprocessing():

    def __init__(self, text):
        self.text = text


    def get_tokens(self):
        tokens = nltk.word_tokenize(self.text)
