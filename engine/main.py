from engine.text import Text
from engine.preprocessing import Preprocessing


def main():
    input_text = input("Введите текст: ")
    tokens = Preprocessing(input_text).get_tokens()
    print(tokens)

    #morph_analyzer = Preprocessing(i)


if __name__ == '__main__':
    main()

