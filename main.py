import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Definindo os valores de H e theta
H_values = np.linspace(-3, 3, 6)
theta_values = np.linspace(0, np.pi/2, 4)

# Função de energia magnética
def stoner_wohlfarth(theta, H):
    
    def magnetic_energy(phi):
        return ((1-np.cos(2*(phi-theta)))/4) - H*np.cos(phi)
        
    resultado = minimize_scalar(magnetic_energy, bounds=(0, 2*np.pi), method='bounded')
    phi_min = resultado.x
    return phi_min

# Função de magnetização
def magnetizacao(theta, H):
    mag_long = np.zeros((len(theta), len(H)))
    mag_tran = np.zeros((len(theta), len(H)))
    
    for i, t in enumerate(theta):
        for j, H1 in enumerate(H):
            mag_long[i, j] = np.cos(stoner_wohlfarth(t, H1))
            mag_tran[i, j] = np.sin(stoner_wohlfarth(t, H1))

    print(mag_long)
    return mag_long, mag_tran

# Função principal
def main():
    magnetizacao_longitudinal, magnetizacao_transversal = magnetizacao(theta_values, H_values)
    for idx, linha in enumerate(magnetizacao_longitudinal):
        print(f'Mag_Longitudinal_{idx} = {linha}')

# Executa a função principal
main()
