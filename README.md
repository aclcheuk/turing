# Turing Pattern Simulator - Streamlit App
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://devguide.python.org/versions/)
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://turing-pattern-simulator.streamlit.app/)

An interactive Streamlit app to simulate and visualise the formation of Turing (Reaction-Diffusion) Patterns.

## Features
- **Interactive Simulation** - Streamlit slider widgets to control parameters such as feed rate and kill rate
- **Real-time Visualisation** - Watch the patterns develop as the simulation calculates the reaction-diffusion equations
- **Mathematical Precision** - Using `Numpy` and `Scipy` for efficient and vectorised computation of differential equations

## Installation
To run this project locally:
1) `git clone https://github.com/aclcheuk/turing.git`
2) `conda env create -f environment.yml`
3) `conda activate turing-env`
4) `streamlit run app.py`

## License
This project is licensed under the MIT License, see `LICENSE.md` for details.
