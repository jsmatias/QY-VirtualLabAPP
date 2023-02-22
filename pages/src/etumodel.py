from scipy import constants as cte
import pandas as pd
import numpy as np

def transitionPowerDensj(j, inputConstants):
  nu = cte.c / (inputConstants.excitationWavelength * 10**(-9))
  alpha = inputConstants.crossSection / (cte.h * nu)
  return (inputConstants.RA[j] * inputConstants.Rb / (inputConstants.WA[j] * alpha * inputConstants.NS))


def Nb(rho, inputConstants):

  nu = cte.c / (inputConstants.excitationWavelength * 10**(-9))
  alpha = inputConstants.crossSection / (cte.h * nu)
  return (alpha * inputConstants.NS * rho / (inputConstants.Rb + alpha * rho))


def Nj(j, rho, inputConstants):
  if j == 0:
    return len(list(rho)) * [inputConstants.NA]
  elif (j <= len(inputConstants.WA)):
    return (
      (inputConstants.WA[j - 1] * Nb(rho, inputConstants) * Nj(j - 1, rho, inputConstants)) /
        (inputConstants.WA[j] * Nb(rho, inputConstants) + inputConstants.RA[j])
    )
  else:
    return None


def QYj(j, rho, inputConstants):
  nu = cte.c / (inputConstants.excitationWavelength * 10**(-9))
  alpha = inputConstants.crossSection / (cte.h * nu)

  return Nj(j, rho, inputConstants) * inputConstants.RArad[j] / (alpha * rho * inputConstants.NS)


def getTransitionPoints(inputConstants):

  rhoiArr = []
  qySaturationArr = []
  for j in range(1, len(inputConstants.RA) - 1):
    rhoiArr.append(transitionPowerDensj(j, inputConstants))
    qySaturationArr.append(
      inputConstants.WA[0] * inputConstants.RArad[j] * inputConstants.WA[1] * inputConstants.NA /
        (inputConstants.RA[1] * inputConstants.Rb * inputConstants.WA[j])
    )

  data = pd.DataFrame({
    "rhoi": rhoiArr,
    "QYs": qySaturationArr
  })

  return data


def getData(inputConstants):
  powerDens = np.linspace(*inputConstants.powerDensRange, 500)

  data = pd.DataFrame({
      "power-dens": powerDens,
      "N0": Nj(0, powerDens, inputConstants),
      "N1": Nj(1, powerDens, inputConstants),
      "N2": Nj(2, powerDens, inputConstants),
      "N3": Nj(3, powerDens, inputConstants),
      "N4": Nj(4, powerDens, inputConstants),
      "QY1": QYj(1, powerDens, inputConstants),
      "QY2": QYj(2, powerDens, inputConstants),
      "QY3": QYj(3, powerDens, inputConstants),
      "QY4": QYj(4, powerDens, inputConstants)
  })
  for i in range(1, 4):
    emissionNu = cte.c / (inputConstants.emissionWavelengths[i] * 10**(-9))
    data[f'Luminescence-{i}'] = data[f'N{i}'] * \
        cte.h * emissionNu * inputConstants.RArad[i]

  return data
