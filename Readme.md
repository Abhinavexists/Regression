# Regression

A comprehensive implementation of various regression techniques using Python, including Simple Linear Regression, Multiple Linear Regression, and Polynomial Regression for different datasets.

## Overview

This project demonstrates different regression analysis techniques:
- Simple Linear Regression (Height-Weight Analysis)
- Multiple Linear Regression (Economic Index Analysis)
- Polynomial Regression (Non-linear Data Modeling)

## Project Structure

```
.
├── Datasets/
│   ├── Economic_Index.csv
│   └── Height_Weight.csv
├── Notebooks/
│   ├── Multiple_Linear_Regression.ipynb
│   ├── Polynomial_Regression.ipynb
│   └── Simple_Linear_Regression.ipynb
├── .gitignore
├── LICENSE
└── requirements.txt
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Abhinavexists/Regression.git
cd Regression
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Dependencies

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- statsmodels

## Usage

### Simple Linear Regression
- Analyzes the relationship between height and weight
- Features standardization and model evaluation
- Includes R-squared and adjusted R-squared calculations

### Multiple Linear Regression
- Analyzes economic indices including interest rates and unemployment rates
- Implements feature scaling and cross-validation
- Includes comprehensive model evaluation metrics

### Polynomial Regression
- Demonstrates handling of non-linear relationships
- Implements polynomial feature transformation
- Includes model comparison with different polynomial degrees

## Model Evaluation Metrics

All implementations include various evaluation metrics:
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R-squared Score
- Adjusted R-squared Score

## Results Visualization

Each notebook includes detailed visualizations:
- Scatter plots
- Correlation matrices
- Regression lines
- Residual plots
- Pair plots

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.