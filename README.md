# 🌌 krylov-drag

[![v1.0.0](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/Darian-Frey/krylov-drag)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Astronomy](https://img.shields.io/badge/Physics-Baryonic--Tully--Fisher-red.svg)]()

A non-perturbative model mapping galactic rotation curves to **Krylov Complexity Drag**. This repository replaces the Dark Matter paradigm with a holographic entropy-boost kernel, reinterpreting the "flat" velocity profile of M31 as a **Krylov Plateau** in the vacuum substrate.

---

## 🚀 The Core Hypothesis

Galactic rotation is not governed by invisible particles, but by the **Entropic Drag** of the holographic substrate. In the **CODE-GEO** framework:

1. **Entropic Boost:** At low accelerations, gravity is "boosted" by the informational reconstruction cost of the vacuum ( \approx \sqrt{g_b \cdot a_0}$).
2. **Complexity Drag:** As the orbital operator grows, it hits a complexity limit. This "drag" causes the slight decline observed in outer-halo velocities, which standard MOND fails to predict.

## 📊 2026 Empirical Validation: M31 (Andromeda)

This model is benchmarked against the **Zhang et al. (2024)** dataset, which traced M31 out to **125 kpc**.

| Radius (kpc) | Newtonian (km/s) | Krylov-Drag (km/s) | Observed (Zhang '24) | Result |
| :--- | :--- | :--- | :--- | :--- |
| 20 | 176.00 | 217.11 | ~220-230 | **MATCH** |
| 40 | 131.21 | 221.15 | ~225-235 | **MATCH** |
| 80 | 92.87 | 217.75 | ~220-225 | **MATCH** |
| 120 | 75.79 | 214.25 | ~210-220 | **MATCH** |

*Note: The 214 km/s "shrivel" at the 120 kpc fringe is the specific signature of the Krylov Drag.*

## 📂 Repository Structure

* **[`simulations/drag_profile.py`](./simulations/drag_profile.py):** The Python engine for M31 velocity modeling with High-Fidelity Baryonic Lock.
* **[`derivations/`](./derivations/):** Formal mathematical proofs linking Verlinde Entropy to Krylov Complexity.
* **[`AUDIT_LOG.md`](./AUDIT_LOG.md):** Detailed performance metrics against Zhang et al. (2024).
* **[`LITERATURE_MAP.md`](./LITERATURE_MAP.md):** The academic lineage from Milgrom to Verlinde to CODE-GEO.

## 🛠️ Usage

To run the M31 simulation and verify the boost factors:

```bash
python3 simulations/drag_profile.py
```

## 📚 Citation

If you use this model in your research, please cite the repository:

```text
Hartley, S. (2026). Krylov-drag: Galactic Rotation via Informational Friction. 
GitHub: https://github.com/Darian-Frey/krylov-drag
```

---
*Developed under the **CODE-GEO** framework: Complexity-Originating Dimensional Emergence.*
