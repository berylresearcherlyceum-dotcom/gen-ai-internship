## Task 2 - why linear regression can’t be used directly:

Linear regression cannot be used because it predicts continuous values that may be outside 0–1, while binary classification needs outputs that represent probabilities or discrete class labels.

## Task 3 - what does sigmoid function represents:

The sigmoid function prodeces values between 0 and 1. It represents the probability that the input belongs to the positive class (1).

## Task 5 - what does a decreasing loss mean in classification:

A decreasing loss means the model’s predictions are getting closer to the true labels, indicating that it is learning and improving.

## Task 7 - Why accuracy alone can be a misleading:

Accuracy alone can be misleading because it may be high even if the model fails to correctly predict the minority class; precision and recall provide a better picture.

## Task 8 - Explain trade-off:

There is a trade-off between precision and recall: lowering the threshold increases recall but decreases precision, while raising it increases precision but decreases recall.

## Task 9 - Why outputs are similar but not identical:

The outputs are similar but not identical because the scratch model and sklearn use slightly different optimization methods, stopping criteria, and floating-point computations.

## Why sigmoid is used instead of a straight line:

A straight line can give values less than 0 or greater than 1, which cannot be interpreted as probabilities.

The sigmoid function squashes any input into the range 0 to 1, so it can be used to predict the probability of a positive class (eg, passing an exam).

## Difference between probability and class label:

Probability: A number between 0 and 1 showing how likely the positive class is.
Class label: A discrete value (0 or 1) obtained by applying a threshold to the probability.

## What binary cross-entropy measures:

Binary cross-entropy (BCE) measures how far the model’s predicted probabilities are from the true labels.
Lower BCE means predictions are closer to actual outcomes.
It is the standard loss function for binary classification.

## Effect of changing threshold:

Threshold decides the cutoff for converting probabilities into class labels.
Lower threshold → more positives predicted → higher recall, lower precision
Higher threshold → less positives predicted → higher precision, lower recall
Choosing the threshold depends on whether you want to catch more positives or avoid false positives.

## One mistake faced and how it was fixed:

One mistake I did is I tried to compare predictions of the scratch model with sklearn, but got model is not defined.Then it was fixed by creaing and training the scratch model before using.

model = LogisticRegressionScratch()
model.fit(X, y)

After that, predictions could be compared without errors.