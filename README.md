# Stochastic Process Simulations

A Python project exploring stochastic processes through numerical simulation and visualization.

The repository contains simulations based on the Wiener process (Brownian motion), including a rotating-process model and a stochastic model for snow accumulation on a roof.

## Overview

The project demonstrates how stochastic processes can be simulated numerically using normally distributed random increments.

The simulations use:

- NumPy for numerical computation
- Matplotlib for visualization
- Wiener process increments
- Multiple simulated trajectories
- Time discretization
- Simple stochastic models

The repository contains two main simulations:

- A Wiener process modulated by a rotating sinusoidal component
- A stochastic snow accumulation model with drift and random fluctuations

## Projects

### Rotating Wiener Process

`ItoovProces.py`

This simulation models the stochastic process:

```text
Y(t) = W(t) sin(ωt)
```

where:

- `W(t)` is a Wiener process
- `ω` is the angular velocity
- `t` is time

The implementation generates many independent Wiener-process trajectories and multiplies each trajectory by a sinusoidal term. :chatgpt-content-reference{index="0"}

The angular velocity is set to:

```text
ω = 0.2
```

and the simulation uses 300 trajectories over 100 units of time. :chatgpt-content-reference{index="1"}

The Wiener process is generated using increments of the form:

```text
dW = sqrt(dt) * N(0,1)
```

which are accumulated over time. :chatgpt-content-reference{index="2"}

The resulting stochastic process is then calculated as:

```text
Y(t) = W(t) sin(ωt)
```

and plotted for all simulated trajectories. :chatgpt-content-reference{index="3"}

## Snow Accumulation Model

`SnowOnTheRoof.py`

This simulation models the amount of snow on a roof using a stochastic process of the form:

```text
X(t) = X0 + a t + c W(t)
```

where:

- `X0` is the initial amount of snow
- `a` represents the average snowfall rate
- `c` controls the strength of random fluctuations
- `W(t)` is a Wiener process :chatgpt-content-reference{index="4"}

The simulation parameters are:

```text
X0 = 5.0
a  = 0.2
c  = 0.8
```

The model is simulated over 100 time units using 500 time steps and 300 independent trajectories. :chatgpt-content-reference{index="5"}

At each time step, the process is updated using:

```text
X[n+1] = X[n] + a * dt + c * dW
```

where:

```text
dW = sqrt(dt) * N(0,1)
```

represents a Wiener-process increment. :chatgpt-content-reference{index="6"}

The model also includes the physical condition that the amount of snow cannot become negative:

```python
if X[n+1] < 0:
    X[n+1] = 0
```

:chatgpt-content-reference{index="7"}

## Wiener Process

A Wiener process, also known as Brownian motion, is a continuous-time stochastic process commonly used in probability theory, mathematical finance, physics, and stochastic differential equations.

In a numerical simulation, the process is approximated using discrete increments:

```text
W(t + dt) = W(t) + dW
```

where:

```text
dW ~ N(0, dt)
```

In the code, this is implemented as:

```python
dW = np.sqrt(dt) * np.random.randn()
```

:chatgpt-content-reference{index="8"}

## Visualization

Both simulations generate multiple stochastic trajectories and display them using Matplotlib.

This makes it possible to observe how the same stochastic model can produce many different outcomes due to random variation.

For example, the snow model plots 300 independent realizations of the snow accumulation process. :chatgpt-content-reference{index="9"}

## Technologies

- Python
- NumPy
- Matplotlib
- Probability theory
- Stochastic processes
- Wiener processes
- Brownian motion
- Numerical simulation
- Scientific computing

## Project Structure

```text
stochastic-process-simulations/
│
├── ItoovProces.py
├── SnowOnTheRoof.py
└── README.md
```

### Files

- `ItoovProces.py` — simulation of a Wiener process multiplied by a sinusoidal component
- `SnowOnTheRoof.py` — stochastic simulation of snow accumulation on a roof
- `README.md` — project documentation

## Running the Project

### Requirements

You need Python and the following packages:

```text
numpy
matplotlib
```

Install the dependencies with:

```bash
pip install numpy matplotlib
```

Clone the repository:

```bash
git clone https://github.com/hannahkuklovska/stochastic-process-simulations.git
cd stochastic-process-simulations
```

Run the rotating Wiener-process simulation:

```bash
python ItoovProces.py
```

Run the snow accumulation simulation:

```bash
python SnowOnTheRoof.py
```

Each script will generate a plot containing multiple simulated trajectories.

## Concepts Demonstrated

This project demonstrates:

- Stochastic processes
- Wiener processes
- Brownian motion
- Normally distributed random increments
- Time discretization
- Monte Carlo-style simulation
- Multiple trajectory generation
- Drift and volatility
- Scientific visualization
- Numerical programming with NumPy

## What I Learned

Through this project, I practiced implementing stochastic processes numerically in Python.

In particular, I worked with:

- generating Wiener-process increments,
- simulating multiple realizations of random processes,
- discretizing continuous-time stochastic models,
- combining deterministic and stochastic components,
- modeling drift and random fluctuations,
- applying simple physical constraints to a stochastic model,
- and visualizing large numbers of simulated trajectories using Matplotlib.

## Possible Improvements

Future improvements could include:

- setting a random seed for reproducible simulations
- calculating sample means and variances
- comparing simulated statistics with theoretical values
- displaying confidence intervals
- creating histograms of terminal values
- computing expected values over time
- exporting plots automatically
- converting repeated simulation logic into reusable functions
- adding command-line parameters
- adding automated tests
- comparing different stochastic models

## Author

Hannah Kuklovska
