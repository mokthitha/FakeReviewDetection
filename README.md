# Fake Review Detection using Machine Learning & Blockchain

📌 Project Description

This project detects whether a product review is fake or real using Machine Learning techniques. It uses Natural Language Processing (NLP) to analyze review text and classify it. Additionally, Blockchain technology is used to securely store predictions, ensuring transparency and data integrity.

---

🚀 Features

- Detects fake vs real reviews using ML model
- Converts text into numerical features using TF-IDF
- Trains a classification model using Logistic Regression
- Predicts new review authenticity
- Stores predictions securely using Blockchain
- Ensures tamper-proof record of reviews

---

🛠️ Tech Stack

- Python
- pandas
- scikit-learn
- hashlib (for blockchain hashing)
- datetime

---

⚙️ How It Works

1. Load dataset containing reviews and labels
2. Extract review text and corresponding labels
3. Convert text into numerical vectors using TF-IDF
4. Split data into training and testing sets
5. Train model using Logistic Regression
6. Evaluate model accuracy
7. Predict whether a new review is fake or real
8. Store the review and prediction in a Blockchain

---

▶️ How to Run

pip install pandas scikit-learn
python app.py

---

📊 Sample Output

Model Accuracy: 0.87

Input Review:
"This product is amazing and worth every penny"

Prediction:
This review is REAL

Blockchain Record:
Index: 1
Review: This product is amazing and worth every penny
Prediction: REAL
Hash: <generated_hash>
Previous Hash: <previous_hash>

---

🔗 Blockchain Explanation

- Each review is stored as a block
- Each block contains:
  - Review text
  - Prediction (FAKE/REAL)
  - Timestamp
  - Hash
  - Previous block hash
- This ensures:
  - Data cannot be altered
  - Full traceability of predictions

---

📁 Project Structure

fake-review-detection/
│── model.py
│── fake reviews dataset.csv
│── README.md

---

📈 Model Details

- Algorithm: Logistic Regression
- Feature Extraction: TF-IDF Vectorizer
- Evaluation Metric: Accuracy Score

---

🔮 Future Improvements

- Use advanced models like Random Forest or BERT
- Improve accuracy with larger datasets
- Build a web interface using Streamlit
- Store blockchain data in distributed systems
- Add real-time review detection

---

💡 Conclusion

This project combines Machine Learning and Blockchain to detect fake reviews and securely store predictions, making it useful for e-commerce platforms to improve trust and reliability.

---
