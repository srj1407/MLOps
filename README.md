# Flask Loan Prediction App

A simple Flask web application that predicts loan eligibility using a scikit-learn Logistic Regression model, packaged with Docker for easy testing.

## Project Structure
```
flask-loan-app/
│
├── app.py              # Main Flask application & ML model training
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── templates/
│   └── index.html      # Frontend HTML form
└── README.md           # Instructions
```

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your browser and navigate to: `http://localhost:5000`

---

## Running with Docker

1. **Build the Docker image**:
   ```bash
   docker build -t flask-loan-app .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 5000:5000 flask-loan-app
   ```

3. Open your browser and navigate to: `http://localhost:5000`
