import streamlit as st

from pages.src.sidebar import *
from pages.src.display import *
from pages.src.etumodel import getData, getTransitionPoints

st.title("UCNP virtual lab (Beta)")

st.markdown("---")

userInput = sidebar()

data = getData(userInput)
transitionPoints = getTransitionPoints(userInput)

chartPanel(data, transitionPoints)
