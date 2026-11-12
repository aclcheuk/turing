import streamlit as st

equations = r'''
$$
\frac{\partial A}{\partial t}=D_{A}\triangledown _{2}A-AB^{2}+f(1-A)
$$
and
$$
\frac{\partial B}{\partial t}=D_{B}\triangledown _{2}B+AB^{2}-(f+k)B
$$
'''

def theory():
    st.subheader("Background and Theory")
    st.markdown('''
    Turing patterns are one of my favourite examples of emergence in biology, where simple rules/reactions applied locally give rise to global complexity.
    The other thing I love about Turing patterns is that they come from an unexpected source, they were first conceived by somebody better known for their contributions to mathematics and computer science than to the life sciences.\n
    
    In 1952, a year before the structure of DNA was determined, Alan Turing (of Enigma-code breaking fame) proposed a mathematical model to explain how patterns can emerge in nature. In his paper, [*The Chemical Basis of Morphogenesis*](https://doi.org/10.1098/rstb.1952.0012), Turing proposed an elegantly simple model for how patterns can emerge from a homogenous state with just two chemicals (morphogens). \
    The only necessary properties for these two morphogens (A and B) are that they diffuse at different rates and that they react with each other. \n

    Turing mathematically formalised these properties using partial differential equations. Today, these partial differential equation systems are known as reaction-diffusion systems and can be solved computationally. Below, is a figure from Turing's paper "*obtained in a few hours by a manual computation*." \n
    ''')
    st.image("../turing/turing_1952.png")
    st.subheader("The Gray-Scott Model")

    st.markdown('''
    Depending on the way morphogens A and B react with each other and their diffusion rates, you get different flavours of these equations. The most famous of these reaction-diffusion systems is the Gray-Scott model, which we use in this app. As you adjust the parameters you can see different patterns such as spots, stripes and labyrinths emerge.\
    We can write the Gray-Scott equations as follows:
    ''')
    st.write(equations)

    # $\frac{\partial A}{\partial t}=D_{A}\triangledown _{2}A-AB^{2}+f(1-A)$)
    #\frac{\partial B}{\partial t}=D_{B}\triangledown _{2}B+AB^{2}-(f+k)B

    st.write("Where:")
    st.write(r'''
    - $D_A$ and $D_B$ are the diffusion coefficients for morphogens A and B, respectively.
    - $f$ is the feed rate of morphogen A.
    - $k$ is the kill rate of morphogen B.
    - $\triangledown_2$ is the Laplacian operator, representing how A and B diffuse into neighbouring cells (pixels in our grid).
    ''')