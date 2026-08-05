import streamlit as st
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
from theory import theory

# ---Streamlit Setup---
st.set_page_config(page_title="Turing Pattern Simulator", page_icon=":leopard:")
st.title("Turing Pattern Simulator :leopard:")

# Allow user to read Background and Theory
with st.expander("Background and Theory"):
    theory()

st.markdown("Adjust the parameters and run the simulation to see your Turing patterns emerge.")

# Sidebar for parameters
st.sidebar.header("Simulation Parameters")
with st.sidebar:
    f = st.slider("Feed Rate (f)", 0.010, 0.100, 0.055, 0.001)
    k = st.slider("Kill Rate (k)", 0.045, 0.070, 0.062, 0.001)
    Da = st.slider("Diffusion A (Da)", 0.5, 1.5, 1.0, 0.1)
    Db = st.slider("Diffusion B (Db)", 0.1, 0.8, 0.5, 0.1)
    iterations = st.number_input("Number of Time Steps", 100, 200000, 10000, 100)

# ---Maths Setup---
# The 3x3 Laplacian kernel for calculating 2D diffusion
laplacian_kernel = np.array([[0.05, 0.2, 0.05],
                             [0.2, -1.0, 0.2],
                             [0.05, 0.2, 0.05]])

def init_grid(size=250):
    # Initialise the grid with morphogen A everywhere and no morphogen B.
    A = np.ones((size, size))
    B = np.zeros((size, size))
    # A and B are now numpy arrays that represent their concentrations in the grid.

    # Add B randomly throughout grid. 
    for i in range(size):
        for j in range(size):
            if np.random.random() < 0.015:  # 1.5 % chance of B
                B[i, j] = 1.0

    return A, B

def update(A, B, Da, Db, f, k):
    """Apply the Gray-Scott equations for one time step."""
    # Calculate diffusion using 2D convolution
    lapA = convolve2d(A, laplacian_kernel, mode='same', boundary='wrap')
    lapB = convolve2d(B, laplacian_kernel, mode='same', boundary='wrap')

    # Calculate reaction terms
    reaction = A * (B ** 2)

    # Calculate next state (dt = 1.0)
    next_A = A + (Da * lapA - reaction + f * (1 - A))
    next_B = B + (Db * lapB + reaction - (k + f) * B)

    # Keep values between 0 and 1
    return np.clip(next_A, 0, 1), np.clip(next_B, 0, 1)

# --- 3. Execution ---
if st.button("Run Simulation"):
    # Create placeholders for a progress bar and the image
    progress_bar = st.progress(0)
    image_placeholder = st.empty()
    
    A, B = init_grid()
    
    # Run the loop
    for i in range(iterations):
        A, B = update(A, B, Da, Db, f, k)
        
        # Update the UI every 50 iterations to avoid freezing
        if i % 50 == 0:
            progress_bar.progress(i / iterations)
            # We visualize Substance B (the inhibitor)
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.imshow(B, cmap="bone", interpolation='bicubic') 
            ax.axis('off')
            image_placeholder.pyplot(fig)
            plt.close(fig) # Free up memory
            
    progress_bar.progress(1.0)
    st.success("Simulation Complete!")