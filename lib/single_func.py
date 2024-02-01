def make_snippet(initial_sentence):
    words = initial_sentence.split()
    first_five_words = words[:5]

    if len(first_five_words) >= 5:
        new_sentence = ' '.join(first_five_words) + ' ...'
        return new_sentence

    return 'Sentence too short'


def count_words(string):
    words = string.split()
    return len(words)