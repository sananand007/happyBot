'''
happyBot
'''
import spacy
class main(object):
    """docstring for main."""
    def __init__(self):
        super(main, self).__init__()
        self.sentence = input("Enter your sentence and I will respond ! \n")

    def manipulate(self):
        nlp = spacy.load('en')
        doc = nlp(self.sentence)
        for token in doc:
            print(token)

obj = main()
obj.manipulate()
