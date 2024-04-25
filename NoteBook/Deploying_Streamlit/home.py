import streamlit as st

def main():
    # Apply custom styles
    st.markdown("""
    <style>
    .title-font {
        font-size: 40px; /* Increase the font size for a more prominent title */
        font-weight: bold;
        color: #2F4F4F; /* Dark Slate Gray */
        text-align: center;
        margin-bottom: 0; /* Reduce space below the title */
    }
    .header-font {
        font-size: 22px; /* Slightly smaller font for the header for better hierarchy */
        font-weight: normal; /* Less emphasis on the header font weight */
        color: #2F4F4F; /* Dark Slate Gray */
        text-align: center;
        margin-top: 0; /* Reduce space above the header */
    }
    .subheader-font {
        font-size: 20px;
        font-weight: bold;
        color: #2F4F4F;
        text-align: center;
    }
    .content-font {
        font-size: 18px;
        color: #2F4F4F;
        text-align: center;
    }
    .list-font {
        font-size: 16px;
        color: #2F4F4F;
    }
    .title-box {
        background-color:#C7DCFF;
        padding: 15px;
        border-radius: 10px;
        margin: 25px 0 10px 0; /* Adjusted margin for tighter spacing */
    }
    .header-box {
        background-color: #D9D7FF;
        padding: 15px;
        border-radius: 10px;
        margin: 0 0 20px 0; /* Adjusted margin for tighter spacing */
    }
    .risk-factors-box {
        background-color: #FFD6CC;
        padding: 10px;
        border-radius: 10px;
        margin: 20px 0;
    }
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
    st.markdown('<div class="title-box title-font">Heart Health Analysis Tool</div>', unsafe_allow_html=True)
    st.markdown('<div class="header-box header-font">Heart attacks are serious medical emergencies that occur when the supply of blood to the heart is suddenly blocked, typically by a blood clot.</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader-font">Several factors can increase your risk of having a heart attack:</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="risk-factors-box list-font">
                
    - Lifestyle factors such as <strong>smoking, high-fat diet, and lack of exercise</strong>.
                
    - Conditions like <strong>high blood pressure, cholesterol, diabetes, and obesity</strong>.
                
    - Family history of <strong>heart disease, age, and previous heart attacks or strokes</strong>.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="content-font">This tool aims to help you understand the likelihood of having a heart attack based on your health and lifestyle inputs. Please navigate to the Prediction page to use the tool.</div>', unsafe_allow_html=True)

    # Adjust image path and width as necessary
    st.image("/Users/asalzooashkiany/Downloads/doctor.webp", width=700)  # Corrected the width argument

if __name__ == "__main__":
    main()
