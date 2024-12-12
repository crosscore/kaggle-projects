from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from tqdm import tqdm
import time
import joblib

def train_model_with_progress(X, y, test_size=0.2, random_state=42):
    """
    Train a linear regression model with progress tracking

    Parameters:
    -----------
    X : array-like of shape (n_samples, n_features)
        Training data
    y : array-like of shape (n_samples,)
        Target values
    test_size : float, default=0.2
        Proportion of the dataset to include in the test split
    random_state : int, default=42
        Random state for reproducibility

    Returns:
    --------
    model : LinearRegression
        Trained model
    score : float
        R-squared score on test data
    """
    # Convert input data to numpy arrays
    X = np.array(X)
    y = np.array(y)

    # Data validation
    if len(X) != len(y):
        raise ValueError("Input X and y must have the same length")

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Initialize model
    model = LinearRegression()

    # Simulate training progress (since LinearRegression is actually instant)
    print("Training model...")
    steps = 10
    progress_bar = tqdm(total=steps, desc="Training Progress")

    for _ in range(steps):
        time.sleep(0.01)  # Simulate computation time
        progress_bar.update(1)

    # Actual model fitting
    model.fit(X_train, y_train)
    progress_bar.close()

    # Evaluate model
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    print(f"\nTraining Score (R²): {train_score:.4f}")
    print(f"Test Score (R²): {test_score:.4f}")
    print(f"Coefficient: {model.coef_[0]:.4f}")
    print(f"Intercept: {model.intercept_:.4f}")

    return model, test_score

if __name__ == "__main__":
    # Sample data
    X_temp = [[15], [17], [19], [20], [22], [23], [25], [27], [28], [30]] # Temperature (°C)
    y_sales = [100, 120, 140, 150, 170, 180, 200, 220, 230, 250]          # Ice cream sales (units)

    try:
        # Train model
        model, score = train_model_with_progress(X_temp, y_sales)

        # Save model
        model_path = 'model.joblib'
        joblib.dump(model, model_path)
        print(f"\nModel saved successfully to {model_path}")

    except Exception as e:
        print(f"Error occurred: {str(e)}")
