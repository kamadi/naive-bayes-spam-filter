from nltk.tokenize import RegexpTokenizer

from classifier import NaiveBayes
from util import load_data, get_data, divide_data


def test1():
    tokenizer = RegexpTokenizer(r'\w+')
    spams = []
    hams = []
    load_data(hams, spams, 'test1.txt')
    spam_words = []
    ham_words = []

    for spam in spams:
        spam_words += tokenizer.tokenize(spam)

    for ham in hams:
        ham_words += tokenizer.tokenize(ham)

    naive_bayes = NaiveBayes()

    naive_bayes.load(ham_words, spam_words)

    test_spams = []
    test_hams = []

    load_data(test_hams, test_spams, 'test1_check.txt')

    spam_correct = 0
    spam_incorrect = 0

    for word in test_spams:
        result = naive_bayes.is_positive(tokenizer.tokenize(word))
        if result:
            spam_incorrect += 1
        else:
            spam_correct += 1

    print('spam:', 'correct', spam_correct, 'incorrect', spam_incorrect)
    print('spam:', (spam_correct / (spam_incorrect + spam_correct)) * 100, '%')

    ham_correct = 0
    ham_incorrect = 0

    for word in test_hams:
        result = naive_bayes.is_positive(tokenizer.tokenize(word))
        if result:
            ham_correct += 1
        else:
            ham_incorrect += 1

    print('ham:', 'correct', ham_correct, 'incorrect', ham_incorrect)
    print('ham:', (ham_correct / (ham_incorrect + ham_correct)) * 100, '%')


def test2(is_from_begginning=True, training_percent=70):
    tokenizer = RegexpTokenizer(r'\w+')

    data = get_data('SMSSpamCollection.txt')

    training_data_length = int((len(data) * training_percent) / 100)

    if is_from_begginning:
        training_data = data[:training_data_length]

        test_data_length = len(data) - training_data_length

        test_data = data[-test_data_length:]
    else:
        training_data = data[-training_data_length:]

        test_data_length = len(data) - training_data_length

        test_data = data[test_data_length:]

    training_hams = []
    training_spams = []

    divide_data(training_data, training_hams, training_spams)

    training_spam_words = []
    training_ham_words = []

    for ham in training_hams:
        training_ham_words += tokenizer.tokenize(ham)

    for spam in training_spams:
        training_spam_words += tokenizer.tokenize(spam)

    naive_bayes = NaiveBayes()

    naive_bayes.load(training_ham_words, training_spam_words)

    test_hams = []
    test_spams = []

    divide_data(test_data, test_hams, test_spams)

    spam_correct = 0
    spam_incorrect = 0

    for word in test_spams:
        result = naive_bayes.is_positive(tokenizer.tokenize(word))
        if result:
            spam_incorrect += 1
        else:
            spam_correct += 1

    print('spam:', 'correct', spam_correct, 'incorrect', spam_incorrect)
    print('spam:', (spam_correct / (spam_incorrect + spam_correct)) * 100, '%')

    ham_correct = 0
    ham_incorrect = 0

    for word in test_hams:
        result = naive_bayes.is_positive(tokenizer.tokenize(word))
        if result:
            ham_correct += 1
        else:
            ham_incorrect += 1

    print('ham:', 'correct', ham_correct, 'incorrect', ham_incorrect)
    print('ham:', (ham_correct / (ham_incorrect + ham_correct)) * 100, '%')


print('')
print("test1 started")
print('---------------')
test1()


print('')
print("test2 started")
print("Training data are 60% from beginning")
print('---------------')
test2(True, 60)

print('')
print("test3 started")
print("Training data are 60% from end")
print('---------------')
test2(False, 60)

print('')
print("test4 started")
print("Training data are 70% from beginning")
print('---------------')
test2(True, 70)

print('')
print("test5 started")
print("Training data are 70% from end")
print('---------------')
test2(False, 70)

print('')
print("test6 started")
print("Training data are 80% from beginning")
print('---------------')
test2(True, 80)

print('')
print("test7 started")
print("Training data are 80% from end")
print('---------------')
test2(False, 80)

print('')
print("test8 started")
print("Training data are 90% from beginning")
print('---------------')
test2(True, 90)

print('')
print("test9 started")
print("Training data are 90% from end")
print('---------------')
test2(False, 90)
