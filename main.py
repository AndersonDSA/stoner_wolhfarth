import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Definindo os valores de H e theta
numero_pontos = 1000
H_max = 1.5
H_values = np.linspace(-H_max, H_max, numero_pontos)
theta_values = np.linspace(0, np.pi / 2, 4)

colors = ['blue', 'green', 'orange', 'red']


# Função de energia magnética com história
def stoner_wohlfarth(theta, H):
    def magnetic_energy(phi):
        return  (np.sin(phi))**2 -  H * np.cos(phi - theta) #((1 - np.cos(2 * (phi - theta))) / 4) - H * np.cos(phi)

    # Use phi_initial as the initial guess
    resultado = minimize_scalar(magnetic_energy, bounds=(0, 2 * np.pi), method='bounded')
    phi_min = resultado.x
    return phi_min

# Função de magnetização com história
def magnetizacao(theta_values, H_values):
    mag_long_inc = np.zeros((len(theta_values), len(H_values)))
    mag_long_dec = np.zeros((len(theta_values), len(H_values)))
    
    for i, theta in enumerate(theta_values):
        for j, H in enumerate(H_values):
            phi_min_inc = stoner_wohlfarth(theta, H)
            mag_long_inc[i, j] = np.cos(phi_min_inc  -  theta)
            phi_min_dec = stoner_wohlfarth(theta, -H)
            mag_long_dec[i, j] = -np.cos(phi_min_dec  -  theta)
           
    return mag_long_inc, mag_long_dec

# Função principal
def main():
    mag_long_inc, mag_long_dec = magnetizacao(theta_values, H_values)

    # Plotando o gráfico
    plt.figure()
    for idx in range(len(mag_long_inc)):
        theta_degrees = int(np.ceil(np.degrees(theta_values[idx])))
        color = colors[idx % len(colors)]
        plt.plot(H_values, mag_long_inc[idx], label=f'Theta {theta_degrees}°', color=color)
        plt.plot(H_values, mag_long_dec[idx], color=color )
 
    plt.xlabel('h')
    plt.ylabel('m_h')
    plt.title('Curva de Histerese')
    plt.legend()
    plt.grid(True)
    plt.show()

# Executa a função principal
main()
