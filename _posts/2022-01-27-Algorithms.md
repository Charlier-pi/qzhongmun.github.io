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







