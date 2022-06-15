import nltk
import textblob
from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()


class Preprocessing():

    def __init__(self, text = str()):
        self.text = text
        self.sentences = self.text.split(".")


    def get_tokens(self):
        self.tokens = nltk.word_tokenize(self.text)
        return self.tokens

    def morph_analyzer(self):
        #for word in self.tokens:
        return self.sentences

