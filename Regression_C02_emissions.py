from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (make sure you're in the correct directory)
df = pd.read_csv('/Users/mitch/Downloads/FuelConsumptionCo2.csv')

x = df.loc[:, 'ENGINESIZE'].values
y = df.loc[:, 'CO2EMISSIONS'].values

# Split into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

x_train = x_train.reshape(-1,1)
x_test = x_test.reshape(-1,1)

# Create linear regression object
regr = LinearRegression()

# Train the model using the training sets
regr.fit(x_train, y_train)

# Make predictions using the testing set
y_pred = regr.predict(x_test)

# The coefficients
np.set_printoptions(precision=4)
print('Coefficient:', regr.coef_)
print('Intercept:', regr.intercept_)

# Evaluation
print("Mean absolute error: ", mean_absolute_error(y_test, y_pred))
print("Variance score: ",  r2_score(y_test, y_pred))

# Plot training results
plt.scatter(x_train, y_train, color='orange', marker='+')
plt.plot(x_train, regr.predict(x_train), color='green', linewidth=3)
plt.title('Training results')
plt.xlabel('Engine Size')
plt.ylabel('CO2 Emissions')
plt.legend(['Predicted', 'Actual'])
plt.show()

# Plot test results
plt.scatter(x_test, y_test, color='purple', marker='+')
plt.plot(x_test, regr.predict(x_test), color='red', linewidth=3)
plt.title('Testing Results')
plt.xlabel('Engine Size')
plt.ylabel('CO2 Emission')
plt.legend(['Predicted', 'Actual'])
plt.show()







