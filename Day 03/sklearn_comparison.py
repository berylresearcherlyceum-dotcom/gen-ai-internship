import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# same dataset as scratch
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("Weight:", model.coef_[0])
print("Bias:", model.intercept_)
print("MSE:", mean_squared_error(y, y_pred))
