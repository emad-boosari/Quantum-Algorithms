\section{Introduction}

In this repository, I am going to explain the Deutsch, Deutsch-Jozsa, and Bernstein–Vazirani algorithms. The related Qiskit files for solving these problems will be included using various approaches.

Before diving into the explanation of our quantum algorithms, it's essential to introduce the "phase kickback" trick, a well-known effect in many quantum algorithms. To make this effect clear, consider the following unitary operator \(U_{f}\):

\[
U_f|x\rangle|y\rangle=|x\rangle|y \oplus f(x)\rangle
\]

Now, let's apply \(U_f\) to the state \(\frac{|0\rangle+|1\rangle}{\sqrt{2}} |0\rangle\):

\[
U_f \left(\frac{|0\rangle+|1\rangle}{\sqrt{2}}\right) |0\rangle = \frac{1}{\sqrt{2}}(|0\rangle|f(0)\rangle+|1\rangle|f(1)\rangle)
\]

\[
\begin{eqnarray}
U_f|x\rangle|-\rangle &=& U_f |x\rangle \frac{(|0\rangle - |1\rangle)}{\sqrt{2}} =  |x\rangle \frac{(|f(x)\rangle - |1+f(x)\rangle)}{\sqrt{2}}
\end{eqnarray}
\]

- For \(f(x) = 0\), we have:
  \[U_f|x\rangle|-\rangle =  |x\rangle\frac{(|0\rangle - |1\rangle)}{\sqrt{2}}=|x\rangle|-\rangle\]

- For \(f(x) = 1\), we have:
  \[U_f|x\rangle|-\rangle =  |x\rangle\frac{(|1\rangle - |0\rangle)}{\sqrt{2}}= - |x\rangle|-\rangle\]

In summary, the effect of \(U_f\) can be expressed as:

\[U_f|x\rangle|-\rangle = (-1)^{f(x)}|x\rangle|-\rangle\]

\section{Conclusion}

The general form can be represented as follows:

\[U_f: \big(a|0\rangle + b |1\rangle\big)|-\rangle  \longmapsto \big(a|0\rangle - b |1\rangle\big)|-\rangle\]

\section{Deutsch Algorithm}

The Deutsch algorithm is one of the simplest algorithms in quantum computation. It's a contrived algorithm designed to illustrate the quantum principles of parallelism and interference, which are fundamental in useful quantum algorithms.

\subsection{The Deutsch Problem}

Let \(f:\{0,1\} \longmapsto \{0,1\}\) be a binary function. There are four possible representations:

1. \(f(0)=0\) and \(f(1)=0\)
2. \(f(0)=0\) and \(f(1)=1\)
3. \(f(0)=1\) and \(f(1)=0\)
4. \(f(0)=1\) and \(f(1)=1\)

The first and fourth functions are "Constant," while the second and third functions are "Balanced." The goal is to determine whether a given function is Constant or Balanced.

\subsubsection{Classical Solution}

Classically, at least two queries are needed to determine if a function is Constant or Balanced. For example, passing '0' provides information about \(f(0)\), but a second query is required to deduce if the function is Constant or Balanced. This classical approach necessitates two queries.

\subsubsection{Quantum Solution}

In the quantum version, using qubits \(|0\rangle\) and \(|1\rangle\) to represent classical bits '0' and '1', a unitary operator \(U_{f(x)}\) distinguishes Constant from Balanced functions:

\[U_f|x\rangle|y\rangle=|x\rangle|y \oplus f(x)\rangle\]

In the quantum version, both \(f(0)\) and \(f(1)\) can be determined with a single query. The Deutsch algorithm leverages quantum interference to efficiently obtain global information about the function \(f(x)\), achieving this more efficiently than classical methods.

\subsection{Deutsch Algorithm Circuit}

Below is the circuit representation of the Deutsch algorithm:

\begin{figure}[h]
\centering
\includegraphics[scale=0.5]{deutsch_algorithm_circuit.png}
\caption{Deutsch Algorithm Circuit}
\end{figure}

The algorithm is executed as follows:

\begin{enumerate}
  \item Initialize the quantum circuit with two qubits.
  \item Apply a Hadamard gate (H) to the first qubit.
  \item Apply the oracle operator \(U_f\) to the qubits.
  \item Apply Hadamard gates to both qubits.
  \item Measure the first qubit.
  \item If the measurement outcome is '0', the function is Constant; if it's '1', the function is Balanced.
\end{enumerate}

\section{Deutsch-Jozsa Algorithm}

\[
U_f|\vec{x}\rangle|y\rangle=|\vec{x}\rangle|y \oplus f(\vec{x})\rangle
\]

\subsection{Deutsch-Jozsa Algorithm Circuit}

The circuit for the Deutsch-Jozsa algorithm is shown below:

\begin{figure}[h]
\centering
\includegraphics[scale=0.5]{deutsch_jozsa_algorithm_circuit.png}
\caption{Deutsch-Jozsa Algorithm Circuit}
\end{figure}

The algorithm is executed as follows:

\begin{enumerate}
  \item Initialize the quantum circuit with \(n+1\) qubits.
  \item Apply a Hadamard gate (H) to the first \(n\) qubits.
  \item Apply the oracle operator \(U_f\) to the qubits.
  \item Apply Hadamard gates to the first \(n\) qubits.
  \item Measure the first \(n\) qubits.
  \item If all measurements are '0', the function is Constant; if any measurement is '1', the function is Balanced.
\end{enumerate}
