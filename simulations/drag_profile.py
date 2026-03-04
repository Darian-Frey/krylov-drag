import numpy as np

def m31_simulation():
    # --- PHYSICAL CONSTANTS ---
    G = 4.3009e-6         
    a0 = 1.2e-10          
    a0_unit = a0 * (3.086e19 / 1000**2) 
    
    # --- M31 BARYONIC LOCK (Baryons + CGM Halo) ---
    M_bulge = 3.5e10
    M_disk  = 1.6e11      # Reaching Zhang et al. 2024 Upper Baryonic Bound
    R_bulge = 1.0
    R_disk  = 5.3
    
    radii = [20, 40, 60, 80, 100, 120]
    
    print(f"{'Radius (kpc)':<15} | {'Newtonian (km/s)':<20} | {'Krylov-Drag (km/s)':<20}")
    print("-" * 65)

    for r in radii:
        g_bulge = (G * M_bulge) / (r * (r + R_bulge)**2)
        m_r_disk = M_disk * (1 - (1 + r/R_disk) * np.exp(-r/R_disk))
        g_disk = (G * m_r_disk) / (r**2)
        g_bar = g_bulge + g_disk
        
        v_newton = np.sqrt(r * g_bar)
        
        # MOND/Entropic Boost
        g_eff = np.sqrt(g_bar * a0_unit)
        
        # Krylov Drag (Informational Friction)
        drag = np.exp(-0.0008 * r)
        
        v_krylov = np.sqrt(r * g_eff * drag)
        
        print(f"{r:<15} | {v_newton:<20.2f} | {v_krylov:<20.2f}")

if __name__ == "__main__":
    m31_simulation()
