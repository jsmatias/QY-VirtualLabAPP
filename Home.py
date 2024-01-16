import streamlit as st
from PIL import Image
from datetime import date

st.set_page_config(
    page_title="UC virtual lab",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

sidebarImg = Image.open('imgs/sidebar-0.png')
panelImg = Image.open('imgs/panel-1.png')
transitionPointsImg = Image.open('imgs/panel-2.png')
dataImg = Image.open('imgs/panel-3.png')
citation = f"""
@article{{jsmatias2023,
  author = {{Matias, J. S. and Komolibus, K. and Kho, K. W. and Konugolu-Venkata-Sekar, S. and Andersson-Engels, S.}},
  title = {{Generalised analytical model of the transition power densities of the upconversion luminescence and quantum yield}},
  year = {{2023}},
  volume = {{5}},
  issue = {{12}},
  pages = {{3279-3286}},
  publisher ={{RSC}},
  doi = {{10.1039/D2NA00850E}},
  note = {{Accessed: """ + f"{date.today().strftime('%m/%d/%Y')}}}" + "\n}"

st.title("Upconversion Virtual Lab")
st.markdown("""
---
## Description

Welcome to our Virtual lab for Upconversion (UC).
Our app is based on a simple general analytical model that introduces
the concept of transition power density points, $\\rho_j$, and QY saturation, $\eta_{sj}$, to characterise the internal Quantum Yield (iQY)
of an UC process originated from an arbitrary $| j \\rangle$ state.
This model is particularly useful for understanding the non-linear power density dependence present in upconverting systems, such as
Upconverting Nanoparticle (UCNPs), which are important for several applications, such as living tissue imaging and super-resolution microscopy.

The general analytical model was derived from a set of rate equation that comprises energy transfer, $W_j$, and linear decay rates, $R_j$, of the electronic
states of sensitizer-activator pair involved in the process called energy transfer upconversion (ETU).
Please check our scientific paper for more details regarding it ([Link to be placed here], DOI:).

Our app allows users to interactively explore the behaviour of the iQY of a upconverting system (a two-level sensitizer coupled to a four-level activator)
under different excitation power densities. Users can change the values of the input parameters of the model and see the
corresponding iQY values and UC luminescence and population densities graphs on the screen.
The app is capable of simulating ETU processes with order higher than two, which has not been widely studied in the literature up to the publishing date
of the paper.

We believe that our web app will be a valuable tool for researchers and scientists interested in studying UCNPs
and the understanding of their behaviour under different excitation conditions.
We hope you find our app useful and informative, and we welcome any feedback or suggestions for improvement.

---

## Usage

To explore the simulation, simply navigate to the "Simulation" tab in the sidebar on the left.
From there, you can adjust the input parameters and observe how they influence the population densities of the energy states,
which in turn affect the UC luminescence and iQY results.

Use the slider to adjust the excitation power density and input boxes to change the decay and energy transfer rates
of the energy levels involved in the UC process.
""")

st.image(sidebarImg, width=350, caption="Parameters in the sidebar. 1. Expand to change the parameters of the sensitizer and activator. 2. Change the values in the input box or use the slider to change the power density range. 3. You can download adjusted parameter as a CSV file.")

st.markdown("""
As you change the parameters, the simulation will automatically update the population densities and the resulting luminescence and iQY values.
You can also observe the changes in real-time on the corresponding graphs.
""")

st.image(panelImg, width=800,
         caption="Panel with the plotted results. You can switch between the population density, luminescence and quantum yield views.")

st.markdown("""
At the "Details" tab you can find the calculated transitions points and the iQY saturation levels.
""")

st.image(transitionPointsImg, width=400,
         caption="Transition points and iQY saturation levels.")

st.markdown("""
In the "Details" tab you can also download the generated data corresponding to the input parameters as a CSV file.
""")

st.image(dataImg, width=800, caption="Data and download button.")

st.markdown("""
By exploring the simulation, you can gain insights into the behaviour of upconverting materials under different excitation conditions
and better understand the relationship between the input parameters and the resulting luminescence and iQY values.

---

## Licence and citation
The source code of this project is publicly available on GitHub [https://github.com/jsmatias/QY-VirtualLabAPP](https://github.com/jsmatias/QY-VirtualLabAPP).
This app is licensed under the MIT License, which allows for unrestricted use, distribution, and modification of the software.
If you use this app in your research or other work, we kindly ask that you cite us as follows:
""")

st.code(citation)

st.markdown("""
By citing this app, you help us to continue developing and improving it for the benefit of the scientific community. Thank you!

---

## Contributing

We believe that collaborative development is the key to improvement, and we welcome any contributions you may have to offer.
To get started, please take a look at our issue tracker of source code on GitHub to see if there are any tasks that you're interested in tackling.
If you have an idea for a new feature or improvement, please feel free to open a new issue so that we can discuss it.

Before making a pull request, please make sure that your code follows our code style guidelines and that all tests pass successfully.
We appreciate well-documented code and encourage you to write clear, concise comments that will help others understand your contributions.

---

## Acknowledgements

This app was developed by Jean Matias as part of his PhD in Biophotonics at Tyndall National Institute - Ireland.
Part of the text in this page was generated with the help of ChatGPT v. Feb 13.

This project was funded by Science Foundation Ireland (SFI/15/RP/2828).

---
""")
