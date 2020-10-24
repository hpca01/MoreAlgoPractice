# MoreAlgoPractice


Taking the algorithmic toolbox course from Coursera for fun.

**Types of algorthms**

- Greedy algorithm problems
  - Break down to sub problems and find an optimal step to solve sub-problem. Given that you can prove that the step you took is a *safe* step. If you cannot prove that it is a safe step, then more than likely, your algorithm will not be optimal.
- Divide and Conquer:
  - Divide main problem into sub-problem and solve, then combine.
    - Eg. Binary Search...looking at upper bound and lower bound of subsections of the **sorted** array($n/2...1$ finding an element in $\log_2n$ time) to find an element. Instead of implementing a recursive approach, my implementation is in place.
    - Inversion Count...interesting problem that uses merge sort's sorting step to do the inversion count. My implementation is not in place, unfortunately it takes up $O(n^2)$ space because I am making sub arrays. One way I can cut down on this is to create the array and then overwrite existing one.
- Dynamic Programming:
  - Esentially computing the solution to sub problems and then working your way using the sub problem solution to the overall problem solution.
    - Eg. Coin Change...finding all the solutions to the minimum amount of coins needed to dispense $1..n$ amount. Build a 1D array with said min amount of coins for $1..n$ amount, then return the $nth$ index in said array.
    - Other more complicated ones require building 2D array, for example the LCS with 2 sequences.

#### Feel free to fork or suggest optimizations! I am open to feedback.
