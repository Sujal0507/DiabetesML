import pickle
import streamlit as st
import numpy as np
import requests

# Load trained model
loaded_model = pickle.load(open('C:/Users/Sujal Patel/trained_model.sav', 'rb'))

# Prediction function
def diabetes_prediction(input_data):
    input_data_np = np.asarray(input_data).reshape(1, -1)
    prediction = loaded_model.predict(input_data_np)
    return '🩺 The person is diabetic' if prediction[0] == 1 else '✅ The person is not diabetic'

# Load Lottie animation from URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Streamlit app
def main():
    st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="wide")

    # Top image (centered and resized)
   # st.markdown("""
        #<div style="text-align: center;">
          ##  <img src="https://cdn.pixabay.com/photo/2019/11/03/20/33/raspberry-4599580_1280.jpg" 
#                 alt="top image" width="250" style="border-radius: 15px; margin-bottom: 10px;">
 #       </div>
  #   """, unsafe_allow_html=True)

    # Title
    st.markdown("""
        <h1 style='text-align: center; color: #2E86C1; font-size: 50px;'>Diabetes Prediction ML Project</h1>
        <div style='text-align: center; font-size: 18px; margin-bottom: 30px;'>
            Fill out the form below with health details to check for diabetes risk.
        </div>
    """, unsafe_allow_html=True)

    # Form header
    st.markdown("<div style='text-align: center; font-size: 20px;'><b>Enter Health Metrics</b></div><br>", unsafe_allow_html=True)

    # Two-column form
    col1, col2 = st.columns([1, 1])
    with col1:
        Pregnancies = st.text_input('👶 Number of pregnancies')
        Glucose = st.text_input('🍬 Glucose level')
        BloodPressure = st.text_input('💉 Blood pressure')
        SkinThickness = st.text_input('🧪 Skin Thickness')
    with col2:
        Insulin = st.text_input('🩸 Insulin level')
        BMI = st.text_input('⚖️ BMI (Body Mass Index)')
        DiabetesPedigreeFunction = st.text_input('🧬 Diabetes Pedigree Function')
        Age = st.text_input('🎂 Age')

    # Load result animation
    lottie_success_url = "https://assets10.lottiefiles.com/packages/lf20_jbrw3hcz.json"
    lottie_success = load_lottie_url(lottie_success_url)

    # Spacer
    st.markdown("<br>", unsafe_allow_html=True)

    # Centered Predict button with adjusted width
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        predict_btn = st.button("🔍 Predict", use_container_width=False)  # Set container_width to False for compact button

    # Prediction and animation logic
    diagnosis = ""
    if predict_btn:
        try:
            inputs = [
                float(Pregnancies or 0),
                float(Glucose or 0),
                float(BloodPressure or 0),
                float(SkinThickness or 0),
                float(Insulin or 0),
                float(BMI or 0),
                float(DiabetesPedigreeFunction or 0),
                float(Age or 0)
            ]
            diagnosis = diabetes_prediction(inputs)

            # Stylish result
            st.markdown(f"""
                <style>
                .result {{
                    text-align: center;
                    font-size: 30px;
                    font-weight: bold;
                    color: #0077b6;
                    animation: fadeIn 1s ease-in-out;
                }}
                @keyframes fadeIn {{
                    from {{ opacity: 0; }}
                    to {{ opacity: 1; }}
                }}
                </style>
                <div class="result">{diagnosis}</div>
            """, unsafe_allow_html=True)

            # Show animation after result
            if lottie_success:
                st_lottie(lottie_success, height=250, key="result-animation")

            # Show right logo (only after prediction)
            st.markdown("""
                <div style="text-align: center; margin-top: 30px;">
                    <img src="https://cdn.pixabay.com/photo/2014/11/12/19/25/diabetes-528678_1280.jpg" 
                         alt="bottom image" width="250" style="border-radius: 15px;">
                </div>
            """, unsafe_allow_html=True)

        except ValueError:
            st.warning("⚠️ Please enter valid numeric values for all fields.")

# Run app
if __name__ == '__main__':
    main()
