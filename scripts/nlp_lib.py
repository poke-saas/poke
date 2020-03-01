__jaccard_threshold__ = .25

def jaccard_similariy_index(first, second):
    """
    Returns the jaccard similarity between two strings
    :param first: first string we are comparing
    :param second: second string we are comparing
    :return: how similar the two strings are
    """

    # First, split the sentences into words
    tokenize_first = set(first.lower().split())
    tokenize_second = set(second.lower().split())

    # Then, find the ratio between their intersection and their total length
    intersection = tokenize_first.intersection(tokenize_second)
    return float(len(intersection)) / (len(tokenize_first) + len(tokenize_second) - len(intersection))