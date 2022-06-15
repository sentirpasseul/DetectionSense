

from processing import Preprocessing

class Text():

    def __init__(self, text):
        self.input_text = text


    def tokenize_text(self):
        self.get_tokens = Preprocessing(self.input_text).get_tokens()
        return self.get_tokens




