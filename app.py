import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('T:/prepleaf/project/ML_2/model.pkl', 'rb'))

def loan_status_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Loan Application accepted'
        
    else:
      return 'Loan Application rejected'


def main():

    st.title('Loan Application Status ')

    st.markdown("#### Gender")
    gender = st.selectbox("Choose the Gender ",("Male","Female"))
    if gender == "Male":
        gender_type = 1
    elif gender == 'Female':
        gender_type = 0


    st.markdown("#### Education")
    education = st.selectbox("Choose the Gender ",("Graduated","Non Graduate"))
    if education == "Graduated":
        education_type = 1
    elif education == 'Non Graduate':
        education_type = 0



    st.markdown("#### Marriage status")
    married = st.selectbox("Choose the Married Status ",("Married","Unmarried"))
    if married == "Married":
        married_type = 1
    elif married == 'Unmarried':
        married_type = 0


    st.markdown("#### No. of dependents")
    dependents = st.selectbox("Choose the number of Dependents", [0,1,2,3])



    st.markdown("#### Self Employed")
    Self_employed = st.selectbox("Is he/she self employed ",("Yes","No"))
    if Self_employed == "Yes":
        Self_employed_type = 1
    elif Self_employed == 'No':
        Self_employed_type = 0


    st.markdown("#### Applicant Income")
    app_income = st.text_input("",value="0")
    app_income = int(app_income)

    st.markdown("#### Co Applicant Income")
    co_app_income = st.text_input("",value="1")
    co_app_income = int(co_app_income)

    st.markdown("#### Loan Amount")
    loan_amt = st.text_input("",value="2")
    loan_amt = int(loan_amt)

    st.markdown("#### Loan amount term in months")
    loan_amt_term = st.text_input("",value="3")
    loan_amt_term = int(loan_amt_term)

    st.markdown("#### Credit History")
    Credit = st.selectbox("Is there credit history ",("Yes","No"))
    if Credit == "Yes":
        Credit_type = 1
    elif Credit == 'No':
        Credit_type = 0

    st.markdown("#### Property area")
    area = st.selectbox("Area ",("Urban","Semi-urban","Rural"))
    if area == "Urabn":
        area_type = 2
    elif area == 'Semi-urban':
        area_type = 1
    elif area == 'Rural':
        area_type = 0

    output = ''


    if st.button("Loan Status Prediction"):
        output = loan_status_prediction([gender_type,married_type,dependents,education_type,Self_employed_type,app_income,co_app_income,loan_amt,loan_amt_term,Credit_type,area_type])
        final_output = output * 100
        st.success(output)
        #st.header('Probability of application accepting is {}% '.format(final_output))

        #if final_output > 50:
         #   st.error("Accepted")
        #else:
         #   st.success("Rejected")
             

if __name__=='__main__':
    main()


    

    








    
    
