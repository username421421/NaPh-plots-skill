# FDTD Method

The **Finite-Difference Time-Domain (FDTD)** method is a numerical technique for solving Maxwell's equations — the fundamental equations governing all electromagnetic phenomena. It was first proposed by Kane Yee in 1966 and remains one of the most widely used computational electromagnetics methods today.

FDTD is a **full-wave** method, meaning it captures all electromagnetic wave effects without approximation: reflection, diffraction, dispersion, polarization, and nonlinear interactions. It works by discretizing both space and time into a grid and marching the electric and magnetic fields forward in time using simple update equations derived from Maxwell's equations.


FDTD fits best in the **"resonance region"** — problems where the feature sizes of interest are on the order of a wavelength. Specifically:

- **Antenna design and analysis**
- **Electromagnetic compatibility (EMC) testing**
- **Photonic devices** (waveguides, filters, resonators)
- **Radar cross-section computation**
- **Biological tissue interaction with EM fields**
- **Optical components** (gratings, lenses, photonic crystals)

It is *less* suited for problems where features are either extremely small compared to the wavelength (quasi-static methods are more efficient) or extremely large (ray-based methods like geometric optics are preferable).

## Finite Differences

FDTD replaces continuous derivatives with discrete approximations. The key tool is the **central difference approximation**.

Consider a function $f(x)$. From Taylor series expansions about $x_0$ with offsets of $\pm\delta/2$:
$$\begin{aligned}f(x_0 + \delta/2) &= f(x_0) + (\delta/2)f'(x_0) + \frac{1}{2!}(\delta/2)^2f''(x_0) + \dots \\ f(x_0 - \delta/2) &= f(x_0) - (\delta/2)f'(x_0) + \frac{1}{2!}(\delta/2)^2f''(x_0) - \dots\end{aligned}$$

Subtracting the second from the first and dividing by $\delta$:
$$\left.\frac{df}{dx}\right|_{x=x_0} \approx \frac{f(x_0 + \delta/2) - f(x_0 - \delta/2)}{\delta} + \mathcal{O}(\delta^2)$$

This is the **central difference formula**. The crucial insight: the error term scales as $\delta^2$, so halving the grid spacing reduces the error by a factor of four. This **second-order accuracy** is what Yee chose for his FDTD algorithm.

> **Key insight**: The function is sampled not at $x_0$ itself, but at the two neighboring half-points. This staggering is the geometric heart of the FDTD method.

## Leap-Frog Scheme
FDTD directly discretizes the Ampère-Maxwell Law and Faraday’s Law of Induction in differential form. To make these equations useful for time-stepping, we substitute the fundamental connections $\mathbf{B} = \mu \mathbf{H}$ and $\mathbf{D} = \varepsilon \mathbf{E}$. Assuming a region with no free current ($\mathbf{J} = 0$), this gives us our working equations:

**Faraday's Law of Induction**: how a changing $\mathbf{E}$-field creates $\mathbf{H}$. Starting from the fundamental law $\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$, we substitute $\mathbf{B}$ to get:
$$-\mu \frac{\partial \mathbf{H}}{\partial t} = \nabla \times \mathbf{E}$$

**The Ampère-Maxwell Law**: how a changing $\mathbf{H}$-field creates $\mathbf{E}$. Starting from the fundamental law $\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}$, we substitute $\mathbf{D}$ and set $\mathbf{J}$ to zero to get:
$$\varepsilon \frac{\partial \mathbf{E}}{\partial t} = \nabla \times \mathbf{H}$$

These two equations are coupled: $\mathbf{E}$ drives changes in $\mathbf{H}$, and $\mathbf{H}$ drives changes in $\mathbf{E}$. The FDTD algorithm exploits this coupling with a leap-frog time-stepping scheme:
1. Update $\mathbf{H}$ using the current $\mathbf{E}$
2. Update $\mathbf{E}$ using the newly updated $\mathbf{H}$.
3. Repeat

This leap-frog approach means $\mathbf{E}$ and $\mathbf{H}$ are never known at the same instant — they are staggered by half a time step. This staggering in time mirrors the staggering in space, and together they form the Yee grid.

## The Yee Algorithm

The Yee algorithm (1966) is summarized in five steps:

1. **Discretize space and time** so that E and H fields are staggered both spatially and temporally.
2. **Replace derivatives** in Ampere's and Faraday's laws with central differences.
3. **Solve** the resulting difference equations for the "future" unknown fields in terms of the "past" known fields, producing **update equations**.
4. **Evaluate H** one half time-step into the future (H becomes "known").
5. **Evaluate E** one full time-step into the future (E becomes "known").
6. Repeat steps 4–5.


### The staggered grid (1D)

In 1D, if only Ez and Hy are non-zero (assuming variation in x only):

```
Space:    ...  Ez[m-1]  Hy[m-1/2]  Ez[m]  Hy[m+1/2]  Ez[m+1]  ...
                  ←——Δx/2——→←—Δx/2——→

Time:     ... Hy^(q-1/2)   Ez^q    Hy^(q+1/2)  Ez^(q+1) ...
              ←——Δt/2——→←——Δt/2——→
```

- **Ez nodes** (circles) sit at integer spatial positions m, sampled at integer time steps q.
- **Hy nodes** (triangles) sit at half-integer spatial positions m+½, sampled at half-integer time steps q+½.

This interlocking is not just mathematical bookkeeping — it is precisely what makes the central difference formula accurate. Each derivative is evaluated exactly at the midpoint between the two sample values.

## Update Equations in 1D

Starting from the 1D form of Faraday's law applied at the space-time point $((m+1/2)\Delta x, q\Delta t)$:
$$\mu \frac{H_y^{q+1/2}[m+1/2] - H_y^{q-1/2}[m+1/2]}{\Delta t} = \frac{E_z^q[m+1] - E_z^q[m]}{\Delta x}$$

