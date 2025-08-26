# SMS Spam Detection

A machine learning project that classifies text messages as Spam or Ham (Not Spam) using CountVectorizer and Multinomial Naive Bayes. The model is trained on a labeled SMS dataset and achieves 98% accuracy.

# 📂 Project Structure
sms-spam-detection/
│
├── app.py                # Main script (Streamlit or console app)
├── model.pkl             # Trained spam detection model
├── vectorizer.pkl        # CountVectorizer for text transformation
├── dataset.csv           # (Optional) Original dataset
├── requirements.txt      # Required dependencies
└── README.md             # Project description and usage


⚙️ Installation
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/sms-spam-detection.git
cd sms-spam-detection

2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows

3. Install dependencies
pip install -r requirements.txt

🚀 Usage
Run the Streamlit app
streamlit run app.py


Then open the link in your browser (usually http://localhost:8501).

📊 Model Details

Algorithm: Multinomial Naive Bayes

Feature Extraction: CountVectorizer

Accuracy: ~98% on test data

📌 Example Predictions
Input Message	Prediction
"Win a free iPhone by clicking this link!"	Spam
"Are we still meeting for lunch today?"	Ham
🤝 Contributing

Feel free to fork this project, open issues, or submit pull requests to improve the code.

📜 License

This project is licensed under the MIT License.
