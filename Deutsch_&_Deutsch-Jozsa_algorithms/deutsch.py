!pip install qiskit
!pip install pylatexenc

from qiskit import QuantumCircuit
import numpy as np

class OracleProvider:
    """Class to provide different types of oracles for the Deutsch and Deutsch-Jozsa algorithms."""

    def __init__(self, num_qubits: int):
        """
        Initialize the OracleProvider with the number of input qubits.

        :param num_qubits: The number of input qubits (not including the output qubit).
        """
        self.num_qubits = num_qubits

    def constant_oracle(self, output_value=0) -> QuantumCircuit:
        """
        Create a constant oracle that returns the same output for any input.

        :param output_value: 0 or 1, the value the oracle should return for any input.
        :return: A Gate representing the constant oracle.
        """
        oracle = QuantumCircuit(self.num_qubits + 1)

        if output_value == 1:
            oracle.x(self.num_qubits)  # Flip the output qubit to |1> if the constant output is 1.

        return oracle.to_gate(label="ConstantOracle")

    def balanced_oracle(self) -> QuantumCircuit:
        """
        Create a balanced oracle that returns 0 for half the inputs and 1 for the other half.

        :return: A Gate representing the balanced oracle.
        """
        oracle = QuantumCircuit(self.num_qubits + 1)

        # Apply CNOT gates to entangle each input qubit with the output qubit.
        for qubit in range(self.num_qubits):
            oracle.cx(qubit, self.num_qubits)

        return oracle.to_gate(label="BalancedOracle")

    def random_oracle(self) -> QuantumCircuit:
        """
        Create a random oracle that is either constant or balanced, but the type is not revealed.

        :return: A Gate representing the random oracle.
        """
        if np.random.rand() > 0.5:
            return self.constant_oracle(output_value=np.random.randint(2))
        else:
            return self.balanced_oracle()

from google.colab import drive
drive.mount('/content/drive')

%cd /content/drive/MyDrive/2- Programming/Python/2- Qiskit/0000- Quantum_Computation_Algorithms/Quantum-Computation-Algorithms



!jupyter nbconvert --to script deutsch.ipynb










































