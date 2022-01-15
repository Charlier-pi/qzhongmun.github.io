# Algorithm
## Stable Matching
a stable matching is a perfect matching with no unstable pairs

stable matchings doesn't always exit

## Unstable Matching
```
/*
Def. Given a perfect matching M , hospital h and student s form an unstable pair if both: 
* h prefers s to matched student. 
* s prefers h to matched hospital.
*/

A-Y  //* h(A) prefers s(Y) to(rather than) matched student(red part).
     //* s prefers h to matched hospital.
```

Note: if something is not a valid pair, it is not an unstable pair.   

For example, suppose that the question is as follows:  

Questinos: 

Consider an instance of Stable Matching with the following preference lists. Suppose that the matching is A-Z, B-Y, C-X, D-V, E-W. Select all pairs that are unstable with respect to this matching.

```
A:Y,V,X,Z,W
B:X,Z,W,V,Y
C:Y,X,Z,V,W
D:X,Y,V,Z,W
E:W,V,X,Y,Z

V:C,A,D,B,E
W:E,A,B,D,C
X:E,A,B,D,C
Y:D,C,B,A,E
Z:D,A,E,B,C
```
Answers: 

- [x] D-X 
- [ ] A-Y
- [ ] E-W
- [ ] E-X
- [ ] E-C
- [x] C-Y
- [ ] B-Z
- [ ] None of these pairs is unstable


First of all, the pair E-C is not valid (all pairs should be of the form hospital-student). This option should not be selected.  

Also, the pair E-W is already in the matching. It should not be selected either. 

Let's look at the remaining choices.  

D is matched to V, but prefers X, and X is matched to C, but prefers D, so D-X is unstable. Select this option. 

A-Y is stable, since Y prefers B to A. So A-Y should be left unchecked. 

E-X is also stable, as E is happier with W than with X. Leave unchecked. 

C-Y is again unstable, since C prefers Y to anybody (in particular to X) and Y likes C more than B. Select this option too. 

B-Z is also stable, since Z prefers A to B. Leave unselected. 


