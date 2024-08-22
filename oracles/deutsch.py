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
        if self.oracle_type == 'constant':
            return self.constant_oracle()
        elif self.oracle_type == 'balanced':
            return self.balanced_oracle()
        elif self.oracle_type == 'random':
            return self.random_oracle()
        else:
            raise ValueError(f"Unknown oracle type: {self.oracle_type}. Choose from 'constant', 'balanced', 'random'.")

    def constant_oracle(self) -> QuantumCircuit:
        """
        Create a constant oracle that returns the same output for any input.

        :return: A Gate representing the constant oracle.
        """
        oracle = QuantumCircuit(2)

        if self.output_value == 1:
            oracle.x(1)  # Flip the output qubit to |1> if the constant output is 1.

        return oracle.to_gate(label="ConstantOracle")

    def balanced_oracle(self) -> QuantumCircuit:
        """
        Create a balanced oracle that returns 0 for half the inputs and 1 for the other half.

        :return: A Gate representing the balanced oracle.
        """
        oracle = QuantumCircuit(2)

        if self.output_value == 1:
            # f(0) = 1, f(1) = 0: Implement this as an "open control" CNOT
            oracle.x(0)      # Invert the control qubit
            oracle.cx(0, 1)  # Apply CNOT
            oracle.x(0)      # Revert the control qubit
        else:
            # f(0) = 0, f(1) = 1: Standard CNOT
            oracle.cx(0, 1)

    return oracle.to_gate(label="BalancedOracle")

    def random_oracle(self) -> QuantumCircuit:
        """
        Create a random oracle that is either constant or balanced, but the type is not revealed.

        :return: A Gate representing the random oracle.
        """
        if np.random.rand() > 0.5:
            oracle_gate = self.constant_oracle()
        else:
            oracle_gate = self.balanced_oracle()

        # Create a wrapper circuit with the "Random Oracle" label
        random_oracle_circuit = QuantumCircuit(2)
        random_oracle_circuit.append(oracle_gate, range(2))

        return random_oracle_circuit.to_gate(label="Random Oracle")
