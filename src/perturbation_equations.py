import numpy as np
from scipy.integrate import solve_ivp

def zpp_over_z(eta):
    """Forma simplificada para slow-roll: z''/z = 2/eta²"""
    return 2.0 / eta**2

def solve_mukhanov_sasaki(k, eta_array):
    """
    Resolve a equação de Mukhanov–Sasaki:
    u'' + (k² - z''/z) u = 0
    """
    def ms_ode(eta, y):
        u, du = y
        ddu = - (k**2 - zpp_over_z(eta)) * u
        return [du, ddu]
    
    eta0 = eta_array[0]
    u0_real = np.real(np.exp(-1j * k * eta0) / np.sqrt(2 * k))
    u0_imag = np.imag(np.exp(-1j * k * eta0) / np.sqrt(2 * k))
    u0 = [u0_real, -k * u0_imag]  # aproximação Bunch–Davies

    sol = solve_ivp(ms_ode, [eta_array[0], eta_array[-1]], u0, t_eval=eta_array)
    return sol.t, sol.y[0]
