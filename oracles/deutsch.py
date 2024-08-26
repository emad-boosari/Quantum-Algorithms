from qiskit import QuantumCircuit
import numpy as np

class DeutschOracle:
    """Class to provide different types of oracles for the Deutsch algorithm."""

    def __init__(self, oracle_type='random', output_value=0):
        """
        Initialize the DeutschOracle with the oracle type.

        :param oracle_type: The type of oracle to generate ('balanced', 'constant', 'random').
        :param output_value: 0 or 1, the value the constant oracle should return (only used for 'constant' type).
        """
        self.oracle_type = oracle_type.lower()
        self.output_value = output_value

    def create_oracle(self) -> QuantumCircuit:
        """
        Create the oracle based on the specified type.

        :return: A Gate representing the oracle.
        """
        oracle_methods = {
            'constant': self.constant,
            'balanced': self.balanced,
            'random': self.random
        }

        if self.oracle_type in oracle_methods:
            return oracle_methods[self.oracle_type]()
        else:
            raise ValueError(f"Unknown oracle type: {self.oracle_type}. Choose from 'constant', 'balanced', 'random'.")

    def constant(self) -> QuantumCircuit:
        """
        Create a constant oracle that returns the same output for any input.

        :return: A Gate representing the constant oracle.
        """
        oracle = QuantumCircuit(2)

        if self.output_value == 1:
            oracle.x(1)  # Flip the output qubit to |1> if the constant output is 1.

        return oracle.to_gate(label="ConstantOracle")

    def balanced(self) -> QuantumCircuit:
        """
        Create a balanced oracle that returns 0 for half the inputs and 1 for the other half.

        :return: A Gate representing the balanced oracle.
        """
        oracle = QuantumCircuit(2)

        if self.output_value == 0:
            oracle.cx(0, 1)
        else:
            oracle.x(0)
            oracle.cx(0, 1)
            oracle.x(0)

        return oracle.to_gate(label="BalancedOracle")

    def random(self) -> QuantumCircuit:
        """
        Create a random oracle that can be one of the four types:
        - Constant 0
        - Constant 1
        - Balanced 0
        - Balanced 1

        :return: A Gate representing the random oracle.
        """
        is_constant = np.random.rand() > 0.5
        random_output_value = np.random.randint(2)
        self.output_value = random_output_value

        if is_constant:
            oracle_gate = self.constant()
        else:
            oracle_gate = self.balanced()

        # Create a wrapper circuit with the "Random Oracle" label
        random_oracle_circuit = QuantumCircuit(2)
        random_oracle_circuit.append(oracle_gate, range(2))

        return random_oracle_circuit.to_gate(label="Random Oracle")