# Algorithms

word RAM : unbound
exception: bucket sort: bound

lower bound: sorting

### STABLE	MATCHING

Unstable pair.	Hospital h and student s form an unstable pair if both:
	* h prefers s to one of its admitted students.
	* s prefers h to assigned hospital.

perfect matching only if the number of h = the number of s

perfect matching may not be stable matching

Stable matching(n*n array): perfect matching with stable pairs

Stable roommate problem.
* 2 n people; each person ranks others from 1 to 2 n – 1.（array is n*(n-1)）
In the stable roommate problem, stable matchings need not exist.

Gale–Shapley deferred acceptance algorithm
An intuitive method that guarantees to find a stable matching.
The Gale–Shapley algorithm guarantees  to find a stable matching for any problem instance.
all executions of Gale–Shapley lead to the same stable matching

ppt2-page16: it should be h–s is unstable.

How many rounds will Gale-Shapley take in the worst case for n hospitals and n students? What does the worst case look like? 
n*(n-1)+1

0 1 2 3      0 1 2 3
A X Y Z      X B C A
B Y X Z      Y C A B
C X Y Z      Z A B C

3*2+1=7

all executions of Gale–Shapley lead to the same stable matching, even though an instance can have several stable matchings  and the algorithm is nondeterministic

Def.Student s is a valid partner for hospital h if there exists any stable  matching in which h and s are matched.
For Example:
all stable matchings in those two arraies:	
S = { A-X, B-Y, C-Z}      and S′ = { A-Y, B-X, C-Z}
* Both X and Y are valid partners for A.   if A prefer X, then X is best valid partner
* Both X and Y are valid partners for B.   if B prefer X, then X is best valid partner
* Z is the only valid partner for C.       C's best valid partner is Z










