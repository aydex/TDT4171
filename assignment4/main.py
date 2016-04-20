import math
import random

class Node():

    def __init__(self):
        pass


def plurality_value(examples):
    n = 0
    p = 0

    for e in examples:
        if e[-1]:
            p += 1
        else:
            n += 1
    if n == p:
        return random.choice([0, 1])
    return 1 if (p>n) else 0
    pass


def b(q):
    return -(q*math.log(q, 2)+(1-q)*math.log((1-q), 2))


def remainder(a, p, n, examples):
    p0 = 0
    p1 = 0
    n0 = 0
    n1 = 0
    for e in examples:
        if e[a]:
            if e[-1]:
                p1 += 1
            else:
                p0 += 1
        else:
            if e[-1]:
                n1 += 1
            else:
                n0 += 1
    return (((p0 + n0)/(p + n))*b(p0/(p0+n0)))+(((p1 + n1)/(p+n))*b(p1/(p1+n1)))


def importance(a, examples):
    p = 0
    n = 0
    for example in examples:
        if example[-1]:
            p += 1
        else:
            n += 1
    return b(p/(p+n)) - remainder(a, p, n, examples)
    pass


def decision_tree_learning(examples, attributes, parent_examples):
    if len(examples) is 0:
        return plurality_value(parent_examples)
    elif examples:  # Needs amendment
        return examples
    elif len(attributes) is 0:
        return plurality_value(examples)
    else:
        attribute_gains = [importance(x, examples) for x in attributes]
        A = attributes[attribute_gains.index(max(attribute_gains))]
        A_random = random.choice(attributes)
        tree = A  # Needs amendment
        for v in A:  # Needs amendment
            exs = v  # Needs amendment
            subtree = decision_tree_learning(exs, attributes - A, examples)
            # Need to add a branch to tree with label (A = vk) and subtree "subtree" somewhere"
        return True


def main():
    random.seed()
    pass


main()
