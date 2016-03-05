""" Forward-Backward algorithm

    Attributes:
        O (array): Observation model when the observation is true
        O_ (array):  Observation model when the observation is false
        T (array): Transition model

"""

import numpy as np

O = np.array([[0.9, 0.0], [0.0, 0.2]])
O_ = np.array([[0.1, 0.0], [0.0, 0.8]])
T = np.array([[0.7, 0.3], [0.3, 0.7]])


def FORWARD(fv, ev):
    """ The forward part of the forward_backward algorithm.
    If the current observation is true, the true observation model will be used, otherwise the false one will be.

    :param fv: The previous forward message
    :param ev: The current evidence value
    :return: The normalized matrix multiplication of O, T transformed and the forward message
    """
    global O, O_, T
    if ev:
        return NORMALIZE(np.dot(np.dot(O, T.T), fv))
    else:
        return NORMALIZE(np.dot(np.dot(O_, T.T), fv))


def BACKWARD(b, ev):
    """ The backward part of the forward_backward algorithm.
    If the current observation is true, the true observation model will be used, otherwise the false one will be.

    :param b: The backward message
    :param ev: The current evidence value
    :return: The matrix multiplication of T, O and b
    """
    global T
    if ev:
        return np.dot(np.dot(T, O), b)
    else:
        return np.dot(np.dot(T, O_), b)


def FORWARD_BACKWARD(ev, prior):
    """ The forward-backward algorithm, as described in Figure 4 p. 586

    :param ev: A vector of evidence values
    :param prior: The prior distribution on the initial state P(X0)
    :return: A vector of smoothed estimates for steps 1,...,t
    """
    fv = np.array([None] * (len(ev) + 1))
    b = np.array([1, 1])
    sv = np.array([None] * (len(ev) + 1))

    fv[0] = prior
    print "Forward:"
    for i in range(1, len(ev)+1):
        fv[i] = FORWARD(fv[i - 1], ev[i-1])
        print "f" + str(i), ":", fv[i]
    print "\nBackward:"
    for i in reversed(range(0, len(ev)+1)):
        sv[i] = NORMALIZE(fv[i]* b)
        b = BACKWARD(b, ev[i-1])
        print "b" + str(i), ":", b

    return sv


def NORMALIZE(m):
    """
    :param m: The vector to be normalized
    :return: The normalized vector
    """
    return m / m.sum()


def main():
    prior = np.array([0.5, 0.5])
    ev = [True, True, False, True, True]

    fb = FORWARD_BACKWARD(ev, prior)
    print "\nForward-Backward:"
    for line in range(0, len(fb)):
        print "Day", line, ":", "[", fb[line][0], ",", fb[line][1], "]"

    exit()


main()
