# Deutsch and Deutsch-Jozsa Algorithms

In this repository, I am going to explain **Deutsch**, and **Deutsch-Jozsa**. The related Qiskit files to solve this problems can be found in this repo.

## Introduction
Before beginning with more complex and "useful" quantum algorithms, it is beneficial to start with simpler examples to illustrate the unique advantages and principles of quantum computing. In this lecture, we will explore three fundamental quantum algorithms: Deutsch's Algorithm, the Deutsch-Jozsa Algorithm, and the Bernstein-Vazirani Algorithm. These algorithms are not just theoretical exercises; they demonstrate key quantum concepts such as superposition, interference, and entanglement, which enable quantum computers to solve certain problems more efficiently than classical counterparts. By understanding these basic algorithms, we lay a solid foundation for appreciating the power and potential of quantum computing.

### Phase Kickback

Before delving into quantum algorithms, it's essential to understand the "phase kickback" phenomenon, a crucial concept in many quantum algorithms. Consider the unitary operator \( U_{f} \) defined as follows:

$$ U_f|x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle $$

$$ U_f \left(\frac{|0\rangle+|1\rangle}{\sqrt{2}} \right)|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle|f(0)\rangle+|1\rangle|f(1)\rangle) $$

$$ U_f|x\rangle|-\rangle = U_f |x\rangle\frac{\big(|0\rangle - |1\rangle\big)}{\sqrt{2}} = |x\rangle\frac{\big(|f(x)\rangle - |1+f(x)\rangle\big)}{\sqrt{2}}
$$

- For $f(x)=0$
  
$$ U_f|x\rangle|-\rangle = |x\rangle\frac{\big(|0\rangle - |1\rangle\big)}{\sqrt{2}}=|x\rangle|-\rangle$$
- For $f(x)=1$

$$ U_f|x\rangle|-\rangle = |x\rangle\frac{\big(|1\rangle - |0\rangle\big)}{\sqrt{2}}=- |x\rangle|-\rangle $$

These equations can be summarized as follows:

$$U_f|x\rangle|-\rangle = (-1)^{f(x)}|x\rangle|-\rangle $$

### Conclusion

The general form can be represented as:
$$ U_f: \big(a|0\rangle + b |1\rangle\big)|-\rangle  \longrightarrow \big(a|0\rangle - b |1\rangle\big)|-\rangle $$

Before starting to express our quantum algorithms, it is better to introduce the "_phase kickedback_" trick which is a well-known effect in many quantum algorithms. To make this effect clear, let me suppose the following unitary operator $U_{f}$.

$$U_f|x\rangle|y\rangle=|x\rangle|y \oplus	f(x)\rangle$$

$$U_f \bigg(\frac{|0\rangle+|1\rangle}{\sqrt{2}} \bigg)|0\rangle=\bigg(\frac{|0\rangle|0 \oplus f(0)\rangle+|1\rangle|0 \oplus f(1)\rangle}{\sqrt{2}} \bigg)=\frac{1}{\sqrt{2}}(|0\rangle|f(0)\rangle+|1\rangle|f(1)\rangle)$$.

$$\begin{eqnarray}
U_f|x\rangle|-\rangle &=& U_f |x\rangle\dfrac{\big(|0\rangle - |1\rangle\big)}{\sqrt{2}} =  |x\rangle\dfrac{\big(|f(x)\rangle - |1+f(x)\rangle\big)}{\sqrt{2}}
\end{eqnarray}
$$
 - for $f(x)=0 \longmapsto U_f|x\rangle|-\rangle =  |x\rangle\dfrac{\big(|0\rangle - |1\rangle\big)}{\sqrt{2}}=|x\rangle|-\rangle$
 - for $f(x)=1 \longmapsto U_f|x\rangle|-\rangle =  |x\rangle\dfrac{\big(|1\rangle - |0\rangle\big)}{\sqrt{2}}=- |x\rangle|-\rangle$

We can summarize above equations in the following rules
 $$U_f|x\rangle|-\rangle =  (-1)^{f(x)}|x\rangle|-\rangle$$




## Conclusion
The general form can be represented as follows

$$ U_f: \big(a|0\rangle + b |1\rangle\big)|-\rangle  \longmapsto \big(a|0\rangle - b |1\rangle\big)|-\rangle$$



