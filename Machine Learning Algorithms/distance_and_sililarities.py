# Distance And Similarities
# Write a series of functions that take in two lists, X = x_1 ... ×_n and Y = y_1 ... _n and return a list
# containing
# • Firstly, the Euclidean distance between X and Y.
# • Secondly, the Manhattan distance between X and Y.
# • Thirdly, the Cosine similarity of X and Y.
# • Finally, the Jaccard similarity of X and Y.
# Note that:
# • You shouldn't use any libraries.
# • Your output values will automatically be rounded to the fourth decimal.
# • X and Y will consist of positive integers up to 1000.
# • X and Y will have cardinalities between 1 and 10 inclusive.

# Sol

from math import sqrt


class Metrics():
    def euclidean_distance(self, X, Y):
        # Write your code here.
        return sqrt(sum(((x - y) ** 2) for x, y in zip(X, Y)))

    def manhattan_distance(self, X, Y):
        # Write your code here.
        return sum(abs(x - y) for x, y in zip(X, Y))

    def cosine_similarity(self, X, Y):
        # Write your code here.
        numerator = sum((x * y) for x, y in zip(X, Y))
        denominator = sqrt(sum([x * x for x in X])) * \
            sqrt(sum([y * y for y in Y]))
        return numerator / float(denominator)

    def jaccard_similarity(self, X, Y):
        # Write your code here.
        intersecation_cardinality = len(set.intersection(*[set(X), set(Y)]))
        union_cardinality = len(set.union(*[set(X), set(Y)]))
        # or we can return:
        # return len(set(x).intersection(set(y))) / len(set(x).union(set(y)))
        return intersecation_cardinality / float(union_cardinality)


def distances_and_similarities(X, Y):
    metrics = Metrics()
    return [metrics.euclidean_distance(X, Y),
            metrics.manhattan_distance(X, Y),
            metrics.cosine_similarity(X, Y),
            metrics.jaccard_similarity(X, Y)]
