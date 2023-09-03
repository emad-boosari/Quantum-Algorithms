# Simon’s Problem
The final example of simple quantum algorithms is Simon’s algorithm. Let us consider a function (oracle) $f : {0, 1}^n \rightarrow \{0, 1}^n$ such that $\{\}$

1. $f$ is 2 to 1; namely, for any $x_1$, there is one and only one $x_2 = x_1$ such that $f(x_1) = f(x_2)$.
2. $f$ is __periodic__; namely, there exists $p \in {0, 1}^n$ such that $f(x \oplus p) = f(x)$, $\forall x \in {0, 1}^n$,

where $\oplus$ is a bitwise addition mod 2.
The function $f$ is made of $n$ component functions $f_k : {0, 1}^n \rightarrow {0, 1}$ as $f = (f_1, f_2, . . . , f_n)$


Suppose we want to find the period $p$, given an unknown oracle $f$. Since $p$ can be any number between $00\cdots 0$ and $11\cdots 1$, we have to try $\sim$ $2^n$ possibilities classically before we hit the right number. It is shown below that the number of trials required to find $p$ is reduced to $O(n)$ if Simon’s algorithm is employed.
The algorithm is decomposed into the following steps:
