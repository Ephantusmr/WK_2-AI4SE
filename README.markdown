# Diabetes Prediction Model

## Overview
This project implements a machine learning model to predict diabetes using a dataset with patient features such as Pregnancies, Glucose, BMI, etc. The script includes data preprocessing, model training, evaluation, and visualization of results using metrics like accuracy, F1-score, and ROC curves. It also supports diagnosing individual patients and providing recommendations.

## Features
- Loads and preprocesses diabetes dataset
- Trains a machine learning model (saved as `diabetes_model.pkl`)
- Evaluates model performance with accuracy, MAE, F1-score, confusion matrix, and ROC curve
- Generates visualizations (confusion matrix and ROC curve)
- Supports individual patient diagnosis with treatment recommendations

## Requirements
- Python 3.8+
- Libraries: 
  - pandas
  - scikit-learn
  - matplotlib
  - seaborn
  - joblib

Install dependencies using:
```bash
pip install pandas scikit-learn matplotlib seaborn joblib
```

## Setup
1. Clone the repository or download the project files.
2. Ensure the dataset is available (expected to be loaded in `load_data()`).
3. Install required Python libraries (see Requirements).
4. Place the script and dataset in the same directory.

## Usage
1. **Run the Script**:
   Execute the main script to preprocess data, train the model, evaluate performance, and generate visualizations:
   ```bash
   python diabetes_model.py
   ```
   Replace `diabetes_model.py` with the actual script name if different.

2. **Output Files**:
   - Preprocessed data: `X_train.csv`, `X_test.csv`, `y_train.csv`, `y_test.csv`
   - Scaler: `scaler.pkl`
   - Trained model: `diabetes_model.pkl`
   - Visualizations: `confusion_matrix.png`, `roc_curve.png`

3. **Patient Diagnosis**:
   The script includes an example patient diagnosis. Modify the `example_patient` dictionary in the script to diagnose other patients.

4. **View Results**:
   - Check console output for metrics (accuracy, MAE, F1-score, confusion matrix).
   - View `confusion_matrix.png` and `roc_curve.png` for visualizations.

## File Structure
```
project_directory/
├── diabetes_model.py       # Main script (assumed name)
├── X_train.csv             # Preprocessed training features
├── X_test.csv              # Preprocessed testing features
├── y_train.csv             # Training labels
├── y_test.csv              # Testing labels
├── scaler.pkl              # Saved scaler object
├── diabetes_model.pkl      # Saved trained model
├── confusion_matrix.png    # Confusion matrix visualization
├── roc_curve.png           # ROC curve visualization
└── README.md               # This file
```

## Notes
- The script assumes a `load_data()` function to load the dataset. Ensure this function is implemented or provide the dataset in the expected format.
- The `preprocess_data` and `train_model` functions are referenced but not shown in the provided code. Ensure they are defined in the script.
- Visualizations are saved as PNG files in the project directory.
- The example patient diagnosis is hardcoded; modify as needed for different inputs.

## Troubleshooting
- **Missing dataset**: Ensure the dataset is accessible to the `load_data()` function.
- **Module errors**: Verify all required libraries are installed.
- **File not found**: Check that preprocessed data and model files are in the correct directory when loading.

## License
This project is licensed under the MIT License.