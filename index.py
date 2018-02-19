from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer


def load_data(spams, hams):
    f = open('test1.txt', 'r', encoding="utf8")
    for line in f:
        if line[0] == 's':
            spams.append(line[4:])
        else:
            hams.append(line[3:])


def main():
    spams = []
    hams = []
    load_data(spams, hams)
    spam_words = []
    ham_words = []
    tokenizer = RegexpTokenizer(r'\w+')

    for spam in spams:
        spam_words += tokenizer.tokenize(spam)

    for ham in hams:
        ham_words += tokenizer.tokenize(ham)

    print(len(spam_words))

    print(len(ham_words))

    all_text_length = len(spam_words) + len(ham_words)

    spam_probability = len(spam_words) / all_text_length

    ham_probability = len(ham_words) / all_text_length

    spam_map = {}

    spam_count = 0

    ham_map = {}

    ham_count = 0

    vocabulary = set().union(spam_words, ham_words)

    for word in vocabulary:

        if word not in spam_map:
            count = spam_words.count(word)
            spam_count += count
            spam_map[word] = count

        if word not in ham_map:
            count = ham_words.count(word)
            ham_count += count
            ham_map[word] = count

    spam_probabilities = {}

    vocabulary_length = len(vocabulary)

    for key, value in spam_map.items():
        spam_probabilities[key] = (value + 1) / (vocabulary_length + spam_count)

    ham_probabilities = {}

    for key, value in ham_map.items():
        ham_probabilities[key] = (value + 1) / (vocabulary_length + ham_count)

    test = "REMINDER FROM O2: To get 2.50 pounds free call credit and details of great offers pls reply 2 this text with your valid name, house no and postcode"
    test_words = tokenizer.tokenize(test)

    test_spam_probability = spam_probability*100
    test_ham_probability = ham_probability*100

    for word in test_words:
        if word in spam_probabilities:
            test_spam_probability *= spam_probabilities[word]
        else:
            test_spam_probability *= 1 / (vocabulary_length + spam_count)

        if word in ham_probabilities:
            test_ham_probability *= ham_probabilities[word]
        else:
            test_ham_probability *= 1 / (vocabulary_length + ham_count)

    print(len(spam_map))
    print(len(ham_map))
    print(test_spam_probability,test_ham_probability)

    if test_spam_probability > test_ham_probability:
        print("spam")
    else:
        print("ham")


main()
