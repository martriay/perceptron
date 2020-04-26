#!/usr/bin/env python
from NeuralNet import NeuralNet

def main():
    print("Starting neural network")
    nn = NeuralNet()

    training_set = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    print(f'How many epochs?')
    epochs = int(input())
    nn.train(training_set, epochs)

    print(f'Model trained with {epochs} epochs, now test it!')

    while(True):
        print("Enter X value:")
        x = int(input())
        print("Enter Y value:")
        y = int(input())
        result = nn.predict(x, y)
        print(f'--- Result: {result}')


if __name__ == "__main__":
    main()