## Deutsch Algorithm
**Deutsch algorithm** is one of the simplest algorithms in the quantum computation. It is a *contrive algorithm* which means it is not going to solve an real-world problem. Its main aim is to prove quantum computation can be faster than its classical counterparts. It is easy example to understand key ideas of *quantum parallelism* and *quantum interfernce* that are used in all usefull quantum algorithms.


### The Deutsch problem

Let $f:\braket \{0,1\} \longmapsto \{0,1\}$ be be a binary function. Thus it is simple to four possible represention of $f$, namely

 - 1. $f(0)=0$ and $f(1)=0$
 - 2. $f(0)=0$ and $f(1)=1$
 - 3. $f(0)=1$ and $f(1)=0$
 - 4. $f(0)=1$ and $f(1)=1$

First and fourth functions are *Constant* and second and third functions are *Balanced*. Let me consider to select randomly one function among these four. How can we evaluate which function is this? 

#### Classical solution

From classical point of view First we pass $'0'$ and evalute the outcome of $f(x)$, regardless of the value of the $f(0)$ whether may be $0$ or $1$, we need a second query to figure out which function is this. Thus classical algorithm needs at least two query to find the function $f(x)$ is constant or balanced.

The question is this, may we find a method which can evaluate a unknown function $f(x)$ is constant or balanced? fortunately, our answer is yes. Deutsch algorithm can evaluate the answer just with one query.

#### Quantum Solution

In the Quantum version, we consider classic bits $0$ and $1$ correspond to quantum bits (qubits) $|0\rangle$ and $|1\rangle$ respectively. For a unitary oprator like $U_{f(x)}$ with the following feature:

$$U_f|x\rangle|y\rangle=|x\rangle|y \oplus	f(x)\rangle$$

So it seems, we can easily find value of $f(0)$ and $f(1)$ because:
 - $U_f|0\rangle|0\rangle=|0\rangle|0 \oplus	f(0)\rangle=|0\rangle|f(0)\rangle$,
 - $U_f|1\rangle|0\rangle=|1\rangle|0 \oplus	f(1)\rangle=|0\rangle|f(1)\rangle$,
 
and by using a superposition state for $|x\rangle$ we will  have

$$U_f \bigg(\frac{|0\rangle+|1\rangle}{\sqrt{2}} \bigg)|0\rangle=\bigg(\frac{|0\rangle|0 \oplus f(0)\rangle+|1\rangle|0 \oplus f(1)\rangle}{\sqrt{2}} \bigg)=\frac{1}{\sqrt{2}}(|0\rangle|f(0)\rangle+|1\rangle|f(1)\rangle)$$.

It seems $U_f$ recalled both value of $f(0)$ and $f(1)$ in the above equation. But we know in the measurnment part we will obtain one of these states. Thus, so far the quantum mechanics isn't helpful. But remmeber the Deutsch problem, it doesn't need to individual value of $f(x)$, instead it want the value of $f(0)\oplus f(1)$. 

The Deutsch algorithm illustrates how we can use quantum interference to obtain such global information about the function $f(x)$, and how this can be done more efficiently than is possible classically.

Leave the previous calculation and look at the following circuit

