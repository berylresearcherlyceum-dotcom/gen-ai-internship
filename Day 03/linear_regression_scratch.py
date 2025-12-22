#Part-A Dataset & Visualization
#Task 1: Dataset Selection
#Dataset Chosen: Simple Synthetic Dataset

X = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

#Task 2: Data Visualization

import numpy as np
import matplotlib.pyplot as plt

# Dataset
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Scatter plot
#plt.scatter(X, y)
#plt.xlabel("X (Input Feature)")
#plt.ylabel("y (Target Variable)")
#plt.title("Scatter Plot of X vs y")
#plt.show()


#PART B — Linear Regression from Scratch
#Task 3: Model Implementation

import numpy as np

class LinearRegressionScratch:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.w = 0.0
        self.b = 0.0
        self.losses = []

    def fit(self, X, y):
        n = len(X)
        for _ in range(self.epochs):
            y_pred = self.w * X + self.b
            loss = (1 / n) * np.sum((y - y_pred) ** 2)
            self.losses.append(loss)

            dw = (-2 / n) * np.sum(X * (y - y_pred))
            db = (-2 / n) * np.sum(y - y_pred)

            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db

    def predict(self, X):
        return self.w * X + self.b


# ---------- RUN HERE ----------
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

model = LinearRegressionScratch(learning_rate=0.01, epochs=1000)
model.fit(X, y)

predictions = model.predict(X)

print("Weight:", model.w)
print("Bias:", model.b)
print("Predictions:", predictions)

#Task 4: Training & Convergence

import numpy as np
import matplotlib.pyplot as plt

class LinearRegressionScratch:

    def __init__(self, learning_rate=0.01, epochs=50):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.w = 0.0
        self.b = 0.0
        self.losses = []

    def fit(self, X, y):
        n = len(X)
        for _ in range(self.epochs):
            y_pred = self.w * X + self.b
            loss = (1 / n) * np.sum((y - y_pred) ** 2)
            self.losses.append(loss)

            dw = (-2 / n) * np.sum(X * (y - y_pred))
            db = (-2 / n) * np.sum(y - y_pred)

            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db
    def predict(self, X):
        return self.w * X + self.b

# -------- RUN --------
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

model = LinearRegressionScratch()
model.fit(X, y)

print("Loss values:", model.losses)

# -------- LOSS PLOT ONLY --------
#plt.figure()
#plt.plot(model.losses, marker='o')
#plt.xlabel("Epoch")
#plt.ylabel("Loss")
#plt.title("Loss vs Epochs")
#plt.grid(True)

import matplotlib.pyplot as plt

# Plot Loss vs Epochs
#plt.figure()
#plt.plot(model.losses)
#plt.xlabel("Epoch")
#plt.ylabel("Mean Squared Error (Loss)")
#plt.title("Training Loss vs Epochs")
#plt.grid(True)
#plt.show()

#PART C — Model Evaluation
#Task 5: Evaluation Metrics (From Scratch)

# Predictions
y_pred = model.predict(X)

# Metrics from scratch
def mean_squared_error(y_true, y_pred):
    return (1 / len(y_true)) * sum((y_true - y_pred) ** 2)

def mean_absolute_error(y_true, y_pred):
    return (1 / len(y_true)) * sum(abs(y_true - y_pred))

mse = mean_squared_error(y, y_pred)
mae = mean_absolute_error(y, y_pred)

#print("Mean Squared Error (MSE):", mse)
#print("Mean Absolute Error (MAE):", mae)

#Task 6: Prediction Visualization

import matplotlib.pyplot as plt

# Plot actual data and predicted regression line
#plt.figure()
#plt.scatter(X, y, label="Actual Data")
#plt.plot(X, y_pred, color="red", label="Predicted Regression Line")
#plt.xlabel("X")
#plt.ylabel("y")
#plt.title("Actual Data vs Predicted Regression Line")
#plt.legend()
#plt.grid(True)
#plt.show()

#PART D — Diagnostics & Insights
#Task 7: Learning Rate Experiment

import matplotlib.pyplot as plt
import numpy as np

# Dataset
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Low learning rate model
model_low_lr = LinearRegressionScratch(learning_rate=0.001, epochs=1000)
model_low_lr.fit(X, y)

# High learning rate model
model_high_lr = LinearRegressionScratch(learning_rate=0.1, epochs=1000)
model_high_lr.fit(X, y)

#Task 8: sklearn Comparison

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# Reshape X for sklearn (IMPORTANT)
X_sklearn = X.reshape(-1, 1)

# Train sklearn model
sk_model = LinearRegression()
sk_model.fit(X_sklearn, y)

# Predictions
y_pred_sklearn = sk_model.predict(X_sklearn)
sk_weight = sk_model.coef_[0]
sk_bias = sk_model.intercept_

# ---------- TASK 8: SKLEARN COMPARISON ----------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# sklearn expects 2D X
X_sklearn = X.reshape(-1, 1)

sk_model = LinearRegression()
sk_model.fit(X_sklearn, y)

y_pred_sklearn = sk_model.predict(X_sklearn)

print("\n--- SKLEARN MODEL ---")
print("Sklearn Weight:", sk_model.coef_[0])
print("Sklearn Bias:", sk_model.intercept_)
print("Sklearn MSE:", mean_squared_error(y, y_pred_sklearn))

print("\n--- SCRATCH MODEL ---")
print("Scratch Weight:", model.w)
print("Scratch Bias:", model.b)
print("Scratch MSE:", mse)

