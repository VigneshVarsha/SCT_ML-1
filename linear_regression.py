import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load Data
train_path = "train.csv" if os.path.exists("train.csv") else "data/train.csv"
test_path = "test.csv" if os.path.exists("test.csv") else "data/test.csv"

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)

# 2. Feature Engineering (Map columns for sqft, bedrooms, bathrooms)
# Training set
train_df['TotalBath'] = (
    train_df['FullBath'] + 
    0.5 * train_df['HalfBath'] + 
    train_df['BsmtFullBath'] + 
    0.5 * train_df['BsmtHalfBath']
)

# Test set (fill missing basement bath entries if any)
test_df['BsmtFullBath'] = test_df['BsmtFullBath'].fillna(0)
test_df['BsmtHalfBath'] = test_df['BsmtHalfBath'].fillna(0)
test_df['TotalBath'] = (
    test_df['FullBath'] + 
    0.5 * test_df['HalfBath'] + 
    test_df['BsmtFullBath'] + 
    0.5 * test_df['BsmtHalfBath']
)

feature_cols = ['GrLivArea', 'BedroomAbvGr', 'TotalBath']
target_col = 'SalePrice'

# Handle any missing values in selected features
X = train_df[feature_cols].fillna(train_df[feature_cols].median())
y = train_df[target_col]

# 3. Train / Validation Split
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train Multiple Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate on Validation Set
y_pred = model.predict(X_val)
r2 = r2_score(y_val, y_pred)
rmse = np.sqrt(mean_squared_error(y_val, y_pred))

print("=== Task 01: Ames Housing Linear Regression ===")
print(f"R² Score: {r2:.4f}")
print(f"RMSE: ${rmse:,.2f}")
print("\nFeature Coefficients:")
for feat, coef in zip(feature_cols, model.coef_):
    print(f"  {feat}: {coef:,.2f}")
print(f"Intercept: {model.intercept_:,.2f}")

# 6. Predict on Official Test Set and Generate Submission CSV
X_test = test_df[feature_cols].fillna(X.median())
test_predictions = model.predict(X_test)

submission = pd.DataFrame({
    'Id': test_df['Id'],
    'SalePrice': test_predictions
})
# Keep CSV values in plain decimal form to avoid scientific notation like 1.23e+05
submission.to_csv("submission_task1.csv", index=False, float_format='%.2f')
print("\nPredictions saved to 'submission_task1.csv'")

# 7. Visualize Actual vs Predicted
plt.figure(figsize=(8, 5))
ax = plt.gca()
plt.scatter(y_val, y_pred, alpha=0.5, color='darkblue', edgecolors='k')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2, label="Perfect Fit Line")
plt.xlabel("Actual SalePrice ($)")
plt.ylabel("Predicted SalePrice ($)")
plt.title("Task 01: Actual vs. Predicted House Prices")

formatter_x = ScalarFormatter(useOffset=False)
formatter_y = ScalarFormatter(useOffset=False)
formatter_x.set_scientific(False)
formatter_y.set_scientific(False)
ax.xaxis.set_major_formatter(formatter_x)
ax.yaxis.set_major_formatter(formatter_y)
ax.format_coord = lambda x, y: f"x, y = ({x:,.0f}, {y:,.0f})"
ax.ticklabel_format(style='plain', axis='both', useOffset=False)

plt.legend()
plt.tight_layout()
plt.savefig("actual_vs_predicted.png", dpi=150)  # always save the plot
print("Plot saved to 'actual_vs_predicted.png'")

# Only open a window if an interactive backend is available (avoid hanging headless)
if plt.get_backend().lower() not in ("agg", "pdf", "svg", "ps", "cairo"):
    plt.show()