male(charles1).
male(james1).
male(charles2).
male(james2).
male(george1).

female(catherine).
female(elizabeth).
female(sophia).

parent(charles1,james1).
parent(elizabeth,james1).
parent(charles2,charles1).
parent(catherine,charles1).
parent(james2,charles1).
parent(sophia,elizabeth).
parent(george1,sophia).

mother(X,Y):- parent(X,Y),female(Y).
father(X,Y):- parent(X,Y),male(Y).
sibling(X, Y) :- parent(X,Z), parent(Y,Z), X \= Y.

sister(X,Y):- sibling(X,Y),female(Y).
brother(X,Y):- sibling(X,Y),male(Y).
aunt(X,Y):- parent(X,Z),sister(Z,Y).
uncle(X,Y):- parent(X,Z),brother(Z,Y).
grandparent(X,Y):- parent(X,Z),parent(Z,Y).
cousin(X,Y):- grandparent(X,Z),grandparent(Y,Z),X\=Y.

