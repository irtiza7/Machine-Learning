import numpy as np

class LinearRegression():
    """
    predicted_y = 1 * training examples
    feature_vector = number of features * training examples
    weights_vector = 1 * number of features

    """
    def __init__(self, total_samples, learning_rate = 0.01, total_iterations = 10000):
        self.learning_rate = learning_rate
        self.total_iterations = total_iterations
        self.total_samples = total_samples

    def predict_y(self, feature_vector, weight_vector, bias):
        dot_prod = np.dot(weight_vector.T, feature_vector)
        return dot_prod

    def calculate_loss(self, actual_y, predicted_y):
        difference = predicted_y - actual_y
        squared_error = np.power(difference, 2)
        sum_of_squared_errors = np.sum(squared_error)
        loss = sum_of_squared_errors / self.total_samples
        return loss

    def gradient_descent(self, old_weight_vector, feature_vector, predicted_y, actual_y):
        dl_dw = np.dot(feature_vector, (predicted_y - actual_y).T)
        sum_of_dl_dw = np.sum(dl_dw)
        dl_dw = sum_of_dl_dw * (2 / m)
        new_weight_vector = old_weight_vector - self.learning_rate * dl_dw
        return new_weight_vector