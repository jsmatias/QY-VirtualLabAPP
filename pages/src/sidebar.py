import streamlit as st
import pandas as pd


def sidebar():
  class Values:
    # Sensitizer
    NS: float
    Rb: float
    crossSection: float
    # Activator
    NA: float
    RA: list
    RArad: list
    emissionWavelengths: list
    WA: list

    # Excitation config
    excitationWavelength: float
    powerDensRange: tuple

  st.sidebar.write("Parameters")

  # Sensitizer
  with st.sidebar.expander("Sensitizer"):

    st.caption("$N_A$ - Ground state population density [$cm^{-3}$]")
    # st.latex("N_0 [cm^{-3}]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.0, max_value=9.9, value=1.5, step=0.1, format="%.3f",
                          key='sens-pop-dens-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=0, max_value=30, value=21, step=1, format="%i",
                          key='sens-pop-dens-power', help=None, label_visibility="collapsed")
    Values.NS = x * 10 ** (y)

    st.markdown("---")

    st.caption(
      r"$R_b$ - Decay rate of the excited state $\left |b \right >$ [$s^{-1}$]")
    Values.Rb = st.number_input("Value", min_value=0.0, max_value=1e5, value=757.57, step=10.0, format="%g",
                                key='sens-decay-rate', help=None, label_visibility="collapsed")

    st.markdown("---")

    st.caption("$\sigma_S$ - Sensitizer's cross-section [$cm^2$]")
    # st.latex("N_0 [cm^{-3}]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.0, max_value=9.9, value=1.69, step=0.01, format="%.3f",
                          key='sens-cross-sect-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=-30, max_value=-10, value=-20, step=1, format="%i",
                          key='sens-cross-sect-power', help=None, label_visibility="collapsed")
    Values.crossSection = x * 10 ** (y)

  # Activator
  with st.sidebar.expander("Activator"):

    st.caption("$N_S$ - Ground state population density [$cm^{-3}$]")
    # st.latex("N_0 [cm^{-3}]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.0, max_value=9.9, value=1.27, step=0.1, format="%.3f",
                          key='act-pop-dens-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=0, max_value=30, value=19, step=1, format="%i",
                          key='act-pop-dens-power', help=None, label_visibility="collapsed")
    Values.NA = x * 10 ** (y)

    st.markdown("---")
    st.write("Non radiative decay rates")
    Values.RA = [None]
    st.caption("$R_1$ - Decay rate of the first energy state [$s^{-1}$]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.0, max_value=9.9, value=1.7, step=0.1, format="%.3f",
                          key='act-decay-rate-1-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=0, max_value=10, value=4, step=1, format="%i",
                          key='act-decay-rate-1-power', help=None, label_visibility="collapsed")
    Values.RA.append(x * 10 ** y)

    st.caption("$R_2$ - Decay rate of the second energy state [$s^{-1}$]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.0, max_value=9.9, value=1.0, step=0.1, format="%.3f",
                          key='act-decay-rate-2-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=0, max_value=10, value=5, step=1, format="%i",
                          key='act-decay-rate-2-power', help=None, label_visibility="collapsed")
    Values.RA.append(x * 10 ** y)

    st.caption("$R_3$ - Decay rate of the third energy state [$s^{-1}$]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.0, max_value=9.9, value=1.5, step=0.1, format="%.3f",
                          key='act-decay-rate-3-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=0, max_value=10, value=3, step=1, format="%i",
                          key='act-decay-rate-3-power', help=None, label_visibility="collapsed")
    Values.RA.append(x * 10 ** y)

    st.caption("$R_4$ - Decay rate of the fourth energy state [$s^{-1}$]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.0, max_value=9.9, value=1.5, step=0.1, format="%.3f",
                          key='act-decay-rate-4-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=0, max_value=10, value=3, step=1, format="%i",
                          key='act-decay-rate-4-power', help=None, label_visibility="collapsed")
    Values.RA.append(x * 10 ** y)

    # st.write(Values.RA)

    st.markdown("---")
    st.write("Radiative decay rates")
    Values.RArad = [None]
    st.caption(
      "$R^{rad}_1$ - Radiative decay rate of the first energy state [$s^{-1}$]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.0, max_value=9.9, value=0.0, step=0.1, format="%.3f",
                          key='act-rad-decay-rate-1-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=0, max_value=10, value=4, step=1, format="%i",
                          key='act-rad-decay-rate-1-power', help=None, label_visibility="collapsed")
    Values.RArad.append(x * 10 ** y)

    st.caption(
      "$R^{rad}_2$ - Radiative decay rate of the second energy state [$s^{-1}$]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.0, max_value=9.9, value=1.0, step=0.1, format="%.3f",
                          key='act-rad-decay-rate-2-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=0, max_value=10, value=3, step=1, format="%i",
                          key='act-rad-decay-rate-2-power', help=None, label_visibility="collapsed")
    Values.RArad.append(x * 10 ** y)

    st.caption(
      "$R^{rad}_3$ - Radiative decay rate of the third energy state [$s^{-1}$]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.0, max_value=9.9, value=1.5, step=0.1, format="%.3f",
                          key='act-rad-decay-rate-3-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=0, max_value=10, value=3, step=1, format="%i",
                          key='act-rad-decay-rate-3-power', help=None, label_visibility="collapsed")
    Values.RArad.append(x * 10 ** y)

    st.caption(
      "$R^{rad}_4$ - Radiative decay rate of the fourth energy state [$s^{-1}$]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.0, max_value=9.9, value=1.5, step=0.1, format="%.3f",
                          key='act-rad-decay-rate-4-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=0, max_value=10, value=3, step=1, format="%i",
                          key='act-rad-decay-rate-4-power', help=None, label_visibility="collapsed")
    Values.RArad.append(x * 10 ** y)

    st.markdown("---")
    Values.emissionWavelengths = [None]  # None for the 0 index
    st.write("Emission wavelengths")
    st.caption(
      "$\lambda_1$ - Emission wavelength from first excited state [$nm$]")
    Values.emissionWavelengths.append(
      st.number_input("Emission wavelength regarding the first excited energy state",
                      min_value=200.0, max_value=2000.0, value=1000.0, step=1.0, format="%.1f",
                      key='emission-wavelength-1', help="Insert a float number in nano-meters",
                      label_visibility="collapsed")
    )

    st.caption(
      "$\lambda_2$ - Emission wavelength from second excited state [$nm$]")
    Values.emissionWavelengths.append(
      st.number_input("Emission wavelength regarding the second excited energy state",
                      min_value=200.0, max_value=2000.0, value=804.0, step=1.0, format="%.1f",
                      key='emission-wavelength-2', help="Insert a float number in nano-meters",
                      label_visibility="collapsed")
    )

    st.caption(
      "$\lambda_3$ - Emission wavelength from third excited state [$nm$]")
    Values.emissionWavelengths.append(
      st.number_input("Emission wavelength regarding the third excited energy state",
                      min_value=200.0, max_value=2000.0, value=470.0, step=1.0, format="%.1f",
                      key='emission-wavelength-3', help="Insert a float number in nano-meters",
                      label_visibility="collapsed")
    )

    st.caption(
      "$\lambda_4$ - Emission wavelength from fourth excited state [$nm$]")
    Values.emissionWavelengths.append(
      st.number_input("Emission wavelength regarding the fourth excited energy state",
                      min_value=200.0, max_value=2000.0, value=450.0, step=1.0, format="%.1f",
                      key='emission-wavelength-4', help="Insert a float number in nano-meters",
                      label_visibility="collapsed")
    )

    st.markdown("---")

    Values.WA = []
    st.caption(
      "$W_0$ - Energy transfer rate from ground to first excited state [$s^{-1}$]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.0, max_value=9.9, value=1.6, step=0.1, format="%.3f",
                          key='et-rate-0-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=-30, max_value=0, value=-18, step=1, format="%i",
                          key='et-rate-0-power', help=None, label_visibility="collapsed")
    Values.WA.append(x * 10 ** y)

    st.caption(
      "$W_1$ - Energy transfer rate from first to second excited state [$s^{-1}$]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.0, max_value=9.9, value=6.2, step=0.1, format="%.3f",
                          key='et-rate-1-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=-30, max_value=0, value=-16, step=1, format="%i",
                          key='et-rate-1-power', help=None, label_visibility="collapsed")
    Values.WA.append(x * 10 ** y)

    st.caption(
      "$W_2$ - Energy transfer rate from second to third excited state [$s^{-1}$]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.0, max_value=9.9, value=1.52, step=0.1, format="%.3f",
                          key='et-rate-2-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=-30, max_value=0, value=-16, step=1, format="%i",
                          key='et-rate-2-power', help=None, label_visibility="collapsed")
    Values.WA.append(x * 10 ** y)

    st.caption(
      "$W_3$ - Energy transfer rate from third to fourth excited state [$s^-1$]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.0, max_value=9.9, value=1.52, step=0.1, format="%.3f",
                          key='et-rate-3-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=-30, max_value=0, value=-16, step=1, format="%i",
                          key='et-rate-3-power', help=None, label_visibility="collapsed")
    Values.WA.append(x * 10 ** y)

    st.caption(
      "$W_4$ - Energy transfer rate from fourth to fifth excited state [$s^-1$]")
    col1, col2, col3 = st.columns([10, 1, 8])
    with col1:
      x = st.number_input('Coefficient', min_value=0.00001, max_value=9.9, value=0.00001, step=0.1, format="%.3f",
                          key='et-rate-4-val', help=None, label_visibility="collapsed")
    with col2:
      st.write("E")
    with col3:
      y = st.number_input('Exponent', min_value=-30, max_value=0, value=-16, step=1, format="%i",
                          key='et-rate-4-power', help=None, label_visibility="collapsed")
    Values.WA.append(x * 10 ** y)

    # st.write(Values.WA)

  # Laser
  with st.sidebar.expander("Excitation config", expanded=True):

    st.caption("$\lambda$ - Wavelength [$nm$]")
    Values.excitationWavelength = st.number_input("", min_value=700.0, max_value=1000.0, value=976.0, step=1.0, format="%.1f",
                                                  key='excitation-wavelength', help="Excitation wavelength", label_visibility="collapsed")

    st.caption(r"$\rho$ - Power density range [$W/cm^2$]")
    Values.powerDensRange = st.slider(
      'Select a range of power densities [W/cm^2]',
      0.0, 100.0, (0.0, 50.0), label_visibility="collapsed"
    )

  # Export input vals to csv
  @st.cache_data
  def exportInputValuesToCsv(Vals):
    valsDict = dict((name, getattr(Vals, name))
                    for name in dir(Vals) if not name.startswith('__'))
    return (pd.Series(valsDict).to_csv())

  inputValsCsv = exportInputValuesToCsv(Values)
  st.sidebar.download_button(
      label="Download parameters as CSV",
      data=inputValsCsv,
      file_name='ucnps_virtual_lab_input_values.csv',
      mime='text/csv',
  )

  return Values