Solving for the future H-field:
$$H_y^{q+1/2}[m+1/2] = H_y^{q-1/2}[m+1/2] + \left(\frac{\Delta t}{\mu\Delta x}\right) \cdot \left(E_z^q[m+1] - E_z^q[m]\right)$$

Similarly, from Ampere's law applied at $(m\Delta x, (q+1/2)\Delta t)$:
$$E_z^{q+1}[m] = E_z^q[m] + \left(\frac{\Delta t}{\varepsilon\Delta x}\right) \cdot \left(H_y^{q+1/2}[m+1/2] - H_y^{q+1/2}[m-1/2]\right)$$

These two equations are the **heart of FDTD**. They say:

- The future H depends only on its past value and the neighboring E values.
- The future E depends only on its past value and the neighboring H values.

No matrix inversion, no global solve — just local arithmetic at each grid point, repeated at every time step.

## 3D Yee Grid
The 3D Yee grid, introduced by Kane Yee in 1966, is the fundamental spatial building block of the FDTD method. Instead of calculating both electric and magnetic fields at the exact same point in space, the Yee cell staggers them across a three-dimensional cubic lattice. In this arrangement, the electric field components are positioned at the centers of the cube's edges, while the magnetic field components are placed at the centers of the cube's faces.

This staggered layout is geometrically brilliant because it mirrors the physical behavior described by Maxwell’s equations. Every electric field vector is naturally surrounded by a closed loop of magnetic field vectors (capturing Ampere's Law), and every magnetic field vector is surrounded by a closed loop of electric field vectors (capturing Faraday's Law). Furthermore, this interlocking grid inherently enforces the divergence-free nature of magnetic fields across the simulation space, ensuring long-term physical accuracy without requiring extra corrective calculations. The visualization below illustrates this interleaved structure (adapted from meep documentation):

![3d yee cell](https://github.com/ymahlau/fdtdx-notebooks/blob/main/img/yee_cube.png?raw=true)


### The Courant Stability Condition

Introducing the Courant number $S_c = c\Delta t/\Delta x$ (where $c = 1/\sqrt{\varepsilon_0\mu_0}$ is the speed of light), the update coefficients simplify to:
$$\begin{aligned}\frac{\Delta t}{\varepsilon\Delta x} &= S_c \cdot \frac{\eta_0}{\varepsilon_r} \quad &\text{(for the E update)} \\ \frac{\Delta t}{\mu\Delta x} &= \frac{S_c}{\mu_r \cdot \eta_0} \quad &\text{(for the H update)}\end{aligned}$$

where$\eta_0 = \sqrt{\mu_0/\varepsilon_0} \approx 377\ \Omega$ is the free-space impedance. FDTD is an explicit time-marching algorithm. If the time step is too large, the simulation goes **unstable** — field values grow without bound, producing meaningless results. The stability condition in 1D is:

$$S_c = \frac{c\Delta t}{\Delta x} \le 1$$

In 2D:
$$\frac{c\Delta t}{\Delta x} \le \frac{1}{\sqrt{2}} \quad \text{(for square cells, } \Delta x = \Delta y \text{)}$$

In 3D:
$$\frac{c\Delta t}{\Delta x} \le \frac{1}{\sqrt{3}} \quad \text{(for cubic cells)}$$

**Physical intuition**: In each update cycle, information can only travel one spatial step. If Δt is too large, a disturbance could "jump" farther than one cell, violating causality as represented on the grid — and the algorithm blows up. The optimal Sc = 1 (in 1D) is also the most accurate, since it minimizes numerical dispersion. In practice, 1D simulations use Sc = 0.99, while 2D and 3D simulations use Sc = 0.99/√2 and 0.99/√3, respectively. This gives a little bit of safety buffer to prevent instabilities.

### Memory and time requirements

| Dimension | Memory (per field) | Time steps for accuracy |
|---|---|---|
| 1D | O(N) | O(N) |
| 2D | O(N²) | O(N²) |
| 3D | O(N³) | O(N⁴) (halving Δx also halves Δt) |

This is why 3D FDTD simulations can be expensive — a 2x increase in resolution in all directions increases memory by 8x and compute by 16x.

## Common Pitfalls and Best Practices

### Grid resolution

As a rule of thumb, use **at least 10–20 cells per wavelength** (at the highest frequency of interest). More cells reduce numerical dispersion but increase memory and time:

$$\begin{aligned}\Delta x &\le \frac{\lambda_{\text{min}}}{10} \quad &\rightarrow \quad \text{safe rule} \\ \Delta x &\le \frac{\lambda_{\text{min}}}{20} \quad &\rightarrow \quad \text{more accurate}\end{aligned}$$

### Numerical dispersion

Waves on an FDTD grid travel at speeds that differ slightly from c, and the error depends on the direction of propagation and the wavelength relative to the grid spacing. In 1D with Sc = 1, dispersion is zero — the scheme is exact. In 2D and 3D, some residual dispersion always exists.

### Staircasing of curved boundaries

Diagonal or curved boundaries must be approximated using staircase steps along the Cartesian grid. This introduces O(Δx) error (first-order) at boundaries, even though the bulk update equations are second-order. Conformal methods like subpixel-smoothing can mitigate this.

### Near-to-far-field transformation

FDTD computes near fields on the grid. To obtain far-field quantities (radiation patterns, RCS), a surface integration — the near-to-far-field (NTFF) transformation — should be applied over a closed Huygens surface that encloses all sources and scatterers.

## References
- Schneider, J. B. (2010). Understanding the finite-difference time-domain method. School of electrical engineering and computer science Washington State University, 28.


