### What Backpropagation Does

Backpropagation is like **helping the network learn from its mistakes**.  
Backpropagation tells each neuron **how much it should change** to be more correct next time.We update the weights little by little.  
Doing this many times, the network gradually **learns to make better predictions**.

### Why ANN is More Flexible Than Logistic Regression

ANNs can capture more complicated relationships in the data than simple logistic regression.

## What is a neuron

A neuron is like a tiny “decision maker” in a network. It looks at the inputs, combines them using weights and bias, and decides an output using an activation function.

## Why hidden layers matter

Hidden layers help the network learn tricky patterns. Without them, it can only make simple straight-line decisions. With them, it can understand more complex rules.

## What backpropagation actually does

Backpropagation teaches the network from its mistakes. It checks how wrong the output is and tells each neuron how to adjust so the next prediction is better.

## Difference between ANN and logistic regression

Logistic regression can only make straight-line decisions.

ANN with hidden layers can learn curved or complicated patterns, so it can handle harder problems.

## How this ANN fits into a Generative AI pipeline

The ANN acts as a “prompt checker”. It decides if a user’s input is ready for the AI to process, helping avoid incomplete or confusing outputs.

## One mistake faced and how it was fixed

The network wasn’t learning and the loss stayed the same.The learning rate was too high, so updates were unstable. I fixed it by Lowering it and restarting the training.

## Why my network initially did not learn, and how I fixed it

At first, my neural network was not learning because the loss was around 0.693 and the predictions stayed close to 0.5. I fixed this by normalizing the features and slightly increasing the learning rate. After this, the loss started decreasing and the predictions became more confident.
