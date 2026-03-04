# 🤝 Contributing to krylov-drag

We welcome contributions from the theoretical physics and astrophysics communities. As a **CODE-GEO** project, we prioritize data-driven audits that test the limits of the **Krylov Complexity** framework.

## 🧪 How to Contribute

### 1. Data Audits (Galaxy Profiles)

The most valuable contribution is a new rotation curve audit. If you have high-fidelity baryonic data for a specific galaxy:

* Duplicate the `simulations/drag_profile.py` script.
* Update the mass coordinates (Bulge, Disk, Gas) and the observed velocity markers.
* Submit a Pull Request with the results added to the `AUDIT_LOG.md`.

### 2. Theoretical Refinements

If you have a derivation that improves the **Krylov Drag** exponential factor or links it more tightly to **Krylov Entropy**, please submit a detailed Issue or a LaTeX-formatted PDF in a new `/theory` directory.

### 3. Code Optimization

Help us make the simulations more precise. We are looking to move from a 2D exponential disk approximation to a full 3D potential solver.

## 🛠️ Development Workflow

1. **Fork** the repository.
2. Create a **Feature Branch** (`git checkout -b feature/galaxy-name`).
3. Ensure your simulation matches the **2026 BTFR Baseline** ( \propto V_f^4$).
4. Commit your changes (`git commit -m "add: M33 rotation curve audit"`).
5. Push to the branch and open a **Pull Request**.

## 📜 Code of Conduct

This project is a space for radical theoretical exploration grounded in empirical data. We value candor, mathematical rigor, and the shrivelling of "magic numbers" through logic.

---
*Questions? Open an issue or contact the CODE-GEO maintainers via the project Wiki.*
