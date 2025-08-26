import streamlit as st
import joblib
import re

# load the trained model and vectorizer

model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title("📱 SMS Spam Detection App")
st.write("Type a message below to check if it's spam or not.")

# input box

message = st.text_area('Enter your message here....')

if st.button('Check your message'):
    if message.strip():
        # clean the message 
        cleaned_message = re.sub('[^a-zA-Z]',' ',message).lower()
        transformed_message = vectorizer.transform([cleaned_message])


        prediction = model.predict(transformed_message)[0]
        probability = model.predict_proba(transformed_message)[0][prediction] *100

        if prediction == 1:
            st.error(f"🚨 Spam Detected! (Confidence: {probability:.2f}%)")
        
        else:
            st.success(f"✅ Not Spam (Confidence: {probability:.2f}%)")
    else:
        st.warning("Please type a message before predicting.")
