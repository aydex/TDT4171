class Node:
    def __init__(self, attribute):
        self.attribute = attribute
        self.rightChild = None
        self.leftChild = None

def plurality_value(examples):
    # TODO
    pass


def importance(attributes, examples):
    # TODO
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
        A = max(importance(attributes, examples))  # Needs amendment
        tree = Node(A)
        exs0 =
        exs1 =
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
