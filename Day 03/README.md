### How linear regression learns

Linear regression was learns with a random weight & bias. Initially, the predictions were wrong and there was a great loss. Then gradually predictions were improved and expected answer is obtained.

### Why gradient descent instead of a direct formula

Gradient descent was used instead of direct formula because i wanted to see learning happen so that step by step can be understanded easily.Gradient descent is usually used for large datasets.

### Difference between underfitting & overfitting

Underfitting takes place when a model is too simple to record patterns in a data where overfitting occurs when the model fits the noise.In this project simple linear regression is used because it does not pass through every data point.

### What learning rate worked best and why

We tested it in task 7. The learning rate 0.01 worked best for this dataset. Very small learnin rates made the model slow, whereas large learning rates made the model unstable. So the chosen learning rate provided a balance between steady convergence and training speed.

### One mistake faced and how you fixed it

One major issue i faced is with the python 3.14 version that did not worked with sklearn, it is solved by installing python 3.11 version.The next problem is with multiple plt.show() functions so that output is not obtained, it was solved by blocking the functions.

### Task 2: Data Visualization

A scatter plot of X vs y was created to visualize the relationship between the input and the target. The plot shows a positive linear relationship, where y increase as X increases. The points are not perfectly paced, causing some noise in the data.

### Task 6: Prediction Visualization

The predicted regression line follows the increasing trend in the data points. This shows that the model has learned the relationship between X and y. The line does not pass through every point because the data contains some variability and the model is linear.

### Task 7: Learning Rate Experiment

When a low learning rate (0.01) was used, the loss decreased slowly and the updates were stable. When a high learning rate (0.1) was used, the loss dropped much faster. This experiment shows that the learning rate controls the trade-off between training speed and stability.

### Task 8: sklearn Comparison

The weight, bias, and MSE values obtained from the scratch implementation and the sklearn model are very close to each other. The results are not exactly identical, while the scratch model depends on gradient descent with a fixed learning rate and limited number of epochs. Small differences in optimization method and numerical precision cause slight variations in the final parameters.

### Why scratch and sklearn results differ

Initially, my scratch model’s results differed from sklearn because the number of epochs and learning rate were not enough. Sklearn uses an closed-form solution, so it produces the optimal weights and bias. I fixed this by training the scratch using a suitable learning rate, while both models were trained on the exact same dataset. After this, the scratch MSE became very close to sklearn’s, but not perfectly identical.
