import streamlit as st
import pickle
import pandas as pd

def main():
    st.title("Heart Attack Prediction Tool :hearts:")

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    .stApp {
        background-color: #fafafa; /* Lighter shade for the background */
        font-family: 'Roboto', sans-serif;
    }

    h1 {
        color: #db3a34; /* A heart-themed color for headings */
        font-weight: 700;
    }

    .stSelectbox .css-2b097c-container {
        border-radius: 20px; /* Rounded corners for select boxes */
        background-color: #fff;
        border: 1px solid #eee;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
    }

    .stButton > button {
        border-radius: 20px;
        border: none;
        color: white;
        background-color: #db3a34; /* Matching button color to the theme */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        font-size: 16px;
        padding: 10px 24px;
    }

    .stButton > button:hover {
        background-color: #c5302c; /* Slightly darker shade on hover */
    }

    .stSlider .css-1e3tf61-EmotionIconBase {
        color: #db3a34; /* Themed color for slider icon */
    }
    
    /* Additional responsive design tweaks can be added here */

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .stApp {
        background-color: #ffe5e5;
    }
    .content {
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Attempt to load the pre-trained model
    model = None
    try:
        base_path = "NoteBook/Deploying_Strimlit/final_model.pkl"
        model = pickle.load(open(base_path, 'rb'))
    except Exception as e:
        st.error(f"Failed to load the model: {e}")
        return

    if model:
        # Define mappings for categorical inputs
        age_category_options = ['Young Adults (18-39)', 'Middle-aged Adults (40-59)', 
                                'Senior Adults (60-79)', 'Elderly (80 and older)']
        smoker_status_options = ['Never smoked', 'Former smoker', 'Current smoker - now smokes every day', 'Current smoker - now smokes some days']
        general_health_options = ['Excellent', 'Very good', 'Good', 'Fair', 'Poor']
        last_checkup_options = ['Within past year', 'Within past 2 years', 'Within past 5 years', '5 or more years ago']
        race_options = ['White only, Non-Hispanic', 'Hispanic', 'Black only, Non-Hispanic', 
                        'Other race only, Non-Hispanic', 'Multiracial, Non-Hispanic']

        age_category = st.selectbox('Age Category:', options=age_category_options)
        smoker_status = st.selectbox('Smoking status:', options=smoker_status_options)
        general_health = st.selectbox('General health:', options=general_health_options)
        last_checkup = st.selectbox('Last checkup:', options=last_checkup_options)
        race_ethnicity = st.selectbox('Race/Ethnicity:', options=race_options)
        sex = st.radio('Gender:', options=['Female', 'Male'])
        had_angina = st.radio('Have you ever had angina?', ['No', 'Yes'])
        physical_activities = st.radio('Are you physically active?', ['No', 'Yes'])
        had_stroke = st.radio('Have you ever had a stroke?', ['No', 'Yes'])
        had_diabetes = st.radio('Do you have diabetes?', ['No', 'Yes'])
        had_depressive_disorder = st.radio('Have you ever had a depressive disorder?', ['No', 'Yes'])
        had_copd = st.radio('Have you ever had COPD?', ['No', 'Yes'])
        had_kidney_disease = st.radio('Have you ever had kidney disease?', ['No', 'Yes'])
        had_arthritis = st.radio('Have you ever had arthritis?', ['No', 'Yes'])
        physical_health_days = st.slider('Physical health days:', 0, 30, 0)
        sleep_hours = st.slider('Hours of sleep:', 1, 12, 8)
        bmi = st.slider('Select the estimated BMI:', 10.0, 50.0, 25.0)
        st.latex(r'''\text{BMI} = \frac{\text{weight (kg)}}{\text{height (m)}^2}''')

        inputs = {
            'remainder__HadAngina': int(had_angina == 'Yes'),
            'remainder__PhysicalHealthDays': physical_health_days,
            'remainder__PhysicalActivities': int(physical_activities == 'Yes'),
            'remainder__HadStroke': int(had_stroke == 'Yes'),
            'remainder__HadDiabetes': int(had_diabetes == 'Yes'),
            'remainder__SmokerStatus': smoker_status_options.index(smoker_status),
            'remainder__GeneralHealth': general_health_options.index(general_health),
            'remainder__SleepHours': sleep_hours,
            'remainder__HadDepressiveDisorder': int(had_depressive_disorder == 'Yes'),
            'remainder__HadCOPD': int(had_copd == 'Yes'),
            'remainder__HadKidneyDisease': int(had_kidney_disease == 'Yes'),
            'remainder__HadArthritis': int(had_arthritis == 'Yes'),
            'remainder__LastCheckupTime': last_checkup_options.index(last_checkup),
            'remainder__Sex': 1 if sex == 'Female' else 0,
            'remainder__AgeCategory': age_category_options.index(age_category),
            'remainder__BMI': bmi
        }

        if st.button('Predict'):
            input_df = pd.DataFrame([inputs])
            race_ohe = pd.get_dummies(pd.Series([race_ethnicity]), prefix='cat__RaceEthnicityCategory')
            input_df = pd.concat([input_df, race_ohe], axis=1)
            input_df.fillna(0, inplace=True)

            expected_columns = ['cat__RaceEthnicityCategory_Black only, Non-Hispanic', 
                                'cat__RaceEthnicityCategory_Hispanic', 'cat__RaceEthnicityCategory_Multiracial, Non-Hispanic', 
                                'cat__RaceEthnicityCategory_Other race only, Non-Hispanic', 
                                'cat__RaceEthnicityCategory_White only, Non-Hispanic', 
                                'remainder__HadAngina', 'remainder__PhysicalHealthDays', 
                                'remainder__PhysicalActivities', 'remainder__HadStroke', 
                                'remainder__HadDiabetes', 'remainder__SmokerStatus', 
                                'remainder__GeneralHealth', 'remainder__SleepHours', 
                                'remainder__HadDepressiveDisorder', 'remainder__HadCOPD', 
                                'remainder__HadKidneyDisease', 'remainder__HadArthritis', 
                                'remainder__LastCheckupTime', 'remainder__Sex', 
                                'remainder__AgeCategory', 'remainder__BMI']
            for col in expected_columns:
                if col not in input_df.columns:
                    input_df[col] = 0

            try:
                predicted_class = model.predict(input_df)
                probabilities = model.predict_proba(input_df)
                probability_yes = probabilities[0][1]
                
                st.success(f'The predicted class is: {predicted_class[0]}')
                st.success(f'The predicted probability of having a heart attack is: {probability_yes:.2%}')

                health_tips = []
                if had_angina == 'Yes':
                    health_tips.append("Having angina can significantly increase your heart risk. Regular check-ups and following your doctor's advice are crucial.")
                if had_stroke == 'Yes':
                    health_tips.append("A history of stroke can increase your chances of a heart attack. Monitoring blood pressure and avoiding smoking can help reduce risk.")
                if had_diabetes == 'Yes':
                    health_tips.append("Managing diabetes is important for heart health. A balanced diet low in sugar and regular exercise can help control blood sugar levels.")
                if had_copd == 'Yes':
                    health_tips.append("COPD can put a strain on your heart. Avoiding tobacco smoke and getting vaccinated for flu can be beneficial.")
                if had_kidney_disease == 'Yes':
                    health_tips.append("Kidney disease can increase heart attack risk. Maintaining a healthy blood pressure and following your treatment plan are key.")
                if had_arthritis == 'Yes':
                    health_tips.append("Some forms of arthritis can increase cardiovascular risk. Regular physical activity and weight management may help reduce it.")
                if sleep_hours < 6:
                    health_tips.append("Sleeping less than 6 hours can increase heart disease risk. Aim for 7-9 hours of quality sleep per night.")
                if bmi > 25:
                    health_tips.append("A BMI over 25 is linked to higher heart health risks. A diet rich in fruits, vegetables, and whole grains along with regular physical activity can help in weight management.")

                if health_tips:
                    st.warning("Health Tips:")
                    for tip in health_tips:
                        st.info(tip)

            except Exception as e:
                st.error(f"Error making prediction: {e}")

if __name__ == "__main__":
    main()
