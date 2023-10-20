# Grover Adaptive Search (GAS) Algorithm 
The Grover Adaptive Search Algorithm (GASA) extends the well-known Grover's algorithm, a quantum search algorithm that offers a quadratic speedup over classical search algorithms. GASA excels in enabling efficient quantum searches in unstructured databases with an unknown number of marked items.

The algorithm initiates with a standard Grover iteration to search for marked items. Subsequently, it measures the number of marked items and employs this information for adaptive adjustment, tailoring the required number of Grover iterations to find the marked items efficiently. This adaptive approach significantly reduces the number of iterations needed compared to the fixed iteration count in the standard Grover's algorithm.

GASA boasts versatile applications, such as searching for multiple solutions to a problem or sifting through solutions in noisy or unreliable settings where the number of marked items may fluctuate.

In summary, GASA stands as a robust quantum algorithm offering an efficient means to search for marked items in unstructured databases.

For an in-depth discussion, please refer to the following link on the Qiskit page: 
https://qiskit.org/documentation/optimization/tutorials/04_grover_optimizer.html







