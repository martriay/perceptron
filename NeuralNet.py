#!/usr/bin/env python
import numpy, random

class NeuralNet():
    def __init__(self, lr = 1, bias = 1):
        self.lr = lr
        self.bias = bias
        self.weights = [random.random(),random.random(),random.random()]

    def train(self, training_set=[], epochs = 50):
        for i in range(epochs):
            for item in training_set:
                self.perceive(item[0], item[1], item[2])

            print(f'Epoch {i}/{epochs}: {self.weights}')

    def predict(self, a, b):
        output = numpy.dot([a, b, self.bias], self.weights)
        return sigmoid(output) # activation function

    def perceive(self, x, y, expected) :
        output = self.predict(x, y)
        error = expected - output

        self.weights[0] += error * self.lr * x
        self.weights[1] += error * self.lr * y
        self.weights[2] += error * self.lr * self.bias


def sigmoid(x):
    return 1/(1+numpy.exp(-x))