import streamlit as st
import plotly.graph_objects as go


def luminescence(data):
  fig = go.Figure()
  luminCols = [col for col in data.columns if 'Lumin' in col]
  for col in luminCols:
    fig.add_trace(go.Scatter(x=data["power-dens"], y=0.03 * data[col],
                             mode='lines+markers',
                             name=col))

  # Edit the layout
  fig.update_layout(title='Luminescence per energy states',
                    xaxis_title='Power density (W/cm^2)',
                    yaxis_title='Emission intensity (W/cm^3)')
  return fig


def populationDensity(data):
  fig = go.Figure()
  popDensCols = [col for col in data.columns if 'N' in col]
  for col in popDensCols:
    fig.add_trace(go.Scatter(x=data["power-dens"], y=data[col],
                             mode='lines+markers',
                             name=col))

  # Edit the layout
  fig.update_layout(title='Population densities of the energy states',
                    xaxis_title='Power density (W/cm^2)',
                    yaxis_title='Population density (cm^-3)')

  return (fig)


def quantumYield(data):
  fig = go.Figure()
  quantumYieldCols = [col for col in data.columns if 'QY' in col]

  for col in quantumYieldCols:
    fig.add_trace(go.Scatter(x=data["power-dens"], y=data[col] * 100,
                             mode='lines+markers',
                             name=col))

  # Edit the layout
  fig.update_layout(title='Quantum Yield per energy state',
                    xaxis_title='Power density (W/cm^2)',
                    yaxis_title='Internal Quantum Yield (%)')

  return (fig)


def chartPanel(data, transitionPoints):

  fig1 = populationDensity(data)
  fig2 = luminescence(data)
  fig3 = quantumYield(data)

  col1, col2 = st.columns(2)
  with col1:
    xLog = st.checkbox("X-Axes in log scale", key='qy-xaxis', value=True)
  with col2:
    yLog = st.checkbox("Y-Axes in log scale", key='qy-yaxis', value=True)
  fig1.update_yaxes(type='log' if yLog else 'linear')
  fig2.update_yaxes(type='log' if yLog else 'linear')
  fig3.update_yaxes(type='log' if yLog else 'linear')

  fig1.update_xaxes(type='log' if xLog else 'linear')
  fig2.update_xaxes(type='log' if xLog else 'linear')
  fig3.update_xaxes(type='log' if xLog else 'linear')

  tab1, tab2, tab3, tab4 = st.tabs(
    ["Population density", "Luminescence", "Quantum Yield", "Details"])

  with tab1:
    st.plotly_chart(fig1, use_container_width=True)
  with tab2:
    st.plotly_chart(fig2, use_container_width=True)
  with tab3:
    st.plotly_chart(fig3, use_container_width=True)
    # st.write(data)
  with tab4:

    rhoiStr = r"$\rho_i$ $[W/cm^2]$"
    etaSiStr = r"$\eta_{si}$ $[\%]$"
    rho1 = transitionPoints['rhoi'][0]
    rho2 = transitionPoints['rhoi'][1]
    rho3 = transitionPoints['rhoi'][2]
    rho4 = transitionPoints['rhoi'][3]
    etaS1 = transitionPoints['QYs'][0] * 100
    etaS2 = transitionPoints['QYs'][1] * 100
    etaS3 = transitionPoints['QYs'][2] * 100
    etaS4 = transitionPoints['QYs'][3] * 100
    st.markdown(f"""
    #### Transition points

    | i | {rhoiStr}       | {etaSiStr}      | 
    |---| --------------: | --------------: | 
    | 1 | {rho1:.3f}      | {etaS1:.4g}     | 
    | 2 | {rho2:.3f}      | {etaS2:.4g}     | 
    | 3 | {rho3:.3f}      | {etaS3:.4g}     | 
    | 4 | {rho4:.3f}      | {etaS4:.4g}     | 
    """)
    # st.write(transitionPoints)

    st.markdown('---')
    st.markdown('#### Data')

    st.write(data.head())

    @st.cache_data
    def convert_df(df):
      # IMPORTANT: Cache the conversion to prevent computation on every rerun
      return df.to_csv()

    dataCsv = convert_df(data)

    st.download_button(
        label="Download full dataset as CSV",
        data=dataCsv,
        file_name='ucnps_virtual_lab_data.csv',
        mime='text/csv',
    )

    # st.write(inputValues)
