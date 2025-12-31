## Task 6: Conceptual Understanding

**Decision Tree:** A tree-structured model for classification or regression. Internal nodes are decisions, branches are outcomes, leaves are predicted labels or values.

**Split:** Dividing data based on a feature and threshold to maximize class purity.

**Interpretability:** Predictions can be traced along paths, making decision trees transparent and explainable.

## Why Distance Matters in k-NN

In k-NN, the predicted class of a point is determined by the classes of its nearest neighbors.
Distance measures how similar two points are—closer points are more likely to share the same class.
If distance is not meaningful, k-NN cannot correctly identify neighbors, leading to poor predictions.

## Effect of k in k-NN

Small k: The prediction depends on only the nearest neighbor. This makes the model sensitive to noise and outliers → overfitting.

Large k: The prediction considers many neighbors. This smooths out local variations, which may ignore small but important patterns → underfitting.

In short: Small k → high variance, low bias
          Large k → low variance, high bias.

## Why Deeper Trees Overfit

Deeper trees fit the training data too closely, including noise and outliers.
This reduces generalization on new data, so it causes overfitting. 

## How a Prediction Flows from Root to Leaf

A prediction starts at the root node and follows feature-based decisions at each internal node.
At each step, the sample moves along the branch that satisfies the node’s condition until it reaches a leaf, where the predicted class is assigned.

## How k-NN Makes Predictions

k-NN looks at the closest k points to the one you want to classify.
Whichever class shows up most among them becomes the prediction.

## Why Distance Matters

Distance tells k-NN which points are “neighbors”.
Closer points are usually more similar, so picking the right neighbors depends on distance.

## Effect of k

Small k → only the closest neighbor counts (overfit) 
Big k → more neighbors count → smoother predictions, but can miss small patterns (underfit).

## Why Decision Trees Are Easy to Understand

They’re basically if-then rules. You can follow the path from the root to a leaf to see exactly why a prediction was made.

## Why Deep Trees Overfit

If the tree goes too deep, it starts learning the noise and outliers in the training data.
That means it does great on training data but worse on new data.

## One Mistake I Faced

I first plotted all k-NN graphs the same way — it was confusing.Then i fixed it by highlighting the nearest neighbors differently for each k and focused on individual test points. Now it’s super clear.
