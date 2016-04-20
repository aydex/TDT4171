import random
import math


class Node:
    def __init__(self, attribute):
        self.attribute = attribute
        self.rightChild = None
        self.leftChild = None

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

def all_same_class(examples):
    value = examples[0][-1]
    for example in examples:
        if(example[-1] != value):
            return False
    return True

def decision_tree_learning(examples, attributes, parent_examples):
    if len(examples) is 0:
        return plurality_value(parent_examples)
    elif all_same_class(examples):
        return all_same_class(examples)
    elif len(attributes) is 0:
        return plurality_value(examples)
    else:
        attribute_gains = [importance(x, examples) for x in attributes]
        A = attributes[attribute_gains.index(max(attribute_gains))]
        A_random = random.choice(attributes)
        tree = Node(A)
        exs0 = None
        exs1 = None
        subtree0 = decision_tree_learning()
        subtree1 = decision_tree_learning()
        tree.rightChild = subtree1
        tree.leftChild = subtree0
        for v in A:  # Needs amendment
            exs = v  # Needs amendment
            subtree = decision_tree_learning(exs, attributes - A, examples)
            # Need to add a branch to tree with label (A = vk) and subtree "subtree" somewhere"
        return tree

def train(examples, attributes):
    tree = decision_tree_learning(examples, attributes, [])
    return tree

def test(tree, examples):
    for example in examples:
        subTree = tree
        while(isinstance(subTree, Node)):
            if example[subTree.attribute]:
                subTree = subTree.rightChild
            else:
                subTree = subTree.leftChild
        if(example[-1] == subTree):
            pass
    return 0

def main():
    random.seed()
    trainingFile = open("data/training.txt","r")
    testFile = open("data/test.txt", "r")
    trainingExamples = []
    testExamples = []
    for line in trainingFile:
        trainingExamples.append(line.split())
    for line in testFile:
        testExamples.append(line.split())
    for i in xrange(0, len(trainingExamples)):
        for j in xrange(0, len(trainingExamples[0])):
            if trainingExamples[i][j] == '1':
                trainingExamples[i][j] = 1
            else:
                trainingExamples[i][j] = 0
    for i in xrange(0, len(testExamples)):
        for j in xrange(0, len(testExamples[0])):
            if testExamples[i][j] == '1':
                testExamples[i][j] = 1
            else:
                testExamples[i][j] = 0
    attributes = [x for x in range(0, len(trainingExamples[0])-1)]
    trainingFile.close()
    testFile.close()
    tree = train(trainingExamples, attributes)
    accuracy = test(tree, testExamples)
    print accuracy


main()
