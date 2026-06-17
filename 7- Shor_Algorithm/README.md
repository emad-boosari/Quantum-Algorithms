# Shor Algorithm
__Shor's algorithm__ is a quantum computer algorithm for finding the _prime factors of an integer_. It was developed in 1994 by the American mathematician __Peter Shor__. On a quantum computer, to factor an integer $N$, Shor's algorithm runs in polynomial time, meaning the time taken is polynomial in $log N$, the size of the integer given as input


## What is the story? Classical approach
Consider a positive integer Number like $N$. We are interested in the factor $p$ of $N$ if it exists. 

### Classical Approach

To determine the prime factors we can use a simple approach step by step.
1. If $N$ is a prime number declare that it is and exit.
2. If $N$ is not a prime number, then choose a random integer $a \in (1,N)$  
   * Calculate $gcd(a,N)$         
     * if $gcd(a,N) \neq 1$, then return the $gcd(a,N)$ as a prime factor
     * if $gcd(a,N) = 1$, proceed to __step 3__.
3. find the period $r$ in such a way that for the function $f_{a,N}(x) = a^x \text{mod} N$ 
$$f_{a,N}(r+1)= f_{a,N}(1) $$
or in general
$$f_{a,N}(r+s)= f_{a,N}(s) \quad \text{for} \qquad s>1 $$

4. if period $r$ is odd or if $a^r \equiv -1$ $\text{mod}$ $N$, then return to __step 2__ and choose another $a$.
     * Attention: $a\equiv b$ $\text{mod}$ $N$ if and only if $a$ $\text{mod}$ $N$ = $b$ $\text{mod}$ $N$
       * Example: $17 \equiv 2\text{mod} 15$
5. prime factors are 
   $$p_1 = \text{gcd}(a^{r/2}+1,N), \qquad p_2 = \text{gcd}(a^{r/2}-1,N)$$

### First Examples $N=15$ and $a=7$
As a first example, let me consider $N=15$ and $a=7$ which is a famous example in quantum computation literature. As a naive person, we can find the period just by following the numbers below:

  * $f_{7,15}(0) = 7^0 \text{mod} 15 = 1$
  * $f_{7,15}(1) = 7^1 \text{mod} 15 = 7$
  * $f_{7,15}(2) = 7^2 \text{mod} 15 = 4$
  * $f_{7,15}(3) = 7^3 \text{mod} 15 = 13$
  * $f_{7,15}(4) = 7^4 \text{mod} 15 = 1$
  * $f_{7,15}(5) = 7^5 \text{mod} 15 = 7$
  * $f_{7,15}(6) = 7^6 \text{mod} 15 = 4$
  * $f_{7,15}(7) = 7^7 \text{mod} 15 = 13$ 

 In this case, we can see the period is *four* $(r=4)$. Now we can use this period (r=4) in order to find the prime factors of the number 15 in the following way:
   * $$p_1 = \text{gcd}(7^{4/2}+1,15)=\text{gcd}(50,15)=5 \qquad  p_2 = \text{gcd}(7^{4/2}-1,15)=\text{gcd}(48,15)=3$$
 
### First Examples $N=35$ and $a=3$
For the second example we will have:
  * $f_{3,35}(0) = 3^0 \text{mod} 35 = 1$
  * $f_{3,35}(1) = 3^1 \text{mod} 35 = 3$
  * $f_{3,35}(2) = 3^2 \text{mod} 35 = 9$
  * $f_{3,35}(3) = 3^3 \text{mod} 35 = 27$
  * $f_{3,35}(4) = 3^4 \text{mod} 35 = 11$
  * $f_{3,35}(5) = 3^5 \text{mod} 35 = 33$
  * $f_{3,35}(6) = 3^6 \text{mod} 35 = 29$
  * $f_{3,35}(7) = 3^7 \text{mod} 35 = 17$
  * $f_{3,35}(8) = 3^8 \text{mod} 35 = 16$
  * $f_{3,35}(9) = 3^9 \text{mod} 35 = 13$
  * $f_{3,35}(10) = 3^{10} \text{mod} 35 = 4$
  * $f_{3,35}(11) = 3^{11} \text{mod} 35 = 12$
  * $f_{3,35}(12) = 3^{12} \text{mod} 35 = 1$
  * $f_{3,35}(13) = 3^{13} \text{mod} 35 = 3$
  * $f_{3,35}(14) = 3^{14} \text{mod} 35 = 9$
  * $f_{3,35}(15) = 3^{15} \text{mod} 35 = 27$
 
 So the period $r$ is 12 and the prime factors are
   $$p_1 = \text{gcd}(3^{12/2}+1,35)=\text{gcd}(730,35)=5 \qquad   p_2 = \text{gcd}(3^{12/2}-1,35)=\text{gcd}(728,35)=7$$
 
