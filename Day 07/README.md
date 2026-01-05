## PART A — Model Comparison (Core Hands-On)
## Task 1: Choose a Single Dataset

A single dataset is used for all models in this assignment.

Problem type: Binary classification

Dataset selected: Spam vs Ham (email classification)

Classes: Spam and Ham

Dataset size: 30 samples, kept small on purpose within the required range of 20–40 samples

Mini Dataset Example:

Email ID	        Text (feature)	             Label (target)
1	               "Win a free phone now!"	        Spam
2	               "Meeting at 10 am"	            Ham
3                  "Claim your prize today"  	    Spam
4	               "Lunch tomorrow?"	            Ham
5	               "You won $1000"	                Spam
6	               "Project deadline extended"	    Ham
7	               "Congratulations! You won"	    Spam
8	               "Can we reschedule?"	            Ham
…	                       …                   	     …
30	               "Last chance to claim reward"	Spam

Feature: Email text 
Label: Binary (Spam vs Ham)

## Which model performed best and why

“Naive Bayes wins because it understands text, learns quickly even from a small dataset, and predicts Spam most accurately.”

## Example of underfitting and overfitting

Overfitting:

k-NN with k = 1 is an example of overfitting.
It gives very high training accuracy but low testing accuracy.
The model learns too much and fails on new data.

Underfitting:

k-NN with k = 5 is an example of underfitting.
It gives low training accuracy and low testing accuracy.
The model learns too little and misses important patterns.

## What bias–variance tradeoff means

Bias–variance tradeoff means balancing between a model that is too simple and a model that is too complex.

The goal is to choose a model that performs well on both training data and new data.

## How GenAI systems use model routing

GenAI systems use model routing to decide which model should handle a task.
The decision is based on the type of input, like text or numbers.
This helps the system choose the most suitable model automatically.

## One mistake faced and how it was fixed

One mistake I faced was using a large value of k in k-NN with a small dataset, which caused an error.
I fixed this by reducing the value of k and making sure it was smaller than the training data size.





