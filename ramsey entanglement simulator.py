import numpy as np
import matplotlib.pyplot as plt

# Okay so here we are setting Laser phase φ from -2π to 2π
phi = np.linspace(-2 * np.pi, 2 * np.pi, 500)

# Just For better Visualisation and our main focus is on entanglement.
beta = 0

# Ramsey fringe probability formula 
def ramsey_probability(alpha, phi, beta=0):
    visibility = np.cos(alpha / 2)
    return 0.5 + 0.5 * visibility * np.cos((alpha / 2) + beta + phi)

# Calculate Ramsey fringes for α = π and α = 2π
P_alpha_pi = ramsey_probability(np.pi, phi, beta)        # Entangled case
P_alpha_2pi = ramsey_probability(2 * np.pi, phi, beta)    # Not entangled case

# Plotting the fringes
plt.figure(figsize=(12, 6))
plt.plot(phi / np.pi, P_alpha_pi, label='α = π (Entangled)', color='crimson', linestyle='--', linewidth=2)
plt.plot(phi / np.pi, P_alpha_2pi, label='α = 2π (Not Entangled)', color='royalblue', linewidth=2)
plt.xlabel('Laser Phase ϕ / π', fontsize=12)
plt.ylabel('Probability of $|1⟩$ (P₁)', fontsize=12)
plt.title('Ramsey Fringes (From Theory) — Entangled vs Not Entangled', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()
