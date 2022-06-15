from engine.text import Text
from engine.processing import Preprocessing

class Main():

    def __init__(self):
        self.input_text = input("Введите текст: ")
        self.preproc = Preprocessing(self.input_text)

    def main(self):


        tokens = self.preproc.get_tokens()
        print("Токенизация: ",tokens)

        morph_analyzer = self.preproc.morph_analyzer()
        print("Морфологический анализ: ",morph_analyzer)


if __name__ == '__main__':
    Main().main()

