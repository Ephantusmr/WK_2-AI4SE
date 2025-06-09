# Saving the model and scaler
joblib.dump(logreg, 'diabetes_logreg_model.pkl')
joblib.dump(scaler, 'diabetes_scaler.pkl')
print("Model and scaler saved successfully.")

#random forest model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_scaled, y_train)
y_pred_rf = rf.predict(X_test_scaled)
rf_accuracy = accuracy_score(y_test, y_pred_rf)
print(f"Random Forest Accuracy: {rf_accuracy:.4f}")
print("\nRandom Forest Classification Report:")
print(classification_report(y_test, y_pred_rf))
joblib.dump(rf, 'diabetes_rf_model.pkl')