from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Train a simple dummy model on startup for demonstration
# Features: [income, credit_score, loan_amount, employment_status (1/0)]
X_train = np.array([
    [50000, 700, 15000, 1],
    [30000, 550, 20000, 0],
    [80000, 750, 10000, 1],
    [20000, 500, 25000, 0],
    [120000, 800, 5000, 1],
    [45000, 620, 30000, 1],
    [60000, 680, 12000, 1],
    [25000, 520, 15000, 0]
])
# Labels: 1 = Approved, 0 = Rejected
y_train = np.array([1, 0, 1, 0, 1, 0, 1, 0])

model = LogisticRegression()
model.fit(X_train, y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        income = float(request.form['income'])
        credit_score = float(request.form['credit_score'])
        loan_amount = float(request.form['loan_amount'])
        employment_status = float(request.form['employment_status'])

        features = np.array([[income, credit_score, loan_amount, employment_status]])
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][prediction]

        if prediction == 1:
            prediction_text = f"Congratulations! Your loan is APPROVED. (Confidence: {probability:.2%})"
            is_approved = True
        else:
            prediction_text = f"We regret to inform you that your loan is REJECTED. (Confidence: {probability:.2%})"
            is_approved = False

        return render_template('index.html', prediction_text=prediction_text, is_approved=is_approved)
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error in prediction: {str(e)}", is_approved=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
