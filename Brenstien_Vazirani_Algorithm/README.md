# BV Algorithm Directory

The Bernstein-Vazirani (BV) algorithm, designed by Ethan Bernstein and Umesh Vazirani in 1992, demonstrates the advantages of quantum algorithms over classical ones. This algorithm is a special case of the Deutsch-Jozsa algorithm, where the function $f(x)$ is defined as:

$$f(x) = x \cdot c = c_{n-1}x_{n-1} + c_{n-2}x_{n-2} + \cdots + c_1x_1 + c_0x_0 \pmod{2} $$

Here, $c = c_{n-1}c_{n-2}\cdots c_0$ is an $n$-bit binary number. The goal is to find $c$ using the fewest evaluations of $f(x)$.

## Classical Solution
Classically, solving the BV problem requires $n$ queries, each providing one bit of information. By evaluating $f(x)$ for each power of 2, we can reveal the secret string $c$:

$$f(0\cdots 00) &= c_0,\quad f(0\cdots 01) = c_1, \quad f(0\cdots 10) = c_2, \quad \cdots, \quad f(1\cdots 11) =  c_{n-1} $$

Each query provides one bit of the secret string, thus requiring $n$ queries to fully reconstruct it.
## Quantum Solution
The quantum solution to the BV problem requires only a single query to retrieve the secret string $c$. The steps involved are similar to those in the Deutsch-Jozsa algorithm. The state $\ket{\psi_3}$ is represented as:

$$ \ket{\psi_3} = \frac{1}{2^n}\sum_{y=0}^{2^n-1}\sum_{x=0}^{2^n-1} (-1)^{x \cdot c} (-1)^{x \cdot y}\ket{y} \ket{-} $$
    
$$ \ket{\psi_3} = \frac{1}{2^n}\sum_{x=0}^{2^n-1} \sum_{y=0}^{2^n-1} (-1)^{x \cdot (c \oplus y)} \ket{y} \ket{-} $$
To analyze $\ket{\psi_3}$, we will use the equation that we have already presented in the Deutsch-Jozsa algorithm:

$$ \frac{1}{2^n}\sum_{x=0}^{2^n-1} (-1)^{x \cdot y} = \delta_{0y} $$ 

Thus, we get:

$$\frac{1}{2^n}\sum_{x=0}^{2^n-1} (-1)^{x \cdot (c \oplus y)} = \delta_{0(c \oplus y)} $$

This means that the sum is non-zero only when $y = c$, which makes $c \oplus y = 0 \cdots 0$. Therefore:

$$\ket{\psi_3} = \sum_{y=0}^{2^n-1} \delta_{0(c \oplus y)} \ket{y} \ket{-} $$

$$ \ket{\psi_3} =\bigg[\delta_{0(c \oplus 0)} \ket{0} + \delta_{0(c \oplus 1)} \ket{1} + \cdots + \delta_{0(c \oplus c)} \ket{c} + \cdots + \delta_{0(c \oplus (2^n-1))} \ket{2^n-1}\bigg] \ket{-} = \ket{c} \ket{-} $$

By measuring the first register, we can determine the secret string $c$ with just one query.