## What is the story of using Quantum Computation?
The story is the same as the classic, but here we just want to calculate the period of function using quantum features. To do this P. Shor has applied quantum phase estimation like below. Let me consider the second example $(N=35, a=3)$. Suppose the following unitary operator:

$$U|y\rangle = |ay \pmod N\rangle$$

1. $U|1\rangle = |(3\times 1) \pmod {35}\rangle = |3\rangle$
2. $U^2|1\rangle   = U(U|1\rangle)      = U|3\rangle = |(3\times 3) \pmod {35}\rangle = |9\rangle$
3. $U^3|1\rangle   = U(U^2|1\rangle)    = U|9\rangle = U(3\times 9) \pmod {35}\rangle = |27\rangle$
4. $U^4|1\rangle   = U(U^3|1\rangle)    = U|27\rangle = U(3\times 27) \pmod {35}\rangle = |11\rangle$
5. $U^5|1\rangle   = U(U^4|1\rangle)    = U|11\rangle = U(3\times 11) \pmod {35}\rangle = |33\rangle$
6. $U^6|1\rangle   = U(U^5|1\rangle)    = U|33\rangle = U(3\times 33) \pmod {35}\rangle = |29\rangle$
7. $U^7|1\rangle   = U(U^6|1\rangle)    = U|29\rangle = U(3\times 29) \pmod {35}\rangle = |17\rangle$
8. $U^8|1\rangle   = U(U^7|1\rangle)    = U|17\rangle = U(3\times 17) \pmod {35}\rangle = |16\rangle$
9. $U^9|1\rangle   = U|16\rangle = |13\rangle$
10. $U^{10}|1\rangle = U|13\rangle  = |4\rangle$
11. $U^{11}|1\rangle = U|4\rangle  = |12\rangle$
12. $U^{12}|1\rangle = U|12\rangle  = |1\rangle$
13. $U^{13}|1\rangle = U|1\rangle  = |3\rangle$

***
So a superposition of these states in this cycle $(|u_0\rangle)$ would be an eigenstate of $U$:
$$|u_0\rangle = \frac{1}{\sqrt{r}} \sum_{k=0}^{r-1} |a^k \pmod {N}\rangle$$


In our case, it can be written as 
$$|u_0\rangle = \frac{1}{\sqrt{12}} \bigg(|1\rangle+|3\rangle+|9\rangle+|27\rangle+\ldots+|4\rangle+|12\rangle\bigg) $$

$$ |u_1\rangle = U|u_0\rangle = \frac{1}{\sqrt{12}} \bigg(U|1\rangle+U|3\rangle+U|9\rangle+U|27\rangle+\ldots+U|4\rangle+U|12\rangle\bigg)$$

$$ = \frac{1}{\sqrt{12}} \bigg(U|3\rangle+U|9\rangle+U|27\rangle+U|11\rangle+\ldots+U|12\rangle+U|1\rangle\bigg) = |u_0\rangle $$


the eigenvalue is 1. But an interesting case could be one in which the phase is different for each of this computational basis.
$$|u_1\rangle = \frac{1}{\sqrt{r}} \sum_{k=0}^{r-1} e^{\frac{-2\pi ik}{r}}|a^k \text{mod} N\rangle.$$

By using the result of $U|u_0\rangle$ we can easily reach to 
$$|u_1\rangle = e^{\frac{2\pi i}{r}}|u_1\rangle$$

we can see the period $r=12$ appears in the denominator of the phase.

