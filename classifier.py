class NaiveBayes:

    negative_map = {}

    positive_map = {}

    positive_count = 0

    negative_probability = 0

    positive_probability = 0

    vocabulary = []

    vocabulary_length = 0

    negative_probabilities = {}

    positive_probabilities = {}

    def __init__(self):

        self.negative_map = {}

        self.negative_count = 0

        self.positive_map = {}

        self.positive_count = 0

        self.negative_probability = 0

        self.positive_probability = 0

        self.vocabulary = []

        self.vocabulary_length = 0

        self.negative_probabilities = {}

        self.positive_probabilities = {}

    def load(self, positive_words, negative_words):

        print("loading data...")

        all_text_length = len(negative_words) + len(positive_words)

        self.negative_probability = len(negative_words) / all_text_length

        self.positive_probability = len(positive_words) / all_text_length

        self.vocabulary = set().union(negative_words, positive_words)

        print("mapping data...")

        for word in self.vocabulary:
            count = negative_words.count(word)
            self.negative_count += count
            self.negative_map[word] = count

            count = positive_words.count(word)
            self.positive_count += count
            self.positive_map[word] = count

        self.vocabulary_length = len(self.vocabulary)

        print("counting probabilities...")

        for key, value in self.negative_map.items():
            self.negative_probabilities[key] = (value + 1) / (self.vocabulary_length + self.negative_count)

        for key, value in self.positive_map.items():
            self.positive_probabilities[key] = (value + 1) / (self.vocabulary_length + self.positive_count)

    def is_positive(self, test_words):

        test_negative_probability = self.negative_probability
        test_positive_probability = self.positive_probability

        for word in test_words:
            if word in self.negative_probabilities:
                test_negative_probability *= self.negative_probabilities[word]
            else:
                test_negative_probability *= 1 / (self.vocabulary_length + self.negative_count)

            if word in self.positive_probabilities:
                test_positive_probability *= self.positive_probabilities[word]
            else:
                test_positive_probability *= 1 / (self.vocabulary_length + self.positive_count)

        return test_positive_probability > test_negative_probability
