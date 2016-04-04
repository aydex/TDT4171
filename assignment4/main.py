def plurality_value(examples):
    # TODO
    pass


def importance(attributes, examples):
    # TODO
    pass


def decision_tree_learning(examples, attributes, parent_examples):
    if len(examples) is 0:
        return plurality_value(parent_examples)
    elif examples:  # Needs amendment
        return examples
    elif len(attributes) is 0:
        return plurality_value(examples)
    else:
        A = max(importance(attributes, examples))  # Needs amendment
        tree = A  # Needs amendment
        for v in A:  # Needs amendment
            exs = v  # Needs amendment
            subtree = decision_tree_learning(exs, attributes - A, examples)
            # Need to add a branch to tree with label (A = vk) and subtree "subtree" somewhere"
        return True


def main():
    pass


main()
