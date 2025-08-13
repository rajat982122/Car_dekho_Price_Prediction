# Car Price Prediction using Machine Learning

This project predicts the **price of used cars** based on various features such as model, age, mileage, engine capacity, and more.  
It uses **Random Forest Regression** trained on real-world car data from **CarDekho**.

---

## Features
- **Machine Learning Model:** Random Forest Regressor (best performance compared to Linear Regression, Ridge, Lasso, KNN, and Decision Tree).
- **Inputs:**
  - `model` (e.g., Alto, i20, Creta, etc.)
  - `vehicle_age` (in years)
  - `km_driven` (total kilometers driven)
  - `seller_type` (Individual, Dealer, Trustmark Dealer)
  - `fuel_type` (Petrol, Diesel, CNG, LPG, Electric)
  - `transmission_type` (Manual, Automatic)
  - `mileage` (in km/l or equivalent)
  - `engine` (in CC)
  - `max_power` (in BHP)
  - `seats` (number of seats)
- **Output:** Predicted car price.

---

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript  (HTML was not written by me)
- **Backend:** Flask (Python)
- **Machine Learning:** scikit-learn
- **Model Storage:** Pickle (`.pkl`) file

---

## Project Structure
├── application.py # Flask application
├── model.pkl # Trained Random Forest model
├── templates/ # HTML templates
│ └── index.html # Main input form
├── static/ # CSS, JS files
└── README.md # Project documentation
