# Programming Assignment 3: Highest Value Longest Common Sequence

### Xabier Sienra (80213894)
### Hailey Pham (24752485)


### Question 1: Empirical Comparison
Use at least 10 nontrivial input files (i.e., contain strings of length at least 25). Graph the
runtime of the 10 files.

### Question 2: Recurrence Equation
Give a recurrence that is the basis of a dynamic programming algorithm to compute the
HVLCS of strings A and B. You must provide the appropriate base cases, and explain why
your recurrence is correct.

OPT(i,j) = maximum value of current sequence ending in a<sub>i</sub>
c = value of current letter j


$$
OPT(i,j)=
\begin{cases}
0 & \quad \text{$i = 0 \wedge j = 0$}\\ 
max(OPT(i-1, j), OPT(i, j-1)) & \quad \text{$if a_i \neq b_j$}\\
v(a_i)+OPT(i-1, j-1)  & \quad \text{$if a_i = b_j$}
\end{cases}
$$


### Question 3: Big-Oh
Give pseudocode of an algorithm to compute the length of the HVLCS of given strings A
and B. What is the runtime of your algorithm?

