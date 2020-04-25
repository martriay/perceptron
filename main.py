#!/usr/bin/env python
import numpy, random


def main():
    print("Starting neural network")
    nn = NeuralNet()

    print(f'How many epochs?')
    epochs = int(input())
    nn.train(epochs)

    print(f'Model trained with {epochs} epochs, now test it!')

    while(True):
        print("Enter X value:")
        x = int(input())
        print("Enter Y value:")
        y = int(input())
        result = nn.predict(x, y)
        print(f'--- Result: {result}')


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

        self.weights[0] += error * a * self.lr
        self.weights[1] += error * b * self.lr
        self.weights[2] += error * self.bias * self.lr

    def train(self, n = 50):
        for _ in range(n) :
            self.perceptron(1,1,0) #True or true
            self.perceptron(1,0,1) #True or false
            self.perceptron(0,1,1) #False or true
            self.perceptron(0,0,0) #False or false
            print(self.weights)





if __name__ == "__main__":
    main()