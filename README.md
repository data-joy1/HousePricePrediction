# HousePricePrediction
🚀 A machine learning-powered API to predict house prices based on square footage, bedrooms, and bathrooms.

#Features
🏠 Predicts house prices using Linear Regression.
🌍 Built with Flask for easy API integration.
📊 Simple input & JSON-based output

#Project structure
HousePricePrediction/
│── api/                     # Flask API
│   ├── app.py               # Main API file
│   ├── test_api.py          # Test script for API
│── notebooks/               # Model training
│   ├── train_model.py       # Training script
│── deployment/              # Saved model
│   ├── model.pkl            # Trained model
│── venv/                    # Virtual environment 
│── README.md                # Project documentation
│── requirements.txt         # Dependencies
│── Dockerfile               # Docker setup 

#installation and setup
1- clone repository
    git clone https://github.com/data-joy1/HousePricePrediction.git
    cd HousePricePrediction
    
2- Create a Virtual Environment
    python -m venv venv
    Activate it:
      Windows: venv\Scripts\activate
      Mac/Linux: source venv/bin/activate
      
3️- Install Dependencies
    pip install -r requirements.txt

4️- Train the Model
    python notebooks/train_model.py
    
5️-  Run the Flask API
    cd api
    python app.py

#Api Usage
1️- Home Route
📌 Check if API is working:
    curl http://127.0.0.1:5000/
✅ Response:
    Welcome to the House Price Prediction API!

2️- Predict House Price
📌 Send a POST request with house details:
    curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"sqft": 1800, "bedrooms": 3, "bathrooms": 2}'
✅ Response:
    {
  "predicted_price": 291288.08
    }



