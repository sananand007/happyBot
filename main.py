'''
happyBot
'''
import spacy
# Sentences we'll respond with if the user greeted us

#######
# Considering a small subset and then go ahead with a proper database
#######
GREETING_KEYWORDS = ["hello", "hi", "greetings", "sup",
                    "what's up","Hey", "Hey There", "Good Morning",
                    "Good Afternoon", "Good Evening",
                    "What’s new?", "What’s going on?",
                    "How’s everything ?", "How are things?", "How’s life?",
                    "Hi There!"]

GREETING_RESPONSES = ["'sup bro", "hey", "Hi There", "hey you get my snap?",
                        "There is a magic in the air", "No Comment",
                        "How you doing", "Never Mind", "Close call",
                        "There you are!"]

# Do some Postprocessing
# Remove the punctuations and get the string into a lower case and get the numbers out
import string
import re
import random

def convert(s):
    s=s.translate(str.maketrans('','',string.punctuation))
    s=s.lower()
    s=re.sub(r'(\d+)','',s, flags=re.I)
    s=re.sub(r'[^a-z]',"",s,flags=re.I)
    return s


class main(object):
    """docstring for main."""
    def __init__(self):
        super(main, self).__init__()
        self.sentence = input("Enter your greeting and I will respond ! \n")
        self.greeting_keys = []
        for word in GREETING_KEYWORDS:
            self.greeting_keys.append(convert(word))

    def manipulate(self):
        nlp = spacy.load('en')
        doc = nlp(self.sentence)
        for token in doc:
            print(token)

    def greeting(self):
        if convert(self.sentence) in self.greeting_keys:
            return print(random.choice(GREETING_RESPONSES))

obj = main()
obj.greeting()
