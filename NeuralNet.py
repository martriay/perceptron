#!/usr/bin/env python
import numpy, random


class NeuralNet():
    def __init__(self, lr = 1, bias = 1):
        self.lr = lr
        self.bias = bias
        self.weights = [random.random(),random.random(),random.random()]

    def predict(self, a, b):
        output = a * self.weights[0] + b * self.weights[1] + self.bias * self.weights[2]
        output = 1/(1+numpy.exp(-output)) # activation function: sigmoid
        return output

    def perceptron(self, a, b, expected) :
        output = self.predict(a, b)
        error = expected - output

        self.weights[0] += error * self.lr * a
        self.weights[1] += error * self.lr * b
        self.weights[2] += error * self.lr * self.bias

    def train(self, n = 50):
        for _ in range(n) :
            self.perceptron(1,1,0) #True or true
            self.perceptron(1,0,1) #True or false
            self.perceptron(0,1,1) #False or true
            self.perceptron(0,0,0) #False or false
            print(self.weights)
