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



## EnglishProficiency	ReadingComprehenshion	ScienceProcessSkills	QuantitativeSkills	AbstractThinkingSkills	
## Vocabulary	Knowledge&Comprehenshion	AbstractReasoning	ComputationalSkill	LogicalReasoning



st.write("""
# College of Engineering
Prediction of Students Success in Engineering Board Exams
         """)

c1, c2 = st.columns(2)
with c1:
   st.write("### CET Results")
   English_Proficiency = st.number_input(
       "English Proficiency", # Input title
        min_value = 0.00,     # Minimum
        max_value = 100.00,    # Maximum
   )
   Reading_Comprehenshion = st.number_input(
       "Reading Comprehension", # Input title
        min_value = 0.00,       # Minimum
        max_value = 100.00      # Maximum
   )
   Science_Process_Skills = st.number_input(
       "Science Process Skills",    # Input title
        min_value = 0.00,           # Minimum
        max_value = 100.00          # Maximum
   )
   Quantitative_Skills = st.number_input(
       "Quantitative Skills",   # Input title
        min_value = 0.00,       # Minimum
        max_value = 100.00      # Maximum
   )
   Abstract_Thinking_Skills = st.number_input(
       "Abstract Thinking Skills",  # Input title
        min_value = 0.00,           # Minimum
        max_value = 100.00          # Maximum
   )
   # ep, rc, sps, qs, ats
   # v, kc, ar, cs, lr

with c2:    
   st.write("### EAT Results")
   Vocabulary = st.number_input(
       "Vocabulary",        # Input title
        min_value = 0.00,      # Minimum
        max_value = 100.00      # Maximum
   )
   Knowledge_and_Comprehenshion = st.number_input(
       "Knowledge & Comprehension", # Input title
        min_value = 0.00,              # Minimum
        max_value = 100.00              # Maximum
   )
   Abstract_Reasoning = st.number_input(
       "Abstract Reasoning", # Input title
        min_value = 0.00,       # Minimum
        max_value = 100.00       # Maximum
   )
   Computational_Skill = st.number_input(
       "Computational Skill", # Input title
        min_value = 0.00,        # Minimum
        max_value = 100.00        # Maximum
   )
   Logical_Reasoning = st.number_input(
       "Logical Reasoning", # Input title
        min_value = 0.00,      # Minimum
        max_value = 100.00      # Maximum
   )
Is_Regular = st.radio(   # CHANGE
     "Are you a regular student?",  # Input title
      ["Yes", "No"],                # Choices
 )

reg_data = 0.0

if Is_Regular == 'Yes':
    reg_data = 1.0
else:
    reg_data = 0.0



predict_call = st.button("Predict")

model = pickle.load(open("model.pkl", "rb"))
print(model)

# def load_eng_model():
#     with open("rf_student_model2.pkl", "rb") as file:
#         eng_model = pickle.load(file)
#     return eng_model


# dt_regressor_main = load_eng_model()

if predict_call:
    main_data_x = np.array([[English_Proficiency, Reading_Comprehenshion, Science_Process_Skills, Quantitative_Skills, Abstract_Thinking_Skills, Vocabulary, Knowledge_and_Comprehenshion, Abstract_Reasoning, Computational_Skill, Logical_Reasoning, reg_data]])


    # Make predictions
    main_predictions = model.predict(main_data_x)
    percent_prediction = main_predictions * 100
    st.subheader(f"Prediction is: {percent_prediction}%")