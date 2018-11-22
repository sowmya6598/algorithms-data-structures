# Parallel Algorithms

Implement the algorithm which computes in parallel a matrix product of N matrices:

```
M=M1[m×n]⋅M2[n×k]⋅M3[k×l]⋅…⋅MN−1[r×p]⋅MN[p×q],
```

where matrix sizes are given inside square brackets. The main task (T) i.e.,  multiplication of matrices, has to be split into subtask (T1,T2,…Tm) to be proceeded in parallel. For example:

```
T=M1⋅M2⋅M3⋅M4⋅M5⋅M6⋅M7⋅M8⋅M9⟶
T1=M1⋅M2⋅M3, T2=M4⋅M5⋅M6, T3=M7⋅M8⋅M9.
```

After completing T1,T2,T3, the algorithm proceeds with the main task, T.
