import streamlit as st

from pages.src.sidebar import *
from pages.src.display import *
from pages.src.etumodel import getData, getTransitionPoints

st.set_page_config(
    page_title="UCNPs virtual lab",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("UCNP virtual lab (Beta)")

st.markdown("---")

userInput = sidebar()

data = getData(userInput)
transitionPoints = getTransitionPoints(userInput)

chartPanel(data, transitionPoints)
