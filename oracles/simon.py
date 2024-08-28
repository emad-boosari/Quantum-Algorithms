import random
from qiskit import QuantumCircuit

class SimonOracle:
    def __init__(self, num_qubits, hidden_string='random'):
        """
        Initialize the Simon Oracle.

        :param num_qubits: Number of qubits in the oracle.
        :param hidden_string: The hidden binary string or 'random' to generate a random string.
        """
        self.num_qubits = num_qubits
        self.is_random = hidden_string == 'random'
        self.hidden_string = self.generate_hidden_string() if self.is_random else hidden_string

    def generate_hidden_string(self):
        """Generate a random binary string of length num_qubits."""
        return ''.join(random.choices('01', k=self.num_qubits))

    def create_oracle(self) -> QuantumCircuit:
        """
        Create the oracle based on the hidden string.

        :return: A QuantumCircuit representing the oracle.
        """
        oracle = QuantumCircuit(self.num_qubits * 2)
        position_from_right = len(self.hidden_string) - self.hidden_string.rfind('1') - 1
        
        # copier block
        for i in range(self.num_qubits):            
                oracle.cx(i, i + self.num_qubits)
        
        for i in range(self.num_qubits):
            if self.hidden_string[::-1][i] == '1':
                oracle.cx(position_from_right, i + self.num_qubits)
        
        oracle_gate = oracle.to_gate()
        if self.is_random:
            oracle_gate.name = 'Random Oracle'
        else:
            oracle_gate.name = f's={self.hidden_string}'
        
        return oracle_gate

    def get_hidden_string(self):
        """
        Get the hidden binary string used by the oracle.

        :return: The hidden binary string.
        """
        return self.hidden_string