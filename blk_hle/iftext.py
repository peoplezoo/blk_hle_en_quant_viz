import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Constantspip instqall
hbar = 1.0
k_B = 1.0
c = 1.0
G = 1.0
beta = 0.5
M_planck = 0.1

# Functions
def hawking_temperature(M):
    return hbar * c**3 / (8 * np.pi * G * M)

def quantum_corrected_entropy(M):
    A = 16 * np.pi * G * M**2 / c**4
    return A / (4 * G * hbar) + beta * np.log(A)

def yin_wavefunction(t, r, M):
    return np.exp(-r / (M + 1)) * np.exp(-1j * 0.5 * t)

def yang_wavefunction(t, r, M):
    return np.exp(-r / (M + 1)) * np.exp(+1j * 0.5 * t)

def emission_spectrum(M, omega):
    T_H = hawking_temperature(M)
    return omega**3 / (np.exp(hbar * omega / (k_B * T_H)) - 1)

# Simulation parameters
time_steps = 100
dt = 0.05
M_initial = 5.0
times = np.linspace(0, time_steps * dt, time_steps)
masses = np.linspace(M_initial, M_planck, time_steps)

# Generate wavefunction grid
r_values = np.linspace(0, 5, 100)
T, R = np.meshgrid(times, r_values)
mass_func = np.interp(T.flatten(), times, masses).reshape(T.shape)
Psi_yin = yin_wavefunction(T, R, mass_func)
Psi_yang = yang_wavefunction(T, R, mass_func)
Psi_total = Psi_yin + Psi_yang
prob_density = np.abs(Psi_total)**2

# Generate emission spectra grid
omega_values = np.linspace(0.01, 2.0, 50)
T_spec, Omega_spec = np.meshgrid(times, omega_values)
Emission_3d = np.zeros_like(T_spec)
for i, t_ in enumerate(times):
    M_ = masses[i]
    for j, omega_ in enumerate(omega_values):
        Emission_3d[j, i] = emission_spectrum(M_, omega_)

# Plotting
fig = plt.figure(figsize=(18, 12))

# Wavefunction probability density
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.plot_surface(T, R, prob_density, cmap=cm.viridis, edgecolor='none')
ax1.set_title("Wavefunction Probability Density (|Ψ|²)")
ax1.set_xlabel("Time")
ax1.set_ylabel("Radius")
ax1.set_zlabel("|Ψ|²")

# Emission spectra evolution
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax2.plot_surface(T_spec, Omega_spec, Emission_3d, cmap=cm.inferno, edgecolor='none')
ax2.set_title("Emission Spectra Evolution")
ax2.set_xlabel("Time")
ax2.set_ylabel("Energy (ω)")
ax2.set_zlabel("Emission Intensity")

# Mass evolution
ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(times, masses, label="Mass (M)", color="blue")
ax3.axhline(M_planck, color="gray", linestyle="--", label="Planck Mass")
ax3.set_title("Black Hole Mass Evolution with Stable Remnant")
ax3.set_xlabel("Time")
ax3.set_ylabel("Mass (M)")
ax3.legend()

# Entropy evolution
ax4 = fig.add_subplot(2, 2, 4)
entropies = quantum_corrected_entropy(masses)
ax4.plot(times, entropies, label="Entropy (S)", color="green")
ax4.set_title("Quantum-Corrected Entropy Evolution")
ax4.set_xlabel("Time")
ax4.set_ylabel("Entropy (S)")
ax4.legend()

plt.tight_layout()
plt.show()
