# linear_regression_comparison.py

import numpy as np
import matplotlib
matplotlib.use('TkAgg')   # Ensures plot shows in a separate window
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([3,5,7,9,11])

# Scratch Linear Regression
class LinearRegressionScratch:
    def __init__(self):
        self.weights = None
        self.bias = None
        self.loss_history = []
    
    def fit(self, X, y, learning_rate=0.01, epochs=2000):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(epochs):
            y_pred = np.dot(X, self.weights) + self.bias
            error = y_pred - y
            dw = (1/n_samples) * np.dot(X.T, error)
            db = (1/n_samples) * np.sum(error)
            self.weights -= learning_rate * dw
            self.bias -= learning_rate * db
            mse = (1/n_samples) * np.sum(error**2)
            self.loss_history.append(mse)
    
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

# Train Scratch Model
scratch_model = LinearRegressionScratch()
scratch_model.fit(X, y)
pred_scratch = scratch_model.predict(X)
mse_scratch = np.mean((pred_scratch - y)**2)

# Train Sklearn Model
sk_model = LinearRegression()
sk_model.fit(X, y)
pred_sk = sk_model.predict(X)
mse_sk = np.mean((pred_sk - y)**2)

# Print Results
print("Scratch weights:", scratch_model.weights, "bias:", scratch_model.bias, "MSE:", mse_scratch)
print("Sklearn weights:", sk_model.coef_, "bias:", sk_model.intercept_, "MSE:", mse_sk)

# Plot Epoch vs Loss

import matplotlib.pyplot as plt

# Create the plot
plt.figure()
plt.plot(scratch_model.loss_history, color='blue', marker='o')
plt.xlabel("Epochs")
plt.ylabel("MSE Loss")
plt.title("Scratch Model Convergence")

# Save the plot as an image in the same folder
plt.savefig("loss_plot.png")
plt.close() 
print("Plot saved as 'loss_plot.png' in the current folder.")

