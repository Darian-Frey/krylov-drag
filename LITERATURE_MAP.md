# 📚 Literature Map: Galactic Entropic Drag

This document traces the academic lineage of the **Krylov-Drag** model, linking empirical Tully-Fisher observations to modern holographic complexity theory and the 2026 CODE-GEO framework.

---

## 1. Empirical Foundation: The MOND Limit

* **Milgrom, M. (1983)** - *A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis.*
  * **Contribution:** Established the acceleration constant  \approx 1.2 \times 10^{-10} \text{ m/s}^2$ as the threshold where Newtonian physics fails.
  * **Link to Project:** Provides the baseline (x)$ boost function in the low-acceleration regime ( < a_0$).

## 2. Theoretical Bridge: Entropic Gravity

* **Verlinde, E. P. (2016)** - *Emergent Gravity and the Dark Universe.*
  * **Contribution:** Proposed that gravity is an emergent entropic response to the displacement of information. Introduced the volume-law entanglement contribution to the gravitational force.
  * **Link to Project:** Justifies the "Boost Factor" as a holographic reconstruction cost rather than "missing mass."

## 3. The 2024-2026 Observational "Lock"

* **Zhang et al. (2024)** - *The Rotation Curve of M31 out to 125 kpc.*
  * **Contribution:** Constructed a high-fidelity rotation curve for Andromeda using >13,000 tracers. Crucially identified the "gentle decline" (250 km/s $\to$ 215 km/s) in the outer halo.
* **Duey et al. (2025/2026)** - *Refining the Baryonic Tully–Fisher Relation.*
  * **Contribution:** Confirmed the universal  \propto V^4$ slope, providing the hard constraint for the model's normalization.
  * **Link to Project:** Acts as the ground-truth data for the `drag_profile.py` simulation.

## 4. Complexity & The Krylov Plateau

* **Parker, D. E. et al. (2019)** - *A Universal Operator Growth Hypothesis.*
  * **Contribution:** Formulated the growth of operator complexity (Krylov Complexity) and the transition to the "plateau" phase.
* **CODE-GEO V3.2 (2026)** - *Holographic Reconstruction Drag.*
  * **Contribution:** Integrates Krylov complexity into the galactic rotation operator. Proposes that the outer-halo decline is a **Krylov Plateau** effect—where the informational substrate reaches maximum density and begins to "shrivel" the velocity profile.
  * **Link to Project:** Introduces the `DRAG_COEFF` which accounts for the Zhang (2024) decline better than standard MOND.

---

## 🗺️ Conceptual Flowchart

```text
[Milgrom/BTFR] ----> [Verlinde/Entropy] ----> [CODE-GEO/Krylov]
(Empirical Rule)      (Theoretical Origin)      (Informational Friction)
      |                     |                         |
   "What"                "How"                     "Why"
(Flat Curves)       (Emergent Boost)          (Krylov Plateau)
```
