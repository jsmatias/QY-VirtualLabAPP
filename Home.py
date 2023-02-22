import streamlit as st

st.set_page_config(
    page_title="UCNPs virtual lab",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("UCNPs Virtual Lab (Beta)")
st.markdown("""
---
This app was developed for sharing data regarding studies on the internal quantum yield of UCNPs.
For more information on the mathematical modelling check the following paper: (Coming soon!)

This is a virtual lab to test how different parameters of UCNP compounds affect
the population densities, luminescence and internal quantum yield of the energy levels of the rare-earth elements embedded in the host matrix.

Navigate to the `simulation` tab in the sidebar and play with the parameters available there.

Enjoy! 
""")
