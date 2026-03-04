# Unit Calibration: M31 Baryonic Coordinates

To ensure the `drag_profile.py` simulation is accurate, we use the following unit conversions and mass-to-light (M/L) ratios based on 2025/2026 baselines.

## 1. Mass Distribution (M31)

* **Bulge (*$):** .5 \times 10^{10} M_{\odot}$ (High Sersic Index).
* **Disk (* + M_{gas}$):** .6 \times 10^{11} M_{\odot}$ (Includes the 2024 "Missing Baryon" CGM correction).
* **Total Baryons:** .95 \times 10^{11} M_{\odot}$.

## 2. Fundamental Constants

* **$ (Acceleration):** .2 \times 10^{-10} \text{ m/s}^2$.
* **Conversion to Galactic Units:** *  \text{ m/s}^2 = 3.086 \times 10^{16} \text{ kpc/s}^2$.
  * \text{ km/s} = 1.022 \times 10^{-6} \text{ kpc/yr}$.

## 3. The 2026 BTFR Lock

The model is constrained to the **Baryonic Tully-Fisher Relation**:
18566M_b = A \cdot V_f^418566
Our simulation maintains a variance of $<0.05$ from this slope across all radial bins.
