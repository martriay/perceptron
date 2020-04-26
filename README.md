# perceptron

Extra basic neural network project. At the moment, it simply learns how to perform a simple OR operation on two X and Y inputs.

```
$ python main.py
== Starting neural network
> How many epochs?
100
Epoch 0/100: [0.6119441736350664, 0.6745495455072777, 1.0594835640410034]
(...)
Epoch 99/100: [6.857739870119925, 6.894447481940778, -2.9396415622721297]
== Model trained successfully
-------------------------------------------------
== Test:
> Enter X value:
0
> Enter Y value:
0
=> Result: 0.050228369877961365
-------------------------------------------------
== Test:
> Enter X value:
0
> Enter Y value:
1
=> Result: 0.9811979057789876
-------------------------------------------------
== Test:
> Enter X value:
1
> Enter Y value:
0
=> Result: 0.9805086044694676
-------------------------------------------------
== Test:
> Enter X value:
1
> Enter Y value:
1
=> Result: 0.9999798552315742
-------------------------------------------------
```