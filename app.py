import pickle
import streamlit as st

# Loading the model to predict on the data
pickle_in = open('Customer_Churn.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
    return 'Welcome to the best AI for predicting features that affect customer churn'

def preprocess_user_input(user_data):
    # Convert categorical variables to numerical format if needed (e.g., using label encoding)
    for key in user_data:
        if user_data[key] == "Yes" or user_data[key] == "Month-to-month" or user_data[key] == "Electronic check":
            user_data[key] = 1
        elif user_data[key] == "No" or user_data[key] == "One year" or user_data[key] == "Mailed check":
            user_data[key] = 0
        else:
            user_data[key] = 2
    return user_data

# Defining the function which will make the prediction using
# the data which the user inputs
def prediction(user_data):
    # Make sure to preprocess the input data in a way consistent with how the model was trained
    # For example, you might need to encode categorical variables or scale numerical features.
    prediction = classifier.predict([user_data])
    return prediction

# This is the main function in which we define our webpage
def main():
    # Giving the webpage a title
    st.title("Customer Churn Prediction")
    
    # Front-end elements
    st.markdown(
        """
        <style>
            .main {
                background-color: #f4f4f4;
                padding: 20px;
                border-radius: 10px;
            }
            h1 {
                color: #0071bc;
                text-align: center;
            }
            .btn {
                background-color: #0071bc;
                color: #ffffff;
                padding: 8px 15px;
                border-radius: 5px;
                margin-top: 10px;
                display: inline-block;
            }
        </style>
        """, 
        unsafe_allow_html=True
    )

    # Main content with a background color and padding
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    
    # HTML template for the header
    html_temp = """ 
    <div style ="background-color:darkblue;padding:13px"> 
        <h1 style ="color:gold;text-align:center;">Streamlit Best Customer Churn Prediction App </h1> 

    </div> 
    """
    
    # Displaying the HTML template for the header
    st.markdown(html_temp, unsafe_allow_html=True)

    # User input
    gender = st.selectbox("Select Gender of the customer:", ["Male", "Female"])
    partner = st.selectbox("Select 'Partner' status:", ["Yes", "No"])
    dependents = st.selectbox("Select 'Dependents' status:", ["Yes", "No"])
    phone_service = st.selectbox("Select 'PhoneService' status:", ["Yes", "No"])
    multiple_lines = st.selectbox("Select 'MultipleLines' status:", ["Yes", "No", "No phone service"])
    internet_service = st.selectbox("Select 'InternetService' type:", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Select 'OnlineSecurity' status:", ["Yes", "No", "No internet service"])
    online_backup = st.selectbox("Select 'OnlineBackup' status:", ["Yes", "No", "No internet service"])
    device_protection = st.selectbox("Select 'DeviceProtection' status:", ["Yes", "No", "No internet service"])
    tech_support = st.selectbox("Select 'TechSupport' status:", ["Yes", "No", "No internet service"])
    streaming_tv = st.selectbox("Select 'StreamingTV' status:", ["Yes", "No", "No internet service"])
    streaming_movies = st.selectbox("Select 'StreamingMovies' status:", ["Yes", "No", "No internet service"])
    contract = st.selectbox("Select 'Contract' type:", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Select 'PaperlessBilling' status:", ["Yes", "No"])
    payment_method = st.selectbox("Select 'PaymentMethod':", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    monthly_charges = st.number_input("Enter the monthly charges:", min_value=0, max_value=100000, value=0)
    total_charges = st.number_input("Enter the total charges:", min_value=0, max_value=100000, value=0)


    # Create a dictionary with the user input
    user_data = {
        'Gender': gender,
        'Partner': partner,
        'Dependents': dependents,
        'PhoneService': phone_service,
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contract,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method, 
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges
    }


    # Preprocess user input
    user_data = preprocess_user_input(user_data)

    result = ""

    # Making the prediction
    if st.button("Predict", key="predict_button"):
        result = prediction(list(user_data.values()))

    # Displaying the result
    st.markdown(f"The predicted result is: **{result}**", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
