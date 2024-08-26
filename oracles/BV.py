import numpy as np
import random
from qiskit import QuantumCircuit, QuantumRegister

from qiskit import QuantumCircuit, QuantumRegister
import random

class BV:
    """Class to implement the Bernstein-Vazirani algorithm."""

    def __init__(self, num_qubits, hidden_string='random'):
        """
        Initialize the BV class.

        :param num_qubits: Number of input qubits.
        :param hidden_string: The hidden binary string or 'random' to generate a random string.
        """
        self.num_qubits = num_qubits
        self.hidden_string = hidden_string if hidden_string != 'random' else self.random_binary_string(num_qubits)
        self.q = QuantumRegister(self.num_qubits)
        self.a = QuantumRegister(1)

    def create_oracle(self) -> QuantumCircuit:
        """Create the oracle based on the specified hidden string."""
        if self.hidden_string == 'random':
            return self.random_oracle()
        else:
            return self.arbitrary_oracle()

    def random_binary_string(self, num_qubits):
        """Generate a random binary string."""
        return ''.join(random.choices(['0', '1'], k=num_qubits))

    def random_oracle(self) -> QuantumCircuit:
        """Create a random oracle based on a random hidden string."""
        string = self.random_binary_string(self.num_qubits)
        circuit = QuantumCircuit(self.q, self.a)
        circuit.x(self.a)
        for i in range(self.num_qubits):
            if string[i] == '1':
                circuit.cx(self.q[i], self.a)
        oracle_gate = circuit.to_gate()
        oracle_gate.name = 'Random Oracle'
        return oracle_gate

    def arbitrary_oracle(self) -> QuantumCircuit:
        """Create an oracle for a specific hidden string."""
        circuit = QuantumCircuit(self.q, self.a)
        circuit.x(self.a)
        for i in range(self.num_qubits):
            if self.hidden_string[i] == '1':
                circuit.cx(self.q[i], self.a)
        oracle_gate = circuit.to_gate()
        oracle_gate.name = f'Oracle {self.hidden_string}'
        return oracle_gate



from google.colab import drive
drive.mount('/content/drive')

%cd /content/drive/MyDrive/2- Programming/Python/2- Qiskit/0000- Quantum_Computation_Algorithms/Quantum-Algorithms/oracles

%ls

!mv BV.ipynb BV.Py
!ls

!pip install jupyter

!jupyter nbconvert --to script your_notebook.ipynb












