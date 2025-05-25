import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

def split_data(df, target_column='Profit', test_size=0.2, random_state=42):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def train_linear_regression(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def train_polynomial_regression(X_train, y_train, degree=2):
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X_train)
    model = LinearRegression()
    model.fit(X_poly, y_train)
    return model, poly

def train_decision_tree(X_train, y_train):
    model = DecisionTreeRegressor(random_state=42)
    model.fit(X_train, y_train)
    return model

def train_random_forest(X_train, y_train, n_estimators=100):
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test, poly_transformer=None):
    if poly_transformer:
        X_test = poly_transformer.transform(X_test)
    predictions = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)
    return rmse, r2

def get_best_model(models_performance):
    return max(models_performance.items(), key=lambda item: item[1]['r2'])

