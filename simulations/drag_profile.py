import numpy as np

"""
CODE-GEO V3.2: M31 Rotation Curve Simulation
--------------------------------------------
This script models the rotation curve of M31 (Andromeda) using the 
Krylov-MOND Hybrid framework. It replaces the need for Dark Matter 
by applying an informational 'Entropic Boost' derived from the 
holographic complexity of the vacuum.

References:
- Zhang et al. (2024): M31 rotation curve out to 125 kpc.
- CODE-GEO: Complexity-Originating Dimensional Emergence.
"""

def m31_simulation():
    # --- PHYSICAL CONSTANTS ---
    G = 4.3009e-6         # Gravitational Constant in kpc (km/s)^2 / M_sun
    a0 = 1.2e-10          # MOND Acceleration constant (m/s^2)
    # Convert a0 to internal units: kpc (km/s)^2 / kpc^2
    a0_unit = a0 * (3.086e19 / 1000**2) 
    
    # --- M31 BARYONIC PARAMETERS (Zhang et al. 2024 High-End) ---
    M_BULGE = 3.5e10      # Central Bulge mass in Solar Masses
    M_DISK  = 1.6e11      # Combined Stellar Disk + Extended Gas Halo (CGM)
    R_BULGE = 1.0         # Bulge scale radius (kpc)
    R_DISK  = 5.3         # Disk scale length (kpc)
    
    # --- KRYLOV DRAG PARAMETERS ---
    # DRAG_COEFF: The rate of informational energy dissipation into the substrate.
    DRAG_COEFF = 0.0008 
    
    radii = [20, 40, 60, 80, 100, 120]
    
    # Header for the results table
    print("\n" + "="*85)
    print(f"{'M31 KRYLOV-DRAG SIMULATION (CODE-GEO V3.2)':^85}")
    print("="*85)
    header = f"{'Radius':<10} | {'Newtonian':<12} | {'Boost':<10} | {'Drag':<10} | {'Final Vrot':<15} | {'Status'}"
    unit_h = f"{'(kpc)':<10} | {'(km/s)':<12} | {'(Factor)':<10} | {'(Factor)':<10} | {'(km/s)':<15} |"
    print(header)
    print(unit_h)
    print("-" * 85)

    for r in radii:
        # 1. NEWTONIAN CALCULATION (g_bar)
        # Bulge follows a Hernquist profile
        g_bulge = (G * M_BULGE) / (r * (r + R_BULGE)**2)
        # Disk follows an Exponential profile M(r) = M_total * [1 - (1+r/R)e^(-r/R)]
        m_r_disk = M_DISK * (1 - (1 + r/R_DISK) * np.exp(-r/R_DISK))
        g_disk = (G * m_r_disk) / (r**2)
        
        g_bar = g_bulge + g_disk
        v_newton = np.sqrt(r * g_bar)
        
        # 2. HOLOGRAPHIC BOOST (Deep MOND Limit)
        # Representing the emergent force from the complexity gradient
        g_eff = np.sqrt(g_bar * a0_unit)
        boost_factor = g_eff / g_bar if g_bar > 0 else 0
        
        # 3. KRYLOV DRAG (Informational Friction)
        # Accounting for the slight 'shrivelling' of the curve at high R
        drag_factor = np.exp(-DRAG_COEFF * r)
        
        # 4. FINAL VELOCITY
        v_final = np.sqrt(r * g_eff * drag_factor)
        
        # Status check against Zhang et al. (2024) 225 km/s target
        status = "MATCH" if 210 <= v_final <= 235 else "OUTLIER"
        
        print(f"{r:<10} | {v_newton:<12.2f} | {boost_factor:<10.2f} | {drag_factor:<10.2f} | {v_final:<15.2f} | {status}")

    print("-" * 85)
    print(f"Baryonic Baseline: { (M_BULGE + M_DISK)/1e11 }e11 M_sun | a0: {a0} m/s^2")
    print("="*85 + "\n")

if __name__ == "__main__":
    m31_simulation()
