__author__ = 'kaiolae'
import Backprop_skeleton as Bp
import matplotlib.pyplot as plt

results = []

# Class for holding your data - one object for each line in the dataset
class DataInstance:
    def __init__(self, qid, rating, features):
        self.qid = qid  # ID of the query
        self.rating = rating  # Rating of this site for this query
        self.features = features  # The features of this query-site pair.

    def __str__(self):
        return "Datainstance - qid: " + str(self.qid) + ". rating: " + str(self.rating) + ". features: " + str(
            self.features)


# A class that holds all the data in one of our sets (the training set or the testset)
class DataHolder:
    def __init__(self, dataset):
        self.dataset = self.load_data(dataset)

    @staticmethod
    def load_data(file):
        # Input: A file with the data.
        # Output: A dict mapping each query ID to the relevant documents, like this:
        # dataset[queryID] = [dataInstance1, dataInstance2, ...]
        data = open(file)
        dataset = {}
        for line in data:
            # Extracting all the useful info from the line of data
            line_data = line.split()
            rating = int(line_data[0])
            qid = int(line_data[1].split(':')[1])
            features = []
            for elem in line_data[2:]:
                if '#docid' in elem:  # We reached a comment. Line done.
                    break
                features.append(float(elem.split(':')[1]))
            # Creating a new data instance, inserting in the dict.
            di = DataInstance(qid, rating, features)
            if qid in dataset.keys():
                dataset[qid].append(di)
            else:
                dataset[qid] = [di]
        return dataset


def run_ranker(trainingset, testset):
    # Insert the code for training and testing your ranker here.
    # Dataholders for training and testset
    dh_training = DataHolder(trainingset)
    dh_testing = DataHolder(testset)

    # Creating an ANN instance - feel free to experiment with the learning rate (the third parameter).
    nn = Bp.NN(46, 10, 0.001)

    # The lists below should hold training patterns in this format:
    # [(data1Features,data2Features), (data1Features,data3Features), ... , (dataNFeatures,dataMFeatures)]
    # The training set needs to have pairs ordered so the first item of the pair has a higher rating.
    training_patterns = []  # For holding all the training patterns we will feed the network
    test_patterns = []  # For holding all the test patterns we will feed the network
    for qid in dh_training.dataset.keys():
        # This iterates through every query ID in our training set
        data_instance = dh_training.dataset[qid]  # All data instances (query, features, rating) for query qid
        # Store the training instances into the trainingPatterns array.
        # Remember to store them as pairs, where the first item is rated higher than the second.
        # Hint: A good first step to get the pair ordering right,
        # is to sort the instances based on their rating for this query. (sort by x.rating for each x in dataInstance)
        data_instance.sort(key=lambda d: d.rating, reverse=True)
        for i in xrange(len(data_instance)):
            for j in xrange(i + 1, len(data_instance)):
                if not (data_instance[i].rating == data_instance[j].rating):
                    training_patterns.append([data_instance[i].features, data_instance[j].features])
    print len(training_patterns)

    for qid in dh_testing.dataset.keys():
        # This iterates through every query ID in our test set
        data_instance = dh_testing.dataset[qid]
        # Store the test instances into the testPatterns array, once again as pairs.
        # Hint: The testing will be easier for you if you also now order the pairs - it will make it easy to see if
        # the ANN agrees with your ordering.
        data_instance.sort(key=lambda d: d.rating, reverse=True)
        for i in xrange(len(data_instance)):
            for j in xrange(i + 1, len(data_instance)):
                if not (data_instance[i].rating == data_instance[j].rating):
                    test_patterns.append([data_instance[i].features, data_instance[j].features])

    test_error = []
    training_error = []
    run = [x for x in xrange(26)]
    # Check ANN performance before training
    test_error.append(nn.countMisorderedPairs(test_patterns))
    training_error.append(nn.countMisorderedPairs(training_patterns))
    for i in range(20):
        print i
        # Running 25 iterations, measuring testing performance after each round of training.
        # Training
        training_error.append(nn.train(training_patterns, iterations=1))
        # Check ANN performance after training.
        test_error.append(nn.countMisorderedPairs(test_patterns))
        print training_error[i + 1]
        print test_error[i + 1]

    # Store the data returned by countMisorderedPairs and plot it, showing how training and testing errors develop.
    # plt.plot(run, testError, 'r', run, trainingError, 'g')
    return [test_error, training_error]
    plt.plot(test_error, label='Test Error')
    plt.plot(training_error, label='Training Error')
    plt.legend()
    plt.show()


def main():
    for i in xrange(5):
        print "Running test", i + 1
        results.append(run_ranker("../datasets/train.txt", "../datasets/test.txt"))

    tests = len(results)
    iterations = len(results[0][0])

    avg_test_error = [0.0]*iterations
    avg_training_error = [0.0]*iterations

    for i in xrange(tests):
        for j in xrange(iterations):
            avg_test_error[j] += results[i][0][j]
            avg_training_error[j] += results[i][1][j]

    for i in xrange(iterations):
        avg_test_error[i] = 1 - (avg_test_error[i] / tests)
        avg_training_error[i] = 1 - (avg_training_error[i] / tests)

    print "Average training success:", avg_training_error
    print "Average test success:", avg_test_error
    plt.plot(avg_test_error, label='Average Test Success')
    plt.plot(avg_training_error, label='Average Training Success')
    plt.legend()
    plt.show()

main()
