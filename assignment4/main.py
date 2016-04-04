def plurality_value(examples):
    pass


def importance(attributes, examples):
    pass


def decision_tree_learning(examples, attributes, parent_examples):
    if len(examples) is 0:
        return plurality_value(parent_examples)
    elif examples:
        return examples
    elif len(attributes) is 0:
        return plurality_value(examples)
    else:
        A = max(importance(attributes, examples))
        tree = A
        for v in A:
            exs = v
            subtree = decision_tree_learning(exs, attributes-A, examples)
        return True

def main():
    pass

main()
