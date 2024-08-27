import random
from qiskit import QuantumCircuit

class BVOracle:
    """Class to create a Bernstein-Vazirani oracle."""

    def __init__(self, num_qubits: int, hidden_string: str = 'random'):
        """
        Initialize the BVOracle.

        :param num_qubits: Number of input qubits.
        :param hidden_string: The hidden binary string or 'random' to generate a random string.
        """
        self.num_qubits = num_qubits
        self.is_random = hidden_string == 'random'  # Track if hidden string is generated randomly
        self.hidden_string = self._initialize_hidden_string(hidden_string)

    def _initialize_hidden_string(self, hidden_string):
        """Generate a random binary string if needed."""
        if self.is_random:
            return ''.join(random.choices('01', k=self.num_qubits))
        return hidden_string

    def create_oracle(self) -> QuantumCircuit:
        """
        Create the oracle based on the hidden string.

        :return: A QuantumCircuit representing the oracle.
        """
        oracle = QuantumCircuit(self.num_qubits + 1)
        for i in range(self.num_qubits):
            if self.hidden_string[i] == '1':
                oracle.cx(i, self.num_qubits)
        oracle_gate = oracle.to_gate()

        # Set the name based on whether the hidden string was generated randomly
        if self.is_random:
            oracle_gate.name = "Random Oracle"
        else:
            oracle_gate.name = f"Oracle {self.hidden_string}"

        return oracle_gate

    def get_hidden_string(self) -> str:
        """
        Get the hidden binary string used by the oracle.

        :return: The hidden binary string.
        """
        return self.hidden_string
