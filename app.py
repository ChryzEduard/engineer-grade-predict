import streamlit as st
import pickle
import numpy as np


from sklearn.ensemble import RandomForestRegressor
##dtree = DecisionTreeClassifier

st.set_page_config(
    menu_items = {},    
    page_title = "Engineering Prediction",
    page_icon = "book",
    layout = "wide",
)

def load_eng_model():
    with open("rf_eng_model.pkl", "rb") as file:
        eng_model = pickle.load(file)
    return eng_model


dt_regressor_main = load_eng_model()

## EnglishProficiency	ReadingComprehenshion	ScienceProcessSkills	QuantitativeSkills	AbstractThinkingSkills	
## Vocabulary	Knowledge&Comprehenshion	AbstractReasoning	ComputationalSkill	LogicalReasoning



st.write("""
# College of Engineering
Prediction of Students Success in Engineering Board Exams
         """)

c1, c2 = st.columns(2)
with c1:
   st.write("### CET Results")
   ep = st.number_input(
       "English Proficiency", # Input title
        min_value = 0.00,     # Minimum
        max_value = 100.00,    # Maximum
   )
   rc = st.number_input(
       "Reading Comprehension", # Input title
        min_value = 0.00,       # Minimum
        max_value = 100.00      # Maximum
   )
   sps = st.number_input(
       "Science Process Skills",    # Input title
        min_value = 0.00,           # Minimum
        max_value = 100.00          # Maximum
   )
   qs = st.number_input(
       "Quantitative Skills",   # Input title
        min_value = 0.00,       # Minimum
        max_value = 100.00      # Maximum
   )
   ats = st.number_input(
       "Abstract Thinking Skills",  # Input title
        min_value = 0.00,           # Minimum
        max_value = 100.00          # Maximum
   )
   # ep, rc, sps, qs, ats
   # v, kc, ar, cs, lr

with c2:    
   st.write("### EAT Results")
   voc = st.number_input(
       "Vocabulary",        # Input title
        min_value = 0,      # Minimum
        max_value = 100      # Maximum
   )
   kc = st.number_input(
       "Knowledge & Comprehension", # Input title
        min_value = 0,              # Minimum
        max_value = 100              # Maximum
   )
   ar = st.number_input(
       "Abstract Reasoning", # Input title
        min_value = 0,       # Minimum
        max_value = 100       # Maximum
   )
   cs = st.number_input(
       "Computational Skill", # Input title
        min_value = 0,        # Minimum
        max_value = 100        # Maximum
   )
   lr = st.number_input(
       "Logical Reasoning", # Input title
        min_value = 0,      # Minimum
        max_value = 100      # Maximum
   )
reg = st.radio(   # CHANGE
     "Are you a regular student?",  # Input title
      ["Yes", "No"],                # Choices
 )


if reg == 'Yes':
    reg = 1
else:
    reg = 0

predict_call = st.button("Predict")

if predict_call:
    main_data_x = np.array([[ep, rc, sps, qs, ats, voc, kc, ar, cs, lr, reg]])

    # Make predictions
    main_predictions = dt_regressor_main.predict(main_data_x)
    percent_prediction = main_predictions * 100
    st.subheader(f"Prediction is: {percent_prediction}%")