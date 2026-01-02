## PART D — Experiments & Insights
## Task 6: Independence Assumption Test

Naive Bayes is “naive” because it assumes all features are independent. 
In spam detection, words like "free" and "money" are clearly dependent, 
but the model still works well because it uses overall word probabilities to classify messages.

## What does each probability term represent?

Probability      	Meaning (Simple)

P(Class)	        How common the class is in general
P(Features)         (Class)
P(Features)	        How likely the features appear overall
P(Class)            (Features)

## Why Naive Bayes works well even with simple assumptions?

Naive Bayes assumes features are independent, but it still works well because it captures overall probability patterns. Strong indicators, like certain words in spam detection, help the model make accurate predictions even when features are not truly independent.

## Why results are similar but not identical.

Both scratch and sklearn Naive Bayes use the same basic algorithm, so predictions and accuracy are very close. Minor differences arise from smoothing, floating-point calculations, and internal optimizations in sklearn, which can slightly change probabilities.

## PART F — README REQUIREMENTS
## What Bayes’ Theorem means intuitively

Bayes’ Theorem tells us how to update the probability of a class after seeing evidence.

## What “naive” assumption is

It’s called “naive” because the model pretends all features are independent, even though they usually aren’t.

## Why it works well for text

Even though the independence assumption isn’t true, Naive Bayes works because some words are really strong clues.

## Where it can fail

When features depend heavily on each other.
With rare words or very small datasets.
Numeric features that don’t follow a Gaussian curve.

## One mistake I faced and how I fixed it

At first, I multiplied tiny probabilities directly, and the numbers became too small to handle, giving wrong predictions.
I fixed it by using log probabilities, turning multiplications into additions and now the predictions work correctly.