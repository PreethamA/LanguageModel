import numpy as np

class Model:
    def __init__(self):
        self.weights = None

    def train(self, X, y):
        # Add a column of ones for the bias term
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        
        # Compute the weights using the normal equation
        self.weights = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

    def predict(self, X):
        # Add a column of ones for the bias term
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        
        # Make predictions
        predictions = X_b.dot(self.weights)
        return predictions

# Example usage:
if __name__ == "__main__":
    # Creating a dataset
    X_train = np.array([[1, 2], [3, 4], [5, 6]])
    y_train = np.array([3, 5, 7])

    # Creating a model
    model = Model()

    # Training the model
    model.train(X_train, y_train)

    # Making predictions
    X_test = np.array([[2, 3], [4, 5]])
    predictions = model.predict(X_test)
    print("Predictions:", predictions)