![image](https://user-images.githubusercontent.com/58440271/208507372-e11e1aee-cee2-495c-a161-f9eacf27ea2b.png)

I'll show each quantum state that is shown in the above figure.

### $|\psi_0\rangle$:

$$|\psi_0\rangle=|0\rangle\bigg(\frac{|0\rangle - |1\rangle}{\sqrt{2}} \bigg)$$

### $|\psi_1\rangle$:

$$|\psi_1\rangle=(H\otimes I)|\psi_0\rangle=\bigg(\frac{|0\rangle + |1\rangle}{\sqrt{2}} \bigg)\bigg(\frac{|0\rangle - |1\rangle}{\sqrt{2}} \bigg)$$

### $|\psi_2\rangle$:

$$ \begin{eqnarray}
|\psi_2\rangle &=& U_{f}|\psi_1\rangle |\psi_0\rangle=U_{f}\frac{|0\rangle}{\sqrt{2}}\bigg(\frac{|0\rangle - |1\rangle}{\sqrt{2}} \bigg) +U_{f}\frac{ |1\rangle}{\sqrt{2}}\bigg(\frac{|0\rangle - |1\rangle}{\sqrt{2}} \bigg) \\
&=& \frac{|0\rangle}{\sqrt{2}}\bigg(\frac{|f(0)\rangle - |1 \oplus f(0)\rangle}{\sqrt{2}} \bigg) +\frac{ |1\rangle}{\sqrt{2}}\bigg(\frac{|f(1)\rangle - |1\oplus f(1)\rangle}{\sqrt{2}} \bigg)
\end{eqnarray}$$


by using the following equation we can rewrite the $|\psi_2$ in a new form

$$U_f |x\rangle\bigg(\frac{|0\rangle-|1\rangle}{\sqrt{2}}\bigg)=(=1)^{f(x)}|x\rangle\bigg(\frac{|0\rangle-|1\rangle}{\sqrt{2}}\bigg)$$

thus

$$|\psi_2\rangle=\frac{1}{\sqrt{2}}\Bigg[\big(-1\big)^{f(0)}|0\rangle +\big(-1\big)^{f(1)}|1\rangle \Bigg]\bigg(\frac{|0\rangle - |1\rangle}{\sqrt{2}} \bigg)$$

### $|\psi_3\rangle$:

$$ \begin{eqnarray}
|\psi_3\rangle &=& (H\otimes I)|\psi_2\rangle = \frac{1}{2\sqrt{2}} \bigg((-1)^{f(0)}\Big(|0\rangle + |1\rangle \Big)|-\rangle + (-1)^{f(1)} \Big(|0\rangle - |1\rangle \Big)|-\rangle\bigg) \\
&=& \frac{1}{2\sqrt{2}} \Bigg( \Big((-1)^{f(0)} + (-1)^{f(1)} \Big)|0\rangle |-\rangle + \Big((-1)^{f(0)} - (-1)^{f(1)} \Big)|1\rangle |-\rangle  \Bigg)
\end{eqnarray}$$

ow we are ready to interpert the state $|\psi_3\rangle$ for constant and balanced functions.

 - for a constant function $f(0)=f(1)$ we will have
 
 $$ |\psi_3\rangle = \frac{1}{2\sqrt{2}} \Big((-1)^{f(0)} + (-1)^{f(1)} \Big)|0\rangle $$

 
 - for a balanced function $f(0) \neq f(1)$ we will have 
 
 $$ |\psi_3\rangle = \frac{1}{2\sqrt{2}} \Big((-1)^{f(0)} - (-1)^{f(1)} \Big)|1\rangle $$

 ## Conclusion
 Based on the above interpertation we can just do a single measurnment over the first qubit, and if it was yield to "0" $f(x)$ is constant and otherwise it is balanced.


## Deutsch-Jozsa Algorithm

 $$U_f|\vec{x}\rangle|y\rangle=|\vec{x}\rangle|y \oplus	f(\vec{x})\rangle$$
 
![image](https://user-images.githubusercontent.com/58440271/208755940-ecfe2228-4e16-4793-95ae-487883980588.png)



I'll show each quantum state that is shown in the above figure.

### $|\psi_0\rangle$:

$$|\psi_0\rangle=|\bf{0}\rangle^{\otimes n}\bigg(\frac{|0\rangle - |1\rangle}{\sqrt{2}} \bigg)$$

### $|\psi_1\rangle$:

$$\begin{equation}
|\psi_1\rangle=(H^{\otimes n}\otimes I)|\psi_0\rangle = \bigg(\frac{|0\rangle + |1\rangle}{\sqrt{2}} \bigg)^{\otimes n}\bigg(\frac{|0\rangle - |1\rangle}{\sqrt{2}} \bigg) = \frac{1}{\sqrt{2^n}}\sum_{x}^{2^n-1} |\bf{x}\rangle \otimes|-\rangle
\end{equation}$$

### $|\psi_2\rangle$:

by using the following equation we can rewrite the $|\psi_2\rangle$ in a new form

$$ \begin{eqnarray}
U_f |\bf{x}\rangle\bigg(\frac{|0\rangle-|1\rangle}{\sqrt{2}}\bigg)=(-1)^{f(\bf{x})}|\bf{x}\rangle \bigg(\frac{|0\rangle-|1\rangle}{\sqrt{2}}\bigg)
\end{eqnarray}$$

thus

$$ \begin{eqnarray}
|\psi_2\rangle = U_f|\psi_1\rangle = U_f\frac{1}{\sqrt{2^n}}\sum_{x}^{2^n-1} |\bf{x}\rangle \otimes|-\rangle = \frac{1}{\sqrt{2^n}}\sum_{x}^{2^n-1} \big(-1\big)^{f(\bf{x})} |\bf{x}\rangle \otimes|-\rangle
\end{eqnarray}$$

### $|\psi_3\rangle$:

$$ \begin{eqnarray}
|\psi_3\rangle &=& (H^{\otimes n}\otimes I)|\psi_2\rangle = \frac{1}{\sqrt{2^n}}\sum_{x}^{2^n-1}\sum_{y}^{2^n-1} \big(-1\big)^{f(\bf{0})} \big(-1\big)^{\bf{x}.\bf{y}}  |\bf{y}\rangle \otimes|-\rangle
\end{eqnarray}$$

Similar to Deutsch algorithm we are intrested in the first register and leave the second. If entire qubits are in the ground state $|000...0\rangle$ it means the function $f(x)$ is *Constant*. Thus we just consider $|\psi_3\rangle$ for $y=0$:

$$ |\psi_3\rangle = \frac{1}{\sqrt{2^n}}\sum_{x}^{2^n-1} \big(-1\big)^{f(\bf{x})} |\bf{0}\rangle \otimes |-\rangle $$

So, the probability of collapsing to $|0\rangle$ is totally dependent on $f(x)$. If $f(x)$ is constant at $1$, the top qubits become

$$ \frac{1}{\sqrt{2^n}}\sum_{x}^{2^n-1} |\bf{0}\rangle = -\frac{2^n}{\sqrt{2^n}} |\bf{0}\rangle = -|\bf{0}\rangle$$

if $f(x)$ is constant at $0$, the top qubits become

$$ \frac{1}{\sqrt{2^n}}\sum_{x}^{2^n-1} |\bf{0}\rangle = \frac{2^n}{\sqrt{2^n}} |\bf{0}\rangle = |\bf{0}\rangle$$

This result for a *Balanced* function is simpler, because for half of the $f(x)$ is zero and for other half is one and terms cancel each other: 

$$ \frac{1}{\sqrt{2^n}}\sum_{x}^{2^n-1} |\bf{0}\rangle = \frac{0}{\sqrt{2^n}} |\bf{0}\rangle = 0|\bf{0}\rangle$$

### number of valid functions for a system with $n$ qubits

for each $n$ there is $2^n$ possible states. As an example, for  $n=2$, there is $ 2^2=4$ possible states:

 - $|00\rangle$
 - $|01\rangle$
 - $|10\rangle$
 - $|11\rangle$
 
Now the question is this, for a space with $4$ possible basis states how many functions can be define based?

We know for $f(x)$ for $x\in \{00,01,10,11\}$, we will have
 
$$\Bigg[f(00),f(01),f(10),f(11)\Bigg]$$

and ecah element $f(x)$ can be zero or one, which means $2^4 =16 $ possible function can be defined as follows:
 
 - $\Big[f(00),f(01),f(10),f(11)\Big]$
 
 1. $\Big[0,0,0,0\Big]$, this is a Constant function
 
 2. $\Big[0,0,0,1\Big]$
 
 3. $\Big[0,0,1,0\Big]$
 
 4. $\Big[0,0,1,1\Big]$, this is a Balanced function
 
 5. $\Big[0,1,0,0\Big]$
 
 6. $\Big[0,1,0,1\Big]$, this is a Balanced function
 
 7. $\Big[0,1,1,0\Big]$, this is a Balanced function
 
 8. $\Big[0,1,1,1\Big]$

 9. $\Big[1,0,0,0\Big]$
 
 10. $\Big[1,0,0,1\Big]$, this is a Balanced function
 
 11. $\Big[1,0,1,0\Big]$, this is a Balanced function
 
 12. $\Big[1,0,1,1\Big]$
 
 13. $\Big[1,1,0,0\Big]$, this is a Balanced function
 
 14. $\Big[1,1,0,1\Big]$
 
 15. $\Big[1,1,1,0\Big]$
 
 16. $\Big[1,1,1,1\Big]$, this is a Constant function
 
The half of these function are niether balanced or constant. We have always $2$ Constant functions, and other are Balanced, which is in this case $6$ functions. In this regard, number of al possible functions are

$$2^{2^n}$$

where $n$ is even. Among entire of these functions only $2$ are _Constant_, and the number of balanced function will be written as


$$\frac{(2^n)!}{(2^{n-1})!(2^{n-1})!}$$

## Bernstein-Vazirani Algorithm
