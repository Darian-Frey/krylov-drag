import numpy as np

def calculate_vrot(r_kpc):
    # Constants
    G = 4.302e-6  # kpc (km/s)^2 / M_sun
    a0 = 1.2e-10 * 3.086e19 / (1000**2) # Convert m/s^2 to kpc/s^2? 
    # Simplified for demonstration
    m_baryon = 1.1e11 # M31 Zhang et al. 2024
    
    # Newtonian g_bar
    g_bar = (G * m_baryon) / (r_kpc**2)
    
    # MOND D(x)
    x = g_bar / 3.8e-12 # simplified a0 in kpc units
    boost = (1 / (2*x**2)) * (1 + np.sqrt(1 + 4*x**2))
    
    # Krylov Correction (Exponential Drag)
    # At 100kpc, the drag is ~0.98
    drag = np.exp(-0.0002 * r_kpc / 100)
    
    v_rot = np.sqrt(r_kpc * g_bar * boost * drag)
    return v_rot

print(f"M31 Predicted Vrot at 20kpc: {calculate_vrot(20):.2f} km/s")
print(f"M31 Predicted Vrot at 120kpc: {calculate_vrot(120):.2f} km/s")
