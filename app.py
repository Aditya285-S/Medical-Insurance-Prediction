import streamlit as st
import pandas as pd
import numpy as np
from model import model

st.set_page_config(page_title="medical-insurance-cost-prediction")

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:20px;margin-bottom:30px">
    <h2 style="color:black;text-align:center"> Medical Insurance Cost Prediction</h2>
    </div>
    """
    
    def generate_random_policy(model):
        random_values = {
            'age': np.random.randint(age, age+15),
            'sex': g1,
            'bmi': np.random.uniform(bmi-5, bmi+5),
            'smoker': g2,
            'region': np.random.randint(g3-1, g3+2),
            'children': np.random.randint(children-1, children+1)
        }

        charges = model.predict([list(random_values.values())])[0]
        random_values['charges'] = charges.round(0)

        return random_values

    df = pd.read_csv('insurance.csv')

    st.markdown(html_temp, unsafe_allow_html=True)

    age = st.slider("Enter your age", 18, 100)
    gender = st.selectbox("Gender", ('Male', 'Female'), index=None, placeholder="Select the Gender...")

    if gender == 'Male':
        g1 = 0
        gender = 'male'
    else:
        g1 = 1
        gender = 'female'

    bmi = st.number_input("Enter your BMI", value=None, placeholder="BMI")
    children = st.slider("Number of children", 0, 5)
    smoke = st.selectbox("Did you smoke", ('No', 'Yes'), index=None, placeholder="Select...")

    if smoke == 'Yes':
        g2 = 0
        smoke = 'yes'
    else:
        g2 = 1
        smoke = 'no'

    region = st.selectbox('Region', ('Southwest', 'Southeast', 'Northwest', 'Northeast'), index=None,
                          placeholder="Select the Region...")

    if region == 'Southwest':
        g3 = 1
        region = 'southwest'
    elif region == 'Southeast':
        g3 = 2
        region = 'southeast'
    elif region == 'Northwest':
        g3 = 3
        region = 'northwest'
    else:
        g3 = 4
        region = 'northeast'

    button = st.button('Predict')

    if button:
        pred = model.predict([[age, g1, bmi, g2, g3, children]])

        st.success('Your Insurance Cost is {}'.format(round(pred[0], 2)))

        new_data = {'age': age, 'sex': gender, 'bmi': bmi, 'smoker': smoke, 'region': region, 'children': children,
                    'charges': round(pred[0], 4)}
        new_df = pd.DataFrame([new_data])  # Create a new DataFrame with a single row

        df = pd.concat([df, new_df], ignore_index=True)

        df.to_csv('insurance.csv', index=False)

        # Generate and display random insurance policies
        st.subheader('Insurance Policy Suggestions:')
        num_suggestions = 10
        # categories = {'sex': g1, 'smoker': g2, 'region': g3}
        random_policies = [generate_random_policy(model) for _ in range(num_suggestions)]

        random_policies_df = pd.DataFrame(random_policies)
        random_policies_df['sex']=random_policies_df['sex'].map({0:'male' , 1:'female'})
        random_policies_df['smoker']=random_policies_df['smoker'].map({0:'yes' , 1:'no'})
        random_policies_df['region']=random_policies_df['region'].map({0:'southwest' , 1:'southwest' , 2:'southeast' , 3:'northwest' , 4:"northeast"})
        st.table(random_policies_df)

if __name__ == "__main__":
    main()
