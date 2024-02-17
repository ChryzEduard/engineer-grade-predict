import streamlit as st
import pickle
import numpy as np


def load_eng_model():
    with open("rf_student_model2.pkl", "rb") as file:
        eng_model = pickle.load(file)
    return eng_model

load_eng_model()