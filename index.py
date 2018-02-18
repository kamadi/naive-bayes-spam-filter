from nltk import word_tokenize

def load_data(spams, hams):
    f = open('SMSSpamCollection.txt', 'r')
    for line in f:
        if line[0] == 's':
            spams.append(line)
        else:
            hams.append(line)


def main():
    spams = []
    hams = []
    load_data(spams, hams)
    spam_words = []
    ham_words = []
    for spam in spams:
        spam_words += word_tokenize(spam)

    for ham in hams:
        ham_words += word_tokenize(ham)

    # spam_words = set(spam_words)

    print(len(spam_words))
    print(len(ham_words))

    spam_words = set(spam_words)
    ham_words = set(ham_words)

    print(len(spam_words))
    print(len(ham_words))

    spam_map = {}
    
    for word in spam_words:
        spam_map[word] = True

    ham_map = {}
    for word in ham_words:
        ham_map[word] = True

    print(len(spam_map))
    print(len(ham_map))



main()
