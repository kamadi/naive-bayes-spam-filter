from nltk.tokenize import RegexpTokenizer

from classifier import NaiveBayes
from util import load_data

tokenizer = RegexpTokenizer(r'\w+')

spams = []
hams = []
load_data(hams, spams, 'res/SMSSpamCollection.txt')
spam_words = []
ham_words = []

for spam in spams:
    spam_words += tokenizer.tokenize(spam)

for ham in hams:
    ham_words += tokenizer.tokenize(ham)

naive_bayes = NaiveBayes()

naive_bayes.load(ham_words, spam_words)

message = ""

while message != "stop":
    message = input("Enter your SMS:")
    if naive_bayes.is_positive(tokenizer.tokenize(message)):
        print("ham")
    else:
        print("spam")
