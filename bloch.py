import cirq
import numpy as np
import cirq_web.bloch_sphere as bs

# Define the Hadamard operator.
H = 1/np.sqrt(2) * np.array([[1, 1],
                             [1, -1]])

# Define state vectors for |0⟩ and |1⟩.
state_0 = np.array([1, 0])
state_1 = np.array([0, 1])

# Apply the Hadamard transformation.
state_H0 = H @ state_0  # H|0⟩ = |+⟩ = [1/√2, 1/√2]
state_H1 = H @ state_1  # H|1⟩ = |−⟩ = [1/√2, -1/√2]

# Generate an HTML file for |0⟩.
bloch_0 = bs.BlochSphere(state_vector=state_0)
output_path_0 = bloch_0.generate_html_file(
    output_directory='.',
    file_name='bloch_sphere_0.html',
    open_in_browser=False
)
print("Bloch sphere for |0⟩ generated at:", output_path_0)

# Generate an HTML file for H|0⟩.
# Note: Convert numpy array to list if necessary.
bloch_H0 = bs.BlochSphere(state_vector=state_H0.tolist())
output_path_H0 = bloch_H0.generate_html_file(
    output_directory='.',
    file_name='bloch_sphere_H0.html',
    open_in_browser=False
)
print("Bloch sphere for H|0⟩ generated at:", output_path_H0)

# Generate an HTML file for |1⟩.
bloch_1 = bs.BlochSphere(state_vector=state_1)
output_path_1 = bloch_1.generate_html_file(
    output_directory='.',
    file_name='bloch_sphere_1.html',
    open_in_browser=False
)
print("Bloch sphere for |1⟩ generated at:", output_path_1)

# Generate an HTML file for H|1⟩.
bloch_H1 = bs.BlochSphere(state_vector=state_H1.tolist())
output_path_H1 = bloch_H1.generate_html_file(
    output_directory='.',
    file_name='bloch_sphere_H1.html',
    open_in_browser=False
)
print("Bloch sphere for H|1⟩ generated at:", output_path_H1)
