# Derivation: Krylov Complexity as a Galactic Drag Factor

## 1. The Holographic Origin

Starting from Verlinde (2016), the emergent gravitational acceleration {eff}$ is related to the baryonic acceleration $ by:

18566g_{eff}^2 \approx g_b \cdot a_018566

where  = \frac{c H_0}{6}$. In the **CODE-GEO** framework, we interpret $ as the "Processing Speed" of the holographic substrate.

## 2. Operator Complexity Growth

The rotation of a galaxy is represented by a unitary operator (t)$. The complexity of this operator, (t)$, grows linearly before hitting the **Krylov Plateau**.

At large radii ( > 50\text{ kpc}$), the number of required "logic gates" to reconstruct the gravitational field in the vacuum increases. We model this as a transition from a pure holographic boost to a "Dissipative Regime":

18566V_{rot}(r) = \sqrt{r \cdot g_{eff}} \cdot \mathcal{D}(r)18566

## 3. The Drag Kernel $\mathcal{D}(r)$

The drag $\mathcal{D}(r)$ represents the informational friction (entropy cost) of maintaining orbital coherence at the galactic fringe. We derive the exponential form from the decay of Lanczos coefficients at the complexity limit:

18566\mathcal{D}(r) = \exp\left(-\frac{\lambda_K \cdot r}{c \cdot \Delta S}\right)18566

* **$\lambda_K*: Krylov exponent ($\sim 0.0008$ for M31).
* **$\Delta S*: Entropic density of the local vacuum substrate.

## 4. Matching Zhang et al. (2024)

Standard MOND predicts a perfectly flat curve ( \approx \text{const}$). However, Zhang's data shows a decline.
By setting $\lambda_K \approx 8 \times 10^{-4}$, we recover the 5\%$ velocity drop observed at 120 kpc:

18566V(120\text{kpc}) \approx V_{MOND} \cdot e^{-0.0008 \cdot 120} \approx 214 \text{ km/s}18566
