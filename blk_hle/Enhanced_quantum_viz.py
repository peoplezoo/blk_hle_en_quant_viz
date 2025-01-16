import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider
import time

# Initialize parameters
time_step = 0
phase = 0
damping_wave = 10
damping_gravity = 5
interaction_strength = 1

plt.ion()  # Turn on interactive plotting
fig, axes = plt.subplots(3, 1, figsize=(8, 12))

# Plot setup
def plot_quantum_dynamics(damping_wave, damping_gravity, interaction_strength):
    global time_step, phase
    
    time_step = (time_step + 1) % 100
    phase = (phase + 0.1) % (2 * np.pi)
    
    x = np.linspace(0, 5, 50)
    
    # Calculate functions
    psi = np.sin(x - phase) * np.exp(-x / damping_wave)
    gravity = np.exp(-x / damping_gravity) * np.cos(x - phase)
    interaction = interaction_strength * psi * gravity

    # Plot Quantum Wave Function
    axes[0].clear()
    axes[0].plot(x, psi, color='#8884d8', linewidth=2)
    axes[0].set_title('Quantum Wave Function')
    axes[0].set_ylim([-1.5, 1.5])
    axes[0].grid(True)

    # Plot Gravitational Field
    axes[1].clear()
    axes[1].plot(x, gravity, color='#82ca9d', linewidth=2)
    axes[1].set_title('Gravitational Field')
    axes[1].set_ylim([-1.5, 1.5])
    axes[1].grid(True)

    # Plot Quantum-Gravity Interaction
    axes[2].clear()
    axes[2].plot(x, interaction, color='#ff7300', linewidth=2)
    axes[2].set_title('Quantum-Gravity Interaction')
    axes[2].set_ylim([-1.5, 1.5])
    axes[2].grid(True)

    fig.canvas.draw()
    fig.canvas.flush_events()


# Create interactive widgets
interact(
    plot_quantum_dynamics,
    damping_wave=FloatSlider(value=10, min=1, max=20, step=0.1, description='Wave Damping'),
    damping_gravity=FloatSlider(value=5, min=1, max=20, step=0.1, description='Gravity Damping'),
    interaction_strength=FloatSlider(value=1, min=0, max=5, step=0.1, description='Interaction Strength')
)

plt.show()